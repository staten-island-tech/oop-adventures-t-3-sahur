import random
from Heros import Hero
from Enemies import Enemy
from Enemies import enemies_list
Gavin = Hero("Gavin", 0, 100, 1, 100, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
round = 0
Fight = random.choice(enemies_list)
Option = input("Pick a choice. 1. Fight 2. Rest")
if Option == "2":
    Gavin.hp += 10
    print(f"Gavin is now well rested. Hp is now {Gavin.hp}")
elif Option == "1":
   print(f"Gavin encounters a {Fight.name}!")
   Fight.show_enemy()
   print(f"Round {round}")
print("What action would you like to do:")
print("1. Attack")
print("2. Slash")
while Gavin.hp >= 0 or Fight.hp >= 0:
        Fight.show_enemy() 
        choice = input("Pick 1 or 2:")
        if choice == "1":
            print(f"Gavin attacks {Fight.name}!")
            attack_dmg = Gavin.atk + 2
            Fight.hp -= Gavin.atk
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            round +=1
            Gavin.mp +=1
        elif choice == "2":
            print(f"Gavin slashes {Fight.name}!")
            Gavin.mp -=2
            slash_dmg = Gavin.atk + 5
            Fight.hp -= slash_dmg
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            round +=1
            Gavin.mp +=1
        if Gavin.hp <= 0 or Fight.hp <= 0:
           print("The battle is over")
           Gavin.exp += 15
           Gavin.show_status()
           break
else:
    print("Invalid choice")