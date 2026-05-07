import random 
class Hero:
    def __init__(self, name, exp, lvl, hp, mp, atk, inventory, skills):
        self.name = name
        self.exp = exp
        self.lvl = lvl
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.inventory = inventory
        self.skills = skills
    def lvl_up(self):
        self.lvl += 1
        self.exp = 0
        self.hp += 20
        self.mp += 5
        self.atk += 2
        print(f"{self.name} leveled up to {self.lvl}!")
class Enemy:
     def __init__(self, name, hp, atk, mp, inventory, skills):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.mp = mp
        self.inventory = inventory
        self.skills = skills
Goblin = Enemy("Goblin", 45, 3, 5, {"title": "Wooden Dagger", "atk": 2}, {"title": "Stab", "atk": 2})
Goblin_Archer = Enemy("Goblin Archer", 35, 4, 10, {"title": "Short Bow", "atk": 3}, {"title": "Aim", "atk": 5})
Goblin_Brute = Enemy("Goblin Brute", 75, 2, 5, {"title": "Leather Armor", "hp": 10}, {"title": "Taunt", "mp": -2})
Gavin = Hero("Gavin", 0, 1, 100, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
enemies = [Goblin, Goblin_Archer, Goblin_Brute]
Fight = random.choice(enemies)
print(f"Gavin encounters a {Fight.name}!")