import smtplib
from config import ALERT_THRESHOLD, EMAIL_CONFIG

def check_thresholds(weather_data):
    alerts = []
    for data in weather_data:
        if data['temp'] > ALERT_THRESHOLD['temp']:
            alerts.append(f"Temperature alert for {data['city']}: {data['temp']}°C exceeds {ALERT_THRESHOLD['temp']}°C")
    
    return alerts

def alert(threshold, alert_type):
    ALERT_THRESHOLD[alert_type] = threshold
    print(f"Alert set for {alert_type}: {threshold}")

def send_email_alert(alert_message):
    with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['port']) as server:
        server.login(EMAIL_CONFIG['email'], EMAIL_CONFIG['password'])
        server.sendmail(
            EMAIL_CONFIG['email'], 
            EMAIL_CONFIG['recipient'], 
            f"Subject: Weather Alert\n\n{alert_message}"
        )
    print("Alert email sent.")
