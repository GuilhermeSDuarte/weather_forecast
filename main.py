import requests
import flet as ft
from flet import *


def main(page: ft.Page):

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    #Função para expandir a tela de previsão do dia.
    def _expand(e):
        if e.data == "true":
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 660 * 0.4
            _c.content.controls[0].update()

    def _text():

        text = TextField(width=250,
                         border_radius=35,
                         text_align='center',
                         text_size=15
                         )

        return text

    #Tela onde vai mostrar a previsão do dia.
    def _top():

        top = Container(
            padding=10,
            width=310,
            height=660 * 0.44,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=350,
                                        curve="decelerate"),
            on_hover=lambda e: _expand(e),
            content=Column(
                alignment='start',
                spacing=10,
                controls=[
                    Row(
                        alignment='center',
                        controls=[_text()]
                    )
                ]
            ),
        )

        return top

    #Tela principal do App.
    _c = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=Stack(
            width=210,
            height=550,
            controls=[_top()]
        ),

    )

    page.add(_c)

    """city_name = input("Informe a cidade:")
    api_key = "f785813693eb1ea0af7a78fb3ce3023a"
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=pt_br").json()

    description = response['weather'][0]['description']
    temperature = response['main']['temp'] - 273.15

    print("Temperatura atual da cidade de", city_name)
    print("Tempo atual:", description)
    print("Temperatura atual:", temperature)"""


ft.app(target=main)
