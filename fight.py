import random
from Heros import Gavin
from Monsters import enemies_list
from item import weapon

def battle(Gavin):
    Fight = random.choice(enemies_list)
    rounds = 0
    while Gavin.hp > 0 and Fight.hp > 0:
        Option = input("Pick a choice: 1. Fight or 2. Run to inn")
        if Option == "2":
            if Gavin.hp >= Gavin.health_max:
                print("Gavin is already max hp")
            else:
                Gavin.hp += 10
                if Gavin.hp > Gavin.health_max:
                    Gavin.hp = Gavin.health_max
            Gavin.show_status()
        elif Option == "1":
            print(f"Hero encounters a {Fight.name}")
            print("----------------------------------------------------------------------------")
            Fight.show_enemy()
            print(f"Round {rounds}")
            print("----------------------------------------------------------------------------")
            print("What action do you like to do:")
            print("1: Attack")
            print("2: Slash")
            choice = input("Pick 1 or 2: ")
            print("----------------------------------------------------------------------------")
            if choice == "1":
                rounds += 1
                weapon(Gavin, rounds)
                print(f"Round {rounds}")
                print(f"Hero attacks {Fight.name}")
                print("----------------------------------------------------------------------------")
                atk_dmg = Gavin.atk + 2
                Fight.hp -= atk_dmg
                print(f"{Fight.name}'s hp is now {Fight.hp}")
                print(f"{Gavin.name}'s hp is now {Gavin.hp}")
                print(f"{Gavin.name}'s mp is now {Gavin.mp}")
                Gavin.mp += 1
            elif choice == "2": 
                rounds += 1
                weapon(Gavin, rounds)
                print(f"Round {rounds}")
                print(f"Hero slashes {Fight.name}")
                print("----------------------------------------------------------------------------")
                Gavin.mp -= 3
                slash_dmg = Gavin.atk + 5
                Fight.hp -= slash_dmg
                print(f"{Fight.name}'s hp is now {Fight.hp}")
                print(f"{Gavin.name}'s hp is now {Gavin.hp}")
                print(f"{Gavin.name}'s mp is now {Gavin.mp}")
                Gavin.mp += 1
            else:
                rounds += 1
                weapon(Gavin, rounds)
                print(f"Round {rounds}")
                print("Invalid choice")   
                Gavin.show_status()
            Gavin.hp -= Fight.atk
            if Fight.hp <= 0:
                print("----------------------------------------------------------------------------")
                print("The battle is over")
                print("----------------------------------------------------------------------------")
                print(f"Hero gained {Fight.exp_given} experience.")
                Gavin.exp += Fight.exp_given
                Gavin.lvl_up()
                Gavin.show_status()
                Fight = random.choice(enemies_list)
                Fight.hp = Fight.hp_limit
                break
            if Gavin.hp <= 0:
                print("----------------------------------------------------------------------------")
                print(f"{Gavin.name} has fallen")
                print("----------------------------------------------------------------------------")
                break
    else:
        print("Invalid Choice")