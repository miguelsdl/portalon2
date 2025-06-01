import os
import hashlib
from django.core.management.base import BaseCommand
from django.core.files import File
from games.models.game import Game
from games.models.game_platform import GamePlatform


def calculate_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

class Command(BaseCommand):
    help = 'Insert MAME games from a directory of .zip files'

    def add_arguments(self, parser):
        parser.add_argument('roms_path', type=str, help='Path to the directory containing .zip files')

    def handle(self, *args, **options):
        roms_path = options['roms_path']
        if not os.path.isdir(roms_path):
            self.stderr.write(self.style.ERROR(f'Path not found: {roms_path}'))
            return

        platform, _ = GamePlatform.objects.get_or_create(name='mame')
        count = 0

        for filename in os.listdir(roms_path):
            if filename.lower().endswith('.zip'):
                title = os.path.splitext(filename)[0]
                file_path = os.path.join(roms_path, filename)
                with open(file_path, 'rb') as f:
                    game = Game(
                        title=title,
                        description=f'MAME ROM: {filename}',
                        platform=platform,
                        checksum=calculate_checksum(file_path)
                    )
                    game.rom.save(filename, File(f), save=True)
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Inserted {count} MAME games.'))