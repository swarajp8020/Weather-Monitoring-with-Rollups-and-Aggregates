API_KEY = 'your_openweathermap_api_key'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

# User preferences
TEMP_UNIT = 'Celsius'  # Options: 'Celsius', 'Fahrenheit'

# Alert thresholds
ALERT_THRESHOLD = {
    'temp': 35  # Default temperature threshold
}

# Email configuration for alerting
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'port': 587,
    'email': 'your_email@gmail.com',
    'password': 'your_email_password',
    'recipient': 'alert_recipient@example.com'
}
