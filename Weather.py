# *************************************  know the weather **********************************
import requests

# API key for OpenWeatherMap
API_KEY = " your _ API _ KEY "

# base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


# function to get weather data
def get_weather_data(city_name):
    # complete URL for API request
    url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY

    # send request to API and get response
    response = requests.get(url)

    # if request is successful
    if response.status_code == 200:
        # get JSON data from response
        data = response.json()

        # extract relevant data from JSON
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        # convert temperature from Kelvin to Celsius
        temperature = temperature - 273.15

        # format output string
        output = f"Current weather in {city}, {country}: {description} ({temperature:.1f} °C)"

    # if request is unsuccessful
    else:
        output = "Sorry, could not get weather data. Please try again later."

    # return output string
    return output


# main program
if __name__ == "__main__":
    # get city name from user
    city_name = input("Enter city name: ")

    # get weather data for city
    weather_data = get_weather_data(city_name)

    # print weather data
    print(weather_data)