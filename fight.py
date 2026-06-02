import random
from Heros import Hero
from Enemies import enemies_list
Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 5, 5, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
round = 0
Fight = random.choice(enemies_list)
print("-----------------------------------------------------------------------")
Option = input("Pick a choice. 1. Fight 2. Rest")

if Option == "1":
    print(f"Gavin encounters a {Fight.name}!")
    while Gavin.hp >= 0 or Fight.hp >= 0:
        print("-----------------------------------------------------------------------")
        print("What action would you like to do:")
        print("1. Attack")
        print("2. Slash")
        choice = input("Pick 1 or 2:")
        Fight.show_enemy() 
        print("-----------------------------------------------------------------------")
        if choice == "1":
            print(f"Round {round}")
            print(f"Gavin attacks {Fight.name}!")
            print("-----------------------------------------------------------------------")
            attack_dmg = Gavin.atk + 2
            Fight.hp -= Gavin.atk
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            print(f"{Gavin.name}'s hp is now {Gavin.hp}")
            print(f"{Gavin.name}'s mp is now {Gavin.mp}")
            round +=1
            Gavin.mp +=1
        elif choice == "2":
            print(f"Round {round}")
            print(f"Gavin slashes {Fight.name}!")
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            print(f"{Gavin.name}'s hp is now {Gavin.hp}")
            print(f"{Gavin.name}'s mp is now {Gavin.mp}")
            Gavin.mp -=2
            slash_dmg = Gavin.atk + 5
            Fight.hp -= slash_dmg
            round +=1
            Gavin.mp += 1
        if Fight.hp <= 0:
           print("-----------------------------------------------------------------------")
           print("The battle is over")
           print("-----------------------------------------------------------------------")
           Gavin.exp += Fight.exp_given
           print(f"Gavin gained {Fight.exp_given} experience!")
           print("-----------------------------------------------------------------------")
           Gavin.lvl_up()
           Gavin.show_status()
           from Intro import Decision
           Decision

           
        if Gavin.hp <= 0:
            print("-----------------------------------------------------------------------")
            print("You have fallen.")
            print("-----------------------------------------------------------------------")
            break
else:
    print("Invalid Choice")
