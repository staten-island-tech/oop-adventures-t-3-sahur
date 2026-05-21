""" from Heros import Hero
Gavin = Hero("Gavin", 0, 100, 1, 100, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})

while Gavin.hp >= 0 or Fight.hp >= 0:
        Fight.show_enemy() 
        choice = input("Pick 1 or 2:")
        if choice == "1":
            print(f"Gavin attacks {Fight.name}!")
            attack_dmg = Gavin.atk + 2
            Fight.hp -= Gavin.atk
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            round +=1
            Gavin.mp +=1
        elif choice == "2":
            print(f"Gavin slashes {Fight.name}!")
            slash_dmg = Gavin.atk + 5
            Fight.hp -= slash_dmg
            print(f"{Fight.name}'s hp is now {Fight.hp}")
            round +=1
            Gavin.mp +=1 """