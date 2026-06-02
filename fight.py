import random
from Heros import Hero
<<<<<<< HEAD
from Enemies import enemies_list
Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 10, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
round = 0
=======
from Monsters import enemies_list

Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 10, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
>>>>>>> 2dbc03c30e4a7ad4c1ed18a625c72e8318dc1506
Fight = random.choice(enemies_list)
round = 0
Option = input("Pick a choice: 1. Fight or 2. Head to inn")
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
            round += 1
            print(f"Round {round}")
            print(f"Gavin attacks {Fight.name}")
            print("----------------------------------------------------------------------------")
            atk_dmg = Gavin.atk + 2
            Fight.hp -= atk_dmg
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            print(f"{Gavin.name}'s hp is now {Gavin.hp}")
            print(f"{Gavin.name}'s mp is now {Gavin.mp}")
            Gavin.mp += 1
        elif choice == "2": 
            round += 1
            print(f"Round {round}")
            print(f"Gavin slashes {Fight.name}")
            print("----------------------------------------------------------------------------")
            Gavin.mp -= 3
            slash_dmg = Gavin.atk + 5
            Fight.hp -= slash_dmg
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            print(f"{Gavin.name}'s hp is now {Gavin.hp}")
            print(f"{Gavin.name}'s mp is now {Gavin.mp}")
            Gavin.mp += 1
        else:
            round += 1
            print(f"Round {round}")
            print("Invalid choice")   
            Gavin.show_status()
        Gavin.hp -= Fight.atk
        if Fight.hp <= 0:
<<<<<<< HEAD
           print("-----------------------------------------------------------------------")
           print("The battle is over")
           print("-----------------------------------------------------------------------")
           Gavin.exp += Fight.exp_given
           Gavin.lvl_up()
           print(f"Gavin gained {Fight.exp_given} experience!")
           print("-----------------------------------------------------------------------")
           Gavin.show_status()
           
=======
            print("----------------------------------------------------------------------------")
            print("The battle is over")
            print("----------------------------------------------------------------------------")
            print(f"Gavin gained {Fight.exp_given} experience.")
            Gavin.exp += Fight.exp_given
            Gavin.lvl_up()
            Gavin.show_status()
>>>>>>> 2dbc03c30e4a7ad4c1ed18a625c72e8318dc1506
        if Gavin.hp <= 0:
            print("----------------------------------------------------------------------------")
            print(f"{Gavin.name} has fallen")
            print("----------------------------------------------------------------------------")
            break
else:
    print("Invalid Choice")