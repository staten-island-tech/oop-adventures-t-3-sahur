import random
from Heros import Hero
from Monsters import enemies_list
from Monsters import Enemy


Bob = Hero("Bob", 0, 100, 1, 100, 10, 5, {"title": "Iron Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})

Option = input("What would you like to do? Fight or rest: ")
if Option == "rest":
    Bob.__hp += 10
    print(f"Bob is well rested. Hp is now {Bob.__hp}")
elif Option == "fight":
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
    elif choice == "2":
        print("SLASH")     
    else:
        print("Invalid choice")
    if not Fight.alive():
        print(f"{Fight._Enemy__name} has been defeated!")
