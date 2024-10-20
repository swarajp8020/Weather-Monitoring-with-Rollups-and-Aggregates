# Weather Monitoring System

## Overview

This system retrieves real-time weather data from the OpenWeatherMap API for various metros in India and provides daily summaries and alerting mechanisms based on configurable thresholds.

### Features

- Real-time weather data processing
- Daily summaries (average, min, max temperature, dominant weather condition)
- Configurable alerts for temperature thresholds
- Simple visualization of weather trends

### Requirements

- Python 3.8+
- Flask
- SQLite
- Docker (for running the services)

### Setup Instructions

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set your OpenWeatherMap API key in the `config.py` file
4. Run the application: `python app.py`
5. (Optional) Use `docker-compose up` to run the app with Docker

### Endpoints

- `/weather`: Retrieves and processes weather data
- `/summary`: Returns daily summary for a given date
- `/alerts`: Configures temperature thresholds for alerting

### Tests

To run tests:
