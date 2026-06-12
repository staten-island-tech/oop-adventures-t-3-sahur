from Heros import Gavin
Score = ""
day = 0
if Gavin.hp <= 0:
    print("Days: ", day)
    if day <= 5:
        Score = ("F")
    elif day <= 10:
        Score = ("E")
    elif day <= 15:
        Score = ("D")
    elif day <= 20:
        Score = ("C")
    elif day <= 30:
        Score = ("B")
    elif day <= 50:
        Score = ("A")
    else:
        Score = ("S")
