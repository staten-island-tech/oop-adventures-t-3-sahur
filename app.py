from Heros import Gavin
from fight import battle
from result import day
from result import Score
print("Welcome to Anson Town!")
print("You are playing as the hero, Gavin.")
print("Choose where you want to go.")
while Gavin.hp > 0:
    print("1 - Forest")
    print("2 - Inn") 
    print("3 - Training Camp")
    print("4 - Quit Game")
    Decision = input("Decide where: ")
    if Decision == "1":
        print("Gavin is going to the forest...")
        battle(Gavin)
        day += 1
        print("Days:", day)
    elif Decision == "2":
        if Gavin.hp >= Gavin.health_max:
            print("Gavin is already max hp")
        else:
            Gavin.hp += 10
            if Gavin.hp > Gavin.health_max:
                Gavin.hp = Gavin.health_max
        Gavin.show_status()
        day += 1
        print("Days:", day)
    elif Decision == "3":
        print("Gavin trained really, really hard.")
        Gavin.atk += 1
        Gavin.hp += 3
        Gavin.mp += 1
        Gavin.health_max += 3
        Gavin.mana_max += 1
        Gavin.show_status()
        day += 1
        print("Days:", day)
    elif Decision == "4":
        print("You have quit this game. Goodbye!")
        print("Days:", day)
        print("Score:", Score)
        break
    else: 
        print("Invalid choice")