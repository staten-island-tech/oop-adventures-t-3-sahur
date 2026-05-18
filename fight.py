import random
from Heros import Hero
from Monsters import enemies_list

Gavin = Hero("Gavin", 0, 100, 1, 100, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
Fight = random.choice(enemies_list)
round = 0
Option = input("Pick a choice: 1. Fight 2. Rest")
if Option == "2":
    Gavin.hp += 10
    print(f"Gavin is well rested. Hp is now {Gavin.hp}")
elif Option == "1":
    print(f"Gavin encounters a {Fight.name}")
    Fight.show_enemy()
    print(f"Round {round}")
    while Gavin.hp >= 0 or Fight.hp >= 0:
        if Gavin.hp <= 0 or Fight.hp <= 0:
            print("The battle is over")
            Gavin.exp += 15
            break
else:
    print("Invalid choice")
