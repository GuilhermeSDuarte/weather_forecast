import requests

API_KEY = "f785813693eb1ea0af7a78fb3ce3023a"
city_name = "São Paulo"
link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

requisicao = requests.get(link)

requisicao_dic = requisicao.json()

description = requisicao_dic['weather'][0]['description']
temperature = requisicao_dic['main']['temp'] - 273.15

print(description, temperature)
