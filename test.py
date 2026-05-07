from classes import Hero
from Monsters import enemies_list
import random


Bob = Hero("Bob", 0, 1, 100, 10, 5, {"title": "Iron Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
Bob.show_status()

Fight = random.choice(enemies_list)
print("Battle Start!")
Fight.show_enemy()