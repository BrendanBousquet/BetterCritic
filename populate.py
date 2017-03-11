import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'criticV1.settings')
import django
django.setup()
from critic.models import Game

def populate():
    games = [
        ["Kingdom Hearts 3",
         10
        ],
        ["Kingdom Hearts 2",
         9
         ]
    ]

    for name, score in games:
        print(name)
        g = add_game(name, score)

def add_game(name, score):
    test = Game.objects.get_or_create(game_name=name, game_score=score)[0]
    test.save()
    return test

if __name__ == '__main__':
    print("Starting")
    populate()