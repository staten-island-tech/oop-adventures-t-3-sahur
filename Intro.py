from Heros import Hero
Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 5, 5, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
print("Welcome to Anson Town!")
print("You are playing as the hero, Gavin.")
print("Choose where you want to go!")
print("1. Forest")
print("2.Training Camp")
print("3. Inn")
Decision = input()
if Decision == "1":
    print("Gavin is going to the forest...")
    from fight import Option
    Option
elif Decision == "2":
    Gavin.atk += 1
    Gavin.hp_limit += 3
    print("Gavin got stronger!")
    Decision
elif Decision == "3":
    Gavin.hp += 10
    print("Gavin is now well rested!")
    Decision
else:
    print("Invalid Choice")