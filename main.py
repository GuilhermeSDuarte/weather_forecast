import requests
import flet as ft
from flet import *
import datetime

api_key = "api_key"
city_name = "São Paulo"
current = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang=pt_br").json()
print(current)
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

    #Função de pesquisa da previsão da cidade.
    def _text():

        text = TextField(width=200,
                         height=38,
                         border="underline",
                         text_align='center',
                         text_size=16,
                         content_padding=0,
                         )

        return text

    #Função para pegar os dados do tempo.
    def current_temp():
        temperature = int(current['main']['temp'] - 273.15)
        weather = current['weather'][0]['main']
        description = current['weather'][0]['description']
        wind = int(current['wind']['speed'])
        humidity = int(current['main']['humidity'])
        feels = int(current['main']['feels_like'] - 273.15)
        image = current['weather'][0]['icon']

        return [temperature, weather, description, wind, humidity, feels, image]

    def current_extra():
        extra_info = []

        extra = [
            [
                int(current['visibility']/1000), "km", "Visibilidade", "./img/botao-de-visibilidade.png"
            ],
            [
                round(current['main']['pressure'] * 0.03, 2), "mbar", "Pressão", "./img/pressao.png"
            ],
            [
                datetime.datetime.fromtimestamp(current['sys']['sunset']).strftime("%I:%M %p"), "", "Sunset", "./img/por-do-sol.png"
            ],
            [
                datetime.datetime.fromtimestamp(current['sys']['sunrise']).strftime("%I:%M %p"), "", "Sunrise", "./img/nascer-do-sol.png"
            ],
        ]

        for data in extra:
            extra_info.append(
                Container(
                    bgcolor="white10",
                    border_radius=12,
                    alignment=alignment.center,
                    content=Column(
                        alignment="center",
                        horizontal_alignment="center",
                        spacing=25,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                content=Image(
                                    src=data[3],
                                    color="white",
                                ),
                                width=32,
                                height=32,
                            ),
                            Container(
                                content=Column(
                                    alignment="center",
                                    horizontal_alignment="center",
                                    spacing=0,
                                    controls=[
                                        Text(
                                            str(
                                                data[0]
                                            ) + " " + data[1], size=14,
                                        ),
                                        Text(
                                            data[2],
                                            size=11,
                                            color="white54"
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                )
            )

        return extra_info

    #Tela onde vai mostrar a previsão do dia.
    def _top():

        today = current_temp()

        today_extra = GridView(
            padding=10,
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5,
        )

        for info in current_extra():
            today_extra.controls.append(info)

        top = Container(
            padding=10,
            width=310,
            height=660 * 0.40,
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
                spacing=20,
                controls=[
                    Row(
                        alignment='center',
                        controls=[Text("São Paulo", size=16)]
                    ),
                    Row(
                        alignment='center',
                        spacing=30,
                        controls=[
                            Column(controls=[Container(
                                width=90,
                                height=90,
                                image_src=f"./img/{today[6]}@2x.png",
                            )]),
                            Column(
                                spacing=5,
                                horizontal_alignment='center',
                                controls=[
                                    Text(
                                        "Hoje",
                                        size=12,
                                    ),
                                    Row(
                                        vertical_alignment="start",
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Text(
                                                    today[0],
                                                    size=52,
                                                ),
                                            ),
                                            Container(
                                                content=Text(
                                                    "°C",
                                                    size=28,
                                                )
                                            )
                                        ]
                                    ),
                                    Text(
                                        today[1] + " - Overcast",
                                        size=10,
                                        color="white",
                                        text_align="center",
                                    )
                                ]
                            )
                        ]
                    ),
                    Divider(height=8, thickness=1, color="white"),
                    Row(
                        alignment="spaceAround",
                        controls=[
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(src="./img/thermometer.png", color="white"),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(today[5]) + "°",
                                            size=11,
                                        )
                                    ]
                                )
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(src="./img/wind.png", color="white"),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(today[3]) + "Km/h",
                                            size=11,
                                        )
                                    ]
                                )
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(src="./img/humidity.png", color="white"),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(today[4]) + "%",
                                            size=11,
                                        ),
                                    ],
                                )
                            ),
                        ],
                    ),
                    today_extra,
                ],
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

ft.app(target=main)
