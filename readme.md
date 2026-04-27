# 🌊 Flood Early Warning System Backend

A robust, RESTful backend service designed to ingest, process, and store telemetry data from IoT sensors for flood mitigation. Built with Python, FastAPI, and PostgreSQL.

## 🚀 Features
- **Real-time Data Ingestion:** Accepts telemetry payload (water level, rainfall) from remote IoT sensors.
- **Automated Threshold Analysis:** Automatically calculates alert levels (Aman, Waspada, Bahaya) based on meteorological thresholds.
- **Persistent Storage:** Securely logs all sensor data and triggered alerts in a relational PostgreSQL database.
- **Interactive API Docs:** Auto-generated Swagger UI for easy testing and integration.

## 🛠️ Tech Stack
- **Backend:** Python 3, FastAPI, Uvicorn
- **Database:** PostgreSQL, psycopg2
- **Data Validation:** Pydantic

## 💻 Running Locally

### 1. Database Setup
Ensure PostgreSQL is installed. Run the schema creation script:
```bash
psql -U postgres -f db/init.sql