from fastapi import FastAPI, HTTPException
from app.models.schemas import TelemetryInput, ResponseMessage
from datetime import datetime

app = FastAPI(
    title="Flood Early Warning API",
    description="Backend untuk menerima dan memproses data sensor mitigasi banjir",
    version="1.0.0"
)

def calculate_alert_level(water_level: float, rainfall: float) -> str:
    if water_level > 250 or rainfall > 100:
        return "Bahaya"
    elif 150 <= water_level <= 250 or 50 <= rainfall <= 100:
        return "Waspada"
    else:
        return "Aman"

@app.get("/")
def read_root():
    return {"message": "Sistem Backend Mitigasi Banjir Aktif"}

@app.post("/api/v1/telemetry", response_model=ResponseMessage)
def receive_telemetry(data: TelemetryInput):
    try:
        alert_status = calculate_alert_level(data.water_level_cm, data.rainfall_mm)
        
        print(f"[{datetime.now()}] Menyimpan data dari Sensor {data.sensor_id} ke database...")
        if alert_status != "Aman":
            print(f"[{datetime.now()}] Memicu ALARM WARNING: Status {alert_status}!")
        
        return ResponseMessage(
            status="success",
            alert_level=alert_status,
            message="Data berhasil diproses dan disimpan"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))