# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

## Overview

This project is a real-time data processing system designed to retrieve and process weather data from the OpenWeatherMap API. It provides summarized weather insights by calculating daily weather aggregates such as average temperature, maximum temperature, minimum temperature, and dominant weather condition. The system also includes configurable alert thresholds and visualizations to monitor weather conditions in major Indian metros.

---

## Features

- **Real-time Data Retrieval**: Continuously fetch weather data from the OpenWeatherMap API at a configurable interval (e.g., every 5 minutes).
- **Temperature Conversion**: Automatically converts temperature from Kelvin to Celsius (or Fahrenheit) based on user preferences.
- **Daily Weather Summary**: Computes and stores daily aggregates:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition
- **Threshold-based Alerts**: Monitors weather conditions against user-defined thresholds, triggering alerts when conditions are breached.
- **Historical Data**: Stores weather summaries for further analysis.
- **Visualizations**: Displays weather summaries, trends, and triggered alerts.

---

## Prerequisites

- **OpenWeatherMap API Key**: Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your API key.
- **Java 11+**: The system is built using Java.
- **Maven**: For building the project and managing dependencies.
- **Database**: The system supports PostgreSQL (configured via Docker).
- **Docker**: For setting up the database and any additional services.
- **Git**: For cloning the project.

---

## Project Structure

```
.
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com.weather.monitor
│   │   │       └── Main.java
│   │   │       └── WeatherProcessor.java
│   │   │       └── AlertService.java
│   │   ├── resources
│   └── test
│       └── java
│           └── com.weather.monitor
├── README.md
├── pom.xml
└── Dockerfile
```

---

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weather-monitor.git
cd weather-monitor
```

### 2. Set up the Environment Variables
Create a `.env` file in the root directory and add the following:
```env
API_KEY=your_openweathermap_api_key
DB_URL=jdbc:postgresql://localhost:5432/weatherdb
DB_USERNAME=your_db_username
DB_PASSWORD=your_db_password
ALERT_EMAIL=alert_email@example.com
```

### 3. Build the Project
Use Maven to build the project:
```bash
mvn clean install
```

### 4. Set up the PostgreSQL Database (Docker)
The application uses PostgreSQL for storing weather summaries. You can run PostgreSQL using Docker:
```bash
docker run --name weatherdb -e POSTGRES_USER=your_db_username -e POSTGRES_PASSWORD=your_db_password -d -p 5432:5432 postgres
```

### 5. Run the Application
Run the application using Maven:
```bash
mvn spring-boot:run
```

Alternatively, you can run the jar:
```bash
java -jar target/weather-monitor-1.0.jar
```

---

## Configurable Settings

You can modify the following settings in the `application.properties` file:

```properties
# OpenWeatherMap API Config
api.key=${API_KEY}
api.url=https://api.openweathermap.org/data/2.5/weather
api.cities=Delhi,Mumbai,Chennai,Bangalore,Kolkata,Hyderabad

# Data Fetch Interval (in minutes)
fetch.interval=5

# Temperature Threshold for Alerts
alert.temp.threshold=35

# PostgreSQL Database Config
spring.datasource.url=${DB_URL}
spring.datasource.username=${DB_USERNAME}
spring.datasource.password=${DB_PASSWORD}
```

---

## Alerts and Notification System

- **Alerting Threshold**: Users can configure a temperature threshold (e.g., alerts when temperature exceeds 35°C).
- **Triggering Alerts**: When the temperature exceeds the threshold for two consecutive updates, an alert is triggered.
- **Alert Notifications**: Alerts can be displayed on the console or sent via email (configurable).

---

## Rollups and Aggregates

- **Daily Weather Summary**: 
  - **Average Temperature**: Average of all temperature readings during the day.
  - **Max/Min Temperature**: Highest and lowest temperature readings.
  - **Dominant Weather Condition**: Calculated based on the most frequent `main` weather condition reported.

---

## Test Cases

### 1. **System Setup**
- Verify that the system starts and connects to the OpenWeatherMap API using a valid API key.

### 2. **Data Retrieval**
- Simulate API calls at the configured interval and verify the correct parsing of weather data.

### 3. **Temperature Conversion**
- Test the conversion of temperature from Kelvin to Celsius or Fahrenheit based on user preferences.

### 4. **Daily Weather Summary**
- Simulate weather updates for several days and validate that daily summaries are calculated correctly.

### 5. **Alerting Thresholds**
- Configure a temperature threshold, simulate weather data breaching that threshold, and ensure alerts are triggered.

---

## Bonus Features

- **Extended Weather Parameters**: Include additional weather parameters like humidity and wind speed.
- **Forecast Data**: Implement weather forecasts and generate summaries based on predicted conditions.

---

## Dependencies

- Java 11+
- Maven
- PostgreSQL
- OpenWeatherMap API
- Docker (for database setup)

---

## Future Improvements

- Incorporate a more robust notification system with email or SMS alerts.
- Extend support for more cities or weather parameters.
- Add caching mechanisms for API data to optimize network usage.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contributors

- Swaraj Ravindra Purarkar

---

This README should give a clear idea of how to set up, run, and test the weather monitoring system.
