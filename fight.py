import random
from Enemies import enemies_list
from Heros import Hero
from item import weapon_upgrade
def start_fight(Gavin: Hero, round_count):
    Fight = random.choice(enemies_list)
    if Fight.name == "Goblin":
            Fight.hp = 50
    elif Fight.name == "Goblin Archer":
            Fight.hp = 40
    else:
            Fight.hp = 80

    print(f"Gavin encounters a {Fight.name}!")
    print("-----------------------------------------------------------------------")
    Fight.show_enemy()

    while Gavin.hp >= 0 and Fight.hp >= 0:
        weapon_upgrade(Gavin, round_count)
        
        print("-----------------------------------------------------------------------")
        print(f"Total Game Rounds {round_count}")
        print(f"Gavin's HP: {Gavin.hp}/{Gavin.health_max}, MP: {Gavin.mp}/{Gavin.mana_max}")
        print("-----------------------------------------------------------------------")
        print("What action would you like to do:")
        print(f"1. Attack (with {Gavin.inventory["title"]})")
        print(f"2. {Gavin.skills["title"]}")

        choice = input("Pick 1 or 2:")
        print("-----------------------------------------------------------------------")

        if choice == "1":
                print(f"Gavin attacks {Fight.name}!")
                attack_dmg = Gavin.atk + Gavin.inventory["atk"]
                Fight.hp -= attack_dmg
                print(f"{Fight.name}'s HP is now {Fight.hp}")
                print(f"{Gavin.name}'s HP is now {Gavin.hp}")
                print(f"{Gavin.name}'s MP is now {Gavin.mp}")
                Gavin.mp += 1
                if Gavin.mp > Gavin.mana_max:
                    Gavin.mp = Gavin.mana_max
        elif choice == "2":
            mp_cost = 2
            if Gavin.mp < mp_cost:
                    print("Gavin does not have enough mana!")
                    continue
            else:
                print(f"Gavin slashes {Fight.name}!")
                Gavin.mp -= mp_cost
                slash_dmg = Gavin.atk + Gavin.skills["atk"]
                Fight.hp -= slash_dmg
                Gavin.mp -= 2
                Gavin.mp += 1
                if Gavin.mp > Gavin.mana_max:
                    Gavin.mp = Gavin.mana_max
                print(f"Gavin slashes {Fight.name}!")
                print(f"{Fight.name}'s HP is now {Fight.hp}")
                print(f"{Gavin.name}'s HP is now {Gavin.hp}")
                print(f"{Gavin.name}'s MP is now {Gavin.mp}")
        else:
            print("Invalid")
        if Fight.hp <= 0:
            print("-----------------------------------------------------------------------")
            print("The battle is over")
            print("-----------------------------------------------------------------------")
            Gavin.exp += Fight.exp_given
            print(f"Gavin gained {Fight.exp_given} experience!")
            print("-----------------------------------------------------------------------")
            Gavin.lvl_up()
            Gavin.total_rounds += 1
            Gavin.show_status
            break
        print(f"{Fight.name} is attacking.")
        enemy_skill = Fight.choose_atk()
        enemy_dmg = Fight.atk + enemy_skill["atk"]
        Gavin.hp -= enemy_dmg
        print(f"{Fight.name} uses {enemy_skill["title"]} and deals {enemy_dmg} damage!")

        if Gavin.hp <= 0:
                            print("-----------------------------------------------------------------------")
                            print("You have fallen. Game Over.")
                            print("-----------------------------------------------------------------------")
                            return round_count
        round_count +=1
    return round_count