# 🌊 Flood Early Warning System Backend

A robust, RESTful backend service designed to ingest, process, and store telemetry data from IoT sensors for flood mitigation. Built with Python, FastAPI, and PostgreSQL.

This project demonstrates the implementation of clean architecture, data validation, and relational database management to handle time-series IoT data.

## 🚀 Features
- **Real-time Data Ingestion:** Accepts telemetry payload (water level, rainfall) from remote IoT sensors.
- **Automated Threshold Analysis:** Automatically calculates alert levels (`Aman`, `Waspada`, `Bahaya`) based on meteorological thresholds.
- **Alert History Retrieval:** Provides an endpoint to fetch recent triggered alerts for frontend dashboard integration.
- **Persistent Storage:** Securely logs all sensor data and triggered alerts in a relational PostgreSQL database.
- **Interactive API Docs:** Auto-generated Swagger UI for easy testing and API exploration.

## 🛠️ Tech Stack
- **Backend Framework:** Python 3.10+, FastAPI, Uvicorn
- **Database & ORM:** PostgreSQL, `psycopg2`
- **Data Validation:** Pydantic

## 📁 Project Structure
```text
flood-warning-backend/
├── app/
│   ├── core/
│   │   └── database.py       # PostgreSQL connection setup
│   ├── models/
│   │   └── schemas.py        # Pydantic models for request/response validation
│   └── main.py               # FastAPI application instances and routers
├── db/
│   └── init.sql              # DDL scripts for database schema
├── .env.example              # Environment variables template
├── .gitignore
├── requirements.txt          # Python dependencies
└── README.md
```

## 🗄️ Database Schema
The system utilizes three main tables to maintain data integrity:
1. `sensors`: Stores IoT device metadata (ID, name, coordinates).
2. `telemetry_logs`: Stores time-series data of water levels and rainfall.
3. `alert_history`: Logs the history of hazard statuses triggered by the system.

## 💻 Running Locally

### 1. Prerequisites
Ensure you have the following installed on your local machine (Ubuntu/Linux recommended):
- Python 3.8 or higher
- PostgreSQL

### 2. Database Setup
Log into your PostgreSQL instance and run the schema creation script.

```bash
# Enter PostgreSQL prompt
sudo -u postgres psql

# Run the provided SQL script to build the schema
\i db/init.sql
```

### 3. Environment Variables
Create a `.env` file in the root directory and configure your database credentials:

```env
DB_HOST=127.0.0.1
DB_NAME=flood_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

### 4. Install Dependencies & Run
Set up your virtual environment and run the server:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app.main:app --reload
```
## 📡 API Reference
Once the server is running, you can access the interactive Swagger UI documentation at: `http://127.0.0.1:8000/docs`

### 1. Submit Telemetry Data
- **Endpoint:** `POST /api/v1/telemetry`
- **Description:** Receives data from IoT sensors and calculates the alert level.
- **Request Body (JSON):**
  ```json
  {
    "sensor_id": 1,
    "water_level_cm": 275.5,
    "rainfall_mm": 120.0
  }
  ```

- **Success Response (200 OK):**
  ```json
  {
    "status": "success",
    "alert_level": "Bahaya",
    "message": "Data berhasil diproses dan disimpan ke database"
  }
  ```

### 2. Get Alert History
- **Endpoint:** `GET /api/v1/alerts`
- **Description:** Retrieves the 10 most recent triggered alerts for dashboard monitoring.
- **Success Response (200 OK):**
  ```json
  {
    "status": "success",
    "data": [
      {
        "id": 1,
        "sensor_id": 1,
        "alert_level": "Bahaya",
        "triggered_at": "2026-04-27T16:00:00"
      }
    ]
  }
  ```

## 👤 Author
**Hadryan Rizky Dimas Saputra** | Informatics Engineering Student ITS

GitHub: [@Tjoyager](https://github.com/Tjoyager)