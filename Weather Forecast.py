import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace 'your_api_key' with your actual OpenWeatherMap API key
API_KEY = 'your_api_key'  # Make sure to insert your API key here

def fetch_weather_data(city):
    """Fetch weather data from OpenWeatherMap API."""
    url = f'https://openweathermap.org/q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

def visualize_weather_data(data):
    """Visualize temperature and humidity from weather data."""
    # Extract relevant data
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    
    # Prepare data for visualization
    weather_data = {
        'Temperature (°C)': [temperature],
        'Humidity (%)': [humidity]
    }
    
    df = pd.DataFrame(weather_data)

    # Set up the matplotlib figure
    plt.figure(figsize=(10, 5))

    # Create a bar plot for temperature and humidity
    sns.barplot(data=df)
    plt.title(f"Weather in {city}")
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    city = input("Enter city name: ")
    
    # Fetch weather data
    weather_data = fetch_weather_data(city)

    # Check if the request was successful
    if weather_data.get('cod') == 200:
        print(f"Temperature: {weather_data['main']['temp']} °C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Description: {weather_data['weather'][0]['description']}")

        # Visualize the weather data
        visualize_weather_data(weather_data)
    else:
        print("City not found. Please check the city name.")
