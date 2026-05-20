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
        print("What action do you like to do:")
        print("1: Attack")
        print("2: Slash")
        choice = input("Pick 1 or 2: ")
        if choice == "1":
            print(f"Gavin attacks {Fight.name}")
            atk_dmg = Gavin.atk + 2
            Fight.hp -= atk_dmg
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            round += 1
            Gavin.mp += 1
        elif choice == "2": 
            print(f"Gavin slashes {Fight.name}")
            Gavin.mp -= 3
            slash_dmg = Gavin.atk + 5
            Fight.hp -= slash_dmg
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            round += 1
            Gavin.mp += 1
        if Fight.hp <= 0:
            print("The battle is over")
            Gavin.exp += 15
            Gavin.show_status()
            break
        if Gavin.hp <= 0:
            print(f"{Gavin.name} has fallen")
            break
        else:
            print("Invalid choice")
else:
    print("Invalid choice")
    Gavin.show_status()
    Gavin.hp -= 10