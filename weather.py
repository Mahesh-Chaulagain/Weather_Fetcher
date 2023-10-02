from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve the value of the environment variable
API_KEY = os.getenv("API_KEY")  #get API_KEY from .env file
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" #url for API

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"    #append api key and city to base url
response = requests.get(request_url)    #use get request to retrieve information

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']   #access weather key from the json file
    temperature = round(data["main"]["temp"] - 273.15,2) #access temp from the json
    print("weather:",weather)
    print("temperature",temperature,"celsius")
else:
    print("an error occured")
