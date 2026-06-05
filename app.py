from Heros import Hero
Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 10, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
print("Welcome to Anson Town!")
print("You are playing as the hero, Gavin.")
while Gavin.hp > 0:
    print("Choose where you want to go.")
    print("1 - Forest")
    print("2 - Inn") 
    print("3 - Training Camp")
    print("4 - Quit Game")
    Decision = input("Decide where: ")
    if Decision == "1":
        print("Gavin is going to the forest...")
        from fight import Option
        Option
    elif Decision == "2":
        Gavin.hp += 10
        print(f"Gavin is well rested. Hp is now {Gavin.hp}")
        Gavin.show_status()
    elif Decision == "3":
        print("Gavin trained really, really hard.")
        Gavin.atk += 1
        Gavin.hp += 3
        Gavin.mp += 1
        Gavin.health_max += 3
        Gavin.mana_max += 1
        Gavin.show_status()
    elif Decision == "4":
        print("You have quit this game. Goodbye!")
        break
    else: 
        print("Invalid choice")