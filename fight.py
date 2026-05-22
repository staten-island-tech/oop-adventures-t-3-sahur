import random
from Heros import Hero
from Monsters import enemies_list
import Monsters

Gavin = Hero("Gavin", 0, 100, 1, 100, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
Fight = random.choice(enemies_list)
round = 0
Option = input("Pick a choice: 1. Fight 2. Rest")
if Option == "2":
    Gavin.hp += 10
    print(f"Gavin is well rested. Hp is now {Gavin.hp}")
elif Option == "1":
    print(f"Gavin encounters a {Fight.name}")
    print("----------------------------------------------------------------------------")
    Fight.show_enemy()
    print(f"Round {round}")
    while Gavin.hp >= 0 or Fight.hp >= 0:
        print("----------------------------------------------------------------------------")
        print("What action do you like to do:")
        print("1: Attack")
        print("2: Slash")
        choice = input("Pick 1 or 2: ")
        print("----------------------------------------------------------------------------")
        if choice == "1":
            print(f"Gavin attacks {Fight.name}")
            print("----------------------------------------------------------------------------")
            atk_dmg = Gavin.atk + 2
            Fight.hp -= atk_dmg
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            print(f"{Gavin.name}'s hp is now {Gavin.hp}")
            print(f"{Gavin.name}'s mp is now {Gavin.mp}")
            round += 1
            Gavin.mp += 1
            print(f"Round {round}")
        elif choice == "2": 
            print(f"Gavin slashes {Fight.name}")
            print("----------------------------------------------------------------------------")
            Gavin.mp -= 3
            slash_dmg = Gavin.atk + 5
            Fight.hp -= slash_dmg
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            print(f"{Gavin.name}'s hp is now {Gavin.hp}")
            print(f"{Gavin.name}'s mp is now {Gavin.mp}")
            round += 1
            Gavin.mp += 1
            print(f"Round {round}")
        else:
            print("Invalid choice")   
            Gavin.show_status()
            round += 1
            print(f"Round {round}")
        Gavin.hp -= Fight.atk 
        if Fight.hp <= 0:
            print("----------------------------------------------------------------------------")
            print("The battle is over")
            print("----------------------------------------------------------------------------")
            print(f"Gavin gained {Fight.exp_given} experience.")
            Gavin.exp += Fight.exp_given
            Gavin.show_status()
            break
        if Gavin.hp <= 0:
            print("----------------------------------------------------------------------------")
            print(f"{Gavin.name} has fallen")
            print("----------------------------------------------------------------------------")
            break