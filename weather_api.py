import requests

Api_key = "Your_API_key"
city = input("Enter the city: ")
url = f"http://api.weatherapi.com/v1/current.json?key={Api_key}&q={city}&aqi=no"

response = requests.get(url)
data = response.json()

if (response.status_code==200):
    location = data['location']['name']
    country = data['location']['country']
    temp_c = data['current']['temp_c']
    condition = data['current']['condition']['text']
    humidity = data['current']['humidity']
    wind_kph = data['current']['wind_kph']

    print(f"Weather in {location}, {country}:")
    print(f"Temperature: {temp_c}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_kph} kph")

else: 
    print("Error", data.get("message","Unable to fetch weather!"))
