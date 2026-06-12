from fight import rounds
from Heros import Gavin
def weapon(Gavin, rounds):
    if rounds == 100:
        Gavin.inventory = {"title": "Stone Sword", "atk": 5}
    if rounds == 250:
        Gavin.inventory = {"title": "Iron Sword", "atk": 10}
    if rounds == 500:
        Gavin.inventory = {"title": "Diamond Sword", "atk": 20}
    if rounds == 1000:
        Gavin.inventory = {"title": "Netherite Sword", "atk": 40}
