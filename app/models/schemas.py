from pydantic import BaseModel, Field

class TelemetryInput(BaseModel):
    sensor_id: int = Field(..., description="ID dari perangkat sensor")
    water_level_cm: float = Field(..., ge=0, description="Ketinggian air dalam cm")
    rainfall_mm: float = Field(..., ge=0, description="Curah hujan dalam mm/jam")

class ResponseMessage(BaseModel):
    status: str
    alert_level: str
    message: str