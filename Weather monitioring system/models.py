from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define the base for the model classes
Base = declarative_base()

# Create an SQLite engine (you can replace this with another database URL if needed)
engine = create_engine('sqlite:///weather.db', echo=True)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Model for storing weather data
class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    main = Column(String)  # Main weather condition (Rain, Snow, etc.)
    temp = Column(Float)  # Current temperature in Celsius
    feels_like = Column(Float)  # Perceived temperature in Celsius
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __init__(self, city, main, temp, feels_like, timestamp=None):
        self.city = city
        self.main = main
        self.temp = temp
        self.feels_like = feels_like
        self.timestamp = timestamp or datetime.utcnow()

    def __repr__(self):
        return f"<WeatherData(city={self.city}, temp={self.temp}, timestamp={self.timestamp})>"


# Model for storing daily weather summaries
class DailySummary(Base):
    __tablename__ = 'daily_summary'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String)  # Date in format YYYY-MM-DD
    avg_temp = Column(Float)  # Average temperature for the day
    max_temp = Column(Float)  # Maximum temperature for the day
    min_temp = Column(Float)  # Minimum temperature for the day
    dominant_condition = Column(String)  # Dominant weather condition

    def __init__(self, date, avg_temp, max_temp, min_temp, dominant_condition):
        self.date = date
        self.avg_temp = avg_temp
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.dominant_condition = dominant_condition

    def __repr__(self):
        return f"<DailySummary(date={self.date}, avg_temp={self.avg_temp}, dominant_condition={self.dominant_condition})>"


# Function to initialize the database (create tables)
def init_db():
    Base.metadata.create_all(engine)

# Function to add weather data
def add_weather_data(city, main, temp, feels_like, timestamp=None):
    weather = WeatherData(city=city, main=main, temp=temp, feels_like=feels_like, timestamp=timestamp)
    session.add(weather)
    session.commit()

# Function to add daily summary
def add_daily_summary(date, avg_temp, max_temp, min_temp, dominant_condition):
    summary = DailySummary(date=date, avg_temp=avg_temp, max_temp=max_temp, min_temp=min_temp, dominant_condition=dominant_condition)
    session.add(summary)
    session.commit()

# Function to fetch weather data by city
def get_weather_data_by_city(city):
    return session.query(WeatherData).filter_by(city=city).all()

# Function to fetch daily summary by date
def get_daily_summary_by_date(date):
    return session.query(DailySummary).filter_by(date=date).first()

# Initialize the database (create tables if they do not exist)
init_db()
