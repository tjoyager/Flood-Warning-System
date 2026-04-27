CREATE TABLE sensors (
    id SERIAL PRIMARY KEY,
    sensor_name VARCHAR(100) NOT NULL,
    location_lat DECIMAL(10, 8),
    location_lon DECIMAL(11, 8),
    installed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE telemetry_logs (
    id SERIAL PRIMARY KEY,
    sensor_id INTEGER REFERENCES sensors(id),
    water_level_cm DECIMAL(5, 2),
    rainfall_mm DECIMAL(5, 2),
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE alert_history (
    id SERIAL PRIMARY KEY,
    sensor_id INTEGER REFERENCES sensors(id),
    alert_level VARCHAR(20) NOT NULL, -- 'Aman', 'Waspada', 'Bahaya'
    triggered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);