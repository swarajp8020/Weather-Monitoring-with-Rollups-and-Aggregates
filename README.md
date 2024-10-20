
# Real-Time Weather Data Processing System

## Overview
This application retrieves real-time weather data from the OpenWeatherMap API, processes it to monitor weather conditions across Indian metros (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad), and provides daily summaries and alerts based on user-configurable thresholds. It uses rollups and aggregates to calculate daily averages, maximum and minimum temperatures, and identifies the dominant weather condition.

## Features
- **Real-time weather data retrieval** from OpenWeatherMap API at configurable intervals.
- **Temperature conversion** from Kelvin to Celsius (with option for Fahrenheit based on user preference).
- **Daily weather summaries** with average, max, min temperatures and dominant weather condition.
- **User-configurable alerts** for threshold breaches (e.g., temperature > 35°C).
- **Persistent storage** of weather data in a database.
- **Visualization** of daily summaries, historical trends, and alerts.
- (Bonus) Additional weather parameters like humidity and wind speed.

## Requirements
- Python 3.8+
- Docker (for running containers such as web server, database)
- OpenWeatherMap API key (you can sign up for a free key at [OpenWeatherMap](https://openweathermap.org/))
- Dependencies listed in `requirements.txt`

## Dependencies
The following dependencies are required to run the application:
- `requests`: For making API calls to OpenWeatherMap.
- `pandas`: For data processing and rollups.
- `sqlalchemy`: For database interaction (can be set up with SQLite/PostgreSQL).
- `matplotlib` or `plotly`: For visualizations.
- `flask`: (optional) For building a web interface to display visualizations.
- `smtplib` or `twilio`: (optional) For sending alerts via email/SMS.

### Installing Dependencies
Run the following command to install all dependencies:
```bash
pip install -r requirements.txt
```

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/weather-monitoring-system.git
cd weather-monitoring-system
```

### 2. API Key Configuration
1. Sign up at [OpenWeatherMap](https://openweathermap.org/) and get your API key.
2. Add the key to a `.env` file or set it as an environment variable.

Example `.env` file:
```
API_KEY=your_openweathermap_api_key
```

### 3. Set up Database (Docker)
If you're using Docker to set up the database (e.g., PostgreSQL):
1. Run the following command to start the database container:
```bash
docker run --name weather-db -e POSTGRES_PASSWORD=yourpassword -d postgres
```
2. Update the `config.py` file with your database credentials.

### 4. Run the Application
1. Run the data processing system:
```bash
python main.py
```
2. The system will start pulling data from the OpenWeatherMap API at the configured interval (default: 5 minutes).

### 5. Running the Web Interface
If you want to run the web interface for visualization:
```bash
python app.py
```
The web app will be available at `http://localhost:5000`.

### 6. Docker
You can also run the application using Docker. The provided Dockerfile creates a containerized environment to run the system.
1. Build the Docker image:
```bash
docker build -t weather-app .
```
2. Run the container:
```bash
docker run -d -p 5000:5000 weather-app
```

## Rollups and Aggregates
### Daily Weather Summary
- **Average temperature**: Calculated by averaging all temperature updates for the day.
- **Maximum/Minimum temperature**: Based on the highest/lowest recorded temperature for the day.
- **Dominant weather condition**: The most frequent weather condition (e.g., Clear, Rain).

### Alerting Thresholds
- User-configurable thresholds can be set for temperature (e.g., alert if temperature exceeds 35°C).
- Alerts can be sent via console or through email notifications when thresholds are breached.

## Test Cases
1. **System Setup**:
    - Ensure the system starts and successfully connects to the OpenWeatherMap API with a valid API key.
2. **Data Retrieval**:
    - Test the system retrieves weather data at configurable intervals and parses it correctly.
3. **Temperature Conversion**:
    - Verify temperature conversion from Kelvin to Celsius/Fahrenheit.
4. **Daily Weather Summary**:
    - Simulate weather updates for several days and verify the accuracy of daily summaries.
5. **Alerting Thresholds**:
    - Configure user thresholds and simulate weather conditions exceeding the thresholds. Check if alerts are triggered correctly.

### Running Unit Tests
You can run the test cases using the `unittest` framework. To run the tests:
```bash
python -m unittest discover tests
```

## Additional Features
- **Humidity and Wind Speed**: Extended support for monitoring additional parameters such as humidity and wind speed.
- **Weather Forecasting**: Retrieve and summarize weather forecasts for the upcoming days.

## Contributing
Feel free to fork this repository, create a new branch, and submit a pull request with any new features or improvements.

---
