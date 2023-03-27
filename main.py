import requests
from pprint import pprint
# aqui voce ira precisar de uma API-KEY pra inserir entre as aspas, como eu não possuo usei um exemplo aleatorio 
API_Key = 'cb77145ac79a4e8e2205c0ce66ff633'

city = input("Enter city: ")
# na base_url voce irar inserir o link da sua api key
base_url = "http://api.weatherapi.com/v1/current.json?key=&q=são paulo&aqi=no"+API_Key+"&q="+city

weather_date = requests.get(base_url).json()

pprint(weather_date)