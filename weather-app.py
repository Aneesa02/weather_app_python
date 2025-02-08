import requests

API_KEY = 'a71b7f9fc32959b2b670fb76ffada744'  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Ask the user for the city name
city = input("Enter the city name: ")

# Create the full URL for the API request
url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

# Send the request to the API using requests.get()
response = requests.get(url)

# Print the status code for debugging
print(f"Status Code: {response.status_code}")

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert the response into a Python dictionary
    main_data = data['main']  # Extract main weather data like temperature, pressure, etc.
    weather_data = data['weather'][0]  # Extract the weather description

    # Extract information and display it
    temperature = main_data['temp']
    pressure = main_data['pressure']
    humidity = main_data['humidity']
    weather_description = weather_data['description']

    print(f"\nWeather in {city.capitalize()}:\n")
    print(f"Temperature: {temperature}°C")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description.capitalize()}")
else:
    print("City not found! Please check the name and try again.")
    # Optionally print the API response content for debugging
    print(f"Response Content: {response.text}")

