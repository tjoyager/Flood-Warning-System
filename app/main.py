from fastapi import FastAPI, HTTPException
from app.models.schemas import TelemetryInput, ResponseMessage
from app.core.database import get_db_connection
from datetime import datetime

app = FastAPI(title="Flood Early Warning API")

def calculate_alert_level(water_level: float, rainfall: float) -> str:
    if water_level > 250 or rainfall > 100:
        return "Bahaya"
    elif 150 <= water_level <= 250 or 50 <= rainfall <= 100:
        return "Waspada"
    else:
        return "Aman"

@app.post("/api/v1/telemetry", response_model=ResponseMessage)
def receive_telemetry(data: TelemetryInput):
    alert_status = calculate_alert_level(data.water_level_cm, data.rainfall_mm)
    
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        insert_telemetry_query = """
            INSERT INTO telemetry_logs (sensor_id, water_level_cm, rainfall_mm)
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_telemetry_query, (data.sensor_id, data.water_level_cm, data.rainfall_mm))
        
        if alert_status != "Aman":
            insert_alert_query = """
                INSERT INTO alert_history (sensor_id, alert_level)
                VALUES (%s, %s)
            """
            cursor.execute(insert_alert_query, (data.sensor_id, alert_status))
            print(f"[{datetime.now()}] ALARM TRIGGERED: {alert_status} for Sensor {data.sensor_id}")
            
        conn.commit()
        cursor.close()
        
        return ResponseMessage(
            status="success",
            alert_level=alert_status,
            message="Data berhasil diproses dan disimpan ke database"
        )
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            conn.close()