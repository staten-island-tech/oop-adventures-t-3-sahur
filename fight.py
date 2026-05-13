""" import random
from Heros import Hero
from Monsters import enemies_list
from Monsters import Enemy

Bob = Hero("Bob", 0, 100, 1, 100, 10, 5, {"title": "Iron Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
Fight = random.choice(enemies_list)
Option = input("What would you like to do? Fight or rest: ")
if Option == "rest":
    Bob.hp += 10
    print(f"Bob is well rested. Hp is now {Bob.hp}")
elif Option == "fight":
    print("Battle Start!")
    Fight.show_enemy()
    print("What action do you take:")
    print("1: Attack")
    print("2: Slash")
    choice = input("Pick 1 or 2: ")

    if choice == "1":
        print(f"Bob attacks {Fight.name}")
        Fight.hp -= Bob.atk
    elif choice == "2":
        print("Bob slashes")     
    else:
        print("Invalid choice")
 """

import random
from Heros import Hero
from Monsters import Enemy
from Monsters import enemies_list
Gavin = Hero("Gavin", 0, 1, 100, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
Gavin.show_status
Fight = random.choice(enemies_list)
Option = input("Pick a choice. 1. Fight 2. Rest")
if Option == "2":
    Gavin.hp += 10
    print(f"Gavin is now well rested. Hp is now {Gavin.hp}")
elif Option == "1":
   
    print(f"Gavin encounters a {Fight.name}!")
    Fight.show_enemy()
    print("What action would you like to do:")
    print("1. Attack")
    print("2. Slash")
    choice = input("Pick 1 or 2:")
    if choice == "1":
        print(f"Gavin attacks {Fight.name}!")
    Fight.hp -= Gavin.atk
    print(f"{Fight.name}'s hp is now {Fight.hp}")
    if choice == "2":
     print(f"Gavin slashes {Fight.name}!")
    slash_dmg = Gavin.atk + 3
    Fight.hp -= slash_dmg
    print(f"{Fight.name}'s hp is now {Fight.hp}")
else:
        print("Invalid choice")
