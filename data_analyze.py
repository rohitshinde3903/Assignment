import sqlite3
import pandas as pd

def fetch_data_from_db():
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query("SELECT * FROM weather", conn)
    conn.close()
    return df

def analyze_data(df):
    print("Basic Statistical Analysis:")
    print(df.describe())


if __name__ == '__main__':
    df = fetch_data_from_db()
    analyze_data(df)

