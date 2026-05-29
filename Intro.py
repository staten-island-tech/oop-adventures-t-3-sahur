from Heros import Hero
Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 10, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
print("Welcome to Anson Town!")
print("You are playing as the hero, Gavin.")
print("Choose where you want to go!")
print("1. Forest")
print("2.Training Camp")
print("3. Inn")
Decision = input()
if Decision == "1":
    from fight import Option
    Option
elif Decision == "2":
    Gavin.atk += 1
    Gavin.hp_limit += 3