from Heros import Hero
Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 10, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
Score = 0
day = 0
if Gavin.hp <= 0:
    print("Days: ", day)
    if day <= 5:
        Score = ("F")
    if day <= 10:
        Score = ("E")
    if day <= 15:
        Score = ("D")
    if day <= 20:
        Score = ("C")
    if day <= 30:
        Score = ("B")
    if day <= 50:
        Score = ("A")
    if day <= 100:
        Score = ("S")
