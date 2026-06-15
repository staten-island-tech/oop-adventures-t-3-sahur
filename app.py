from Heros import Gavin
from fight import battle
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
    elif Decision == "2":
        if Gavin.hp >= Gavin.health_max:
            print("Gavin is already max hp")    
        else:
            Gavin.hp += 10
            if Gavin.hp > Gavin.health_max:
                Gavin.hp = Gavin.health_max
        Gavin.show_status()
    elif Decision == "3":
        if Gavin.kills >=  Gavin.last_kill + 5:
            print("Gavin trained really, really hard.")
            Gavin.last_kill = Gavin.kills
            Gavin.atk += 1
            Gavin.hp += 3
            Gavin.mp += 1
            Gavin.health_max += 3
            Gavin.mana_max += 1
            Gavin.show_status()
        else:
            print("Training camp is locked.")
            print(f"Next training unlock at {Gavin.last_kill + 5} kills.")
    elif Decision == "4":
        print("Current kills:", Gavin.kills)
        print("Your final score is: ", Score(Gavin.kills))
        print("You have quit this game. Goodbye!")
        break
    else: 
        print("Invalid choice")