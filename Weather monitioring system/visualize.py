import matplotlib.pyplot as plt
import sqlite3

def visualize_daily_summary(date):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather WHERE timestamp LIKE ?", (f'{date}%',))
    data = cursor.fetchall()
    conn.close()
    
    timestamps = [d[4] for d in data]
    temps = [d[2] for d in data]
    
    plt.plot(timestamps, temps)
    plt.xlabel('Time')
    plt.ylabel('Temperature (Celsius)')
    plt.title(f'Temperature on {date}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
