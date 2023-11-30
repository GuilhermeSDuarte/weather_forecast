import requests


def main():

    city_name = input("Informe a cidade:")

    if city_name:
        menu(city_name)
    else:
        print(city_name)


def menu(city_name):

    api_key = "f785813693eb1ea0af7a78fb3ce3023a"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=pt_br"
    response = requests.get(link)
    response_dic = response.json()

    opcao = int(input(f"""===Menu===
    1 - Previsão do tempo atual
    2 - Previsão do tempo semanal
    3 - Previsão do tempo de um dia em especifico
    4 - Dados adicionais de previsão
    0 - Sair
    Digite o número do que deseja saber:
"""))

    if opcao == 1:
        description = response_dic['weather'][0]['description']
        temperature = response_dic['main']['temp'] - 273.15

        print("Temperatura atual da cidade de", city_name)
        print("Tempo atual:", description)
        print("Temperatura atual:", temperature)
    if opcao == 2:
        pass
    if opcao == 3:
        pass
    if opcao == 4:
        pass
    if opcao == 0:
        pass

main()