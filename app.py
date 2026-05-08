from heroes import Hero
from Monsters import enemies_list
import random


Bob = Hero("Bob", 0, 1, 100, 10, 5, {"title": "Iron Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
Bob.show_status()

Fight = random.choice(enemies_list)
print("Battle Start!")
Fight.show_enemy()

print("What action do you take:")
print("1: Attack")
print("2: Slash")
choice = input("Pick 1 or 2: ")

if choice == "1":
    Bob.attack(Fight)
if choice == "2":
    print("SLASH")     
else:
    print("Invalid choice")

if not Fight.is_alive():
        print(f"{Fight._Enemy__name} has been defeated!")