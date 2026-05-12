import random
from Heros import Hero
from Enemies import Enemy
from Enemies import enemies_list
Gavin = Hero("Gavin", 0, 1, 100, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})

def attack(self, target):
        damage = self.__atk
        print(f"{self.__name} attacks!")
        target.take_damage(damage)

current_enemy = random.choice(enemies_list)
Option = input("Pick a choice. 1. Fight 2. Rest")
if Option == "2":
    Gavin.hp += 10
    print(f"Gavin is now well rested. Hp is now {Gavin.hp}")
elif Option == "1":
    print(f"Gavin encounters a {current_enemy.name}!")

    print("What action would you like to do:")
    print("1. Attack")
    print("2. Slash")
    choice = input("Pick 1 or 2:")

    if choice == "1":
        Gavin.atk(current_enemy)
    if choice == "2":
        slash_dmg = Gavin.atk + 3
else:
        print("Invalid choice")