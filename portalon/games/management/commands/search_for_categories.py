import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from games.models.game import Game
from games.models.game_category import GameCategory


import requests


def consultar_phind(pregunta):
    """
    Envía una pregunta a Phind y devuelve la respuesta.

    Args:
        pregunta (str): La pregunta que quieres hacer

    Returns:
        str: La respuesta de Phind
    """
    try:
        # Preparar la solicitud
        url = "https://api.phind.com/v1/chat"
        datos = {
            "question": pregunta
        }

        # Enviar la solicitud
        respuesta = requests.post(url, json=datos)

        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:
            resultado = respuesta.json()
            return resultado.get("answer", "No se obtuvo respuesta")
        else:
            return f"Error en la solicitud: {respuesta.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error de conexión: {str(e)}"

class Command(BaseCommand):
    help = 'Update Game categories by searching the internet'

    def handle(self, *args, **options):
        games = Game.objects.all()
        updated = 0
        for game in games:
            name_category = consultar_phind(f'quiero las categorias de este juego {game.title}')
            print(f'for game: {game.title} - category: {name_category}')
            # if not game.category:
            #
            #     if name_category:
            #         category, _ = GameCategory.objects.get_or_create(name=name_category)
            #         game.category = category
            #         game.save()
            #         updated += 1
            #         self.stdout.write(f'Updated "{game.title}" with category "{name_category}"')
        # self.stdout.write(self.style.SUCCESS(f'Updated {updated} games with categories.'))