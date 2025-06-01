from django.core.management.base import BaseCommand
from games.models.game import Game
from games.models.game_category import GameCategory
from games.models.game_platform import GamePlatform

import random

class Command(BaseCommand):
    help = 'Insert 200 mock games'

    def handle(self, *args, **kwargs):
        categories = list(GameCategory.objects.all())
        platforms = list(GamePlatform.objects.all())
        for i in range(200):
            game = Game.objects.create(
                title=f'Mock Game {i+1}',
                description=f'This is a mock description for game {i+1}.',
                category=random.choice(categories) if categories else None,
                platform=random.choice(platforms) if platforms else None,
            )
        self.stdout.write(self.style.SUCCESS('Inserted 200 mock games.'))