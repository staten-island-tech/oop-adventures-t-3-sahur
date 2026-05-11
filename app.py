import random
from fight import Fight
from Heros import Hero
from Monsters import enemies_list


Bob = Hero("Bob", 0, 100, 1, 100, 10, 5, {"title": "Iron Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})

Option = input("What would you like to do? Fight or rest: ")