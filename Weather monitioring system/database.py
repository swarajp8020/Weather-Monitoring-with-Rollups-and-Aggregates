import sqlite3

def init_db():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            main TEXT,
            temp REAL,
            feels_like REAL,
            timestamp TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            date TEXT,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_weather_data(data):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    for item in data:
        cursor.execute("INSERT INTO weather (city, main, temp, feels_like, timestamp) VALUES (?, ?, ?, ?, ?)", 
                       (item['city'], item['main'], item['temp'], item['feels_like'], item['timestamp']))
    conn.commit()
    conn.close()

def get_daily_summary(date):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM daily_summary WHERE date=?", (date,))
    summary = cursor.fetchone()
    conn.close()
    return summary
