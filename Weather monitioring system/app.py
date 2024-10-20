from flask import Flask, request, jsonify
from weather import get_weather_data, process_weather_data, summarize_daily_weather
from alerts import check_thresholds, alert
from database import init_db, store_weather_data, get_daily_summary

app = Flask(__name__)

# Initialize database
init_db()

@app.route('/weather', methods=['GET'])
def get_weather():
    # Retrieve and process weather data
    weather_data = get_weather_data()
    processed_data = process_weather_data(weather_data)
    store_weather_data(processed_data)
    
    return jsonify(processed_data), 200

@app.route('/summary', methods=['GET'])
def daily_summary():
    date = request.args.get('date')
    summary = get_daily_summary(date)
    
    return jsonify(summary), 200

@app.route('/alerts', methods=['POST'])
def set_alert():
    threshold = request.json.get('threshold')
    alert_type = request.json.get('alert_type')  # e.g., 'temp'
    alert(threshold, alert_type)
    
    return jsonify({"message": "Alert set"}), 200

if __name__ == '__main__':
    app.run(debug=True)
