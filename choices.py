from Heros import Hero
from fight import Fight
Gavin = Hero("Gavin", 0, 100, 1, 100, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
while Gavin.hp >= 0 or Fight.hp >= 0:
<<<<<<< HEAD
        Fight.show_enemy() 
        print(f"Round {round}") 
        print("What action would you like to do:")
        print("1. Attack")
        print("2. Slash")
        choice = input("Pick 1 or 2:")
        if choice == "1":
            print(f"Gavin attacks {Fight.name}!")
            attack_dmg = Gavin.atk + 2
            Fight.hp -= Gavin.atk
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            round +=1
        elif choice == "2":
            print(f"Gavin slashes {Fight.name}!")
            slash_dmg = Gavin.atk + 5
            Fight.hp -= slash_dmg
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            round +=1
=======
    print("What action do you like to do:")
    print("1: Attack")
    print("2: Slash")
    choice = input("Pick 1 or 2: ")
    if choice == "1":
        print(f"Gavin attacks {Fight.name}")
        atk_dmg = Gavin.atk + 2
        Fight.hp -= Gavin.atk
        print(f"{Fight.name}'s hp is now {Fight.hp}")
        round += 1
        Gavin.mp += 1
    elif choice == "2":
        print(f"Gavin slashes {Fight.name}")
        slash_dmg = Gavin.atk + 5
        Fight.hp -= slash_dmg
        print(f"{Fight.name}'s hp is now {Fight.hp}")
        round += 1
        Gavin.mp += 1
else:
    print("Invalid choice")
>>>>>>> 4b5681dc14af6926670f02606784ab777cde3019
