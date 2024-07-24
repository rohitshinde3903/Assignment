import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from data_analyze import fetch_data_from_db

def visualize_data(df):
    plt.figure(figsize=(14, 10))

    # Temperature Trends - Line Plot
    plt.subplot(3, 2, 1)
    sns.lineplot(data=df, x='timestamp', y='temperature', marker='o', color='blue')
    plt.title('Temperature Trends')
    plt.xticks(rotation=45)
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')

    # Humidity Trends - Bar Plot
    plt.subplot(3, 2, 2)
    sns.barplot(data=df, x='timestamp', y='humidity', color='green')
    plt.title('Humidity Trends')
    plt.xticks(rotation=45)
    plt.xlabel('Timestamp')
    plt.ylabel('Humidity (%)')

    # Wind Speed Trends - Scatter Plot
    plt.subplot(3, 2, 3)
    sns.scatterplot(data=df, x='timestamp', y='wind_speed', color='red')
    plt.title('Wind Speed Trends')
    plt.xticks(rotation=45)
    plt.xlabel('Timestamp')
    plt.ylabel('Wind Speed (m/s)')

    # Temperature Distribution - Histogram
    plt.subplot(3, 2, 4)
    sns.histplot(df['temperature'], bins=20, color='purple')
    plt.title('Temperature Distribution')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')

    # Humidity Distribution - KDE Plot
    plt.subplot(3, 2, 5)
    sns.kdeplot(df['humidity'], color='orange')
    plt.title('Humidity Distribution')
    plt.xlabel('Humidity (%)')
    plt.ylabel('Density')

    # Wind Speed Distribution - Box Plot
    plt.subplot(3, 2, 6)
    sns.boxplot(x=df['wind_speed'], color='cyan')
    plt.title('Wind Speed Distribution')
    plt.xlabel('Wind Speed (m/s)')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    df = fetch_data_from_db()
    visualize_data(df)
