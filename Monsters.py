""" class Enemy:
    def __init__(self, name, hp, atk, mp, inventory, skills):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.mp = mp
        self.inventory = inventory
        self.skills = skills
    def show_enemy(self):
        print(f"{self.name}'s status: ")
        print(f"Health: {self.hp}")
        print(f"Mana: {self.mp}")
        print(f"Attack: {self.atk}")
        print(f"Inventory: {self.inventory}")
        print(f"Skills: {self.skills}")
    def target(self, amount):
        self.hp -= amount
        print(f"{self.name} too {amount} damage. Hp is now {self.hp}")
    def death(self):
        if self.hp > 0:
            self.hp = 0
        print(f"{self.name} has died.")


Goblin = Enemy("Goblin", 45, 3, 5, {"title": "Wooden Dagger", "atk": 2}, {"title": "Stab", "atk": 2, "mp": -1})
Goblin_Archer = Enemy("Goblin Archer", 35, 4, 10, {"title": "Short Bow", "atk": 3}, {"title": "Aim", "atk": 5, "mp": -2})
Goblin_Brute = Enemy("Goblin Brute", 75, 2, 5, {"title": "Leather Armor", "hp": 10}, {"title": "Taunt", "atk": 2})
enemies_list = [Goblin, Goblin_Archer, Goblin_Brute]
 """

import random
class Enemy:
    def __init__(self, name, hp, atk, mp, inventory, skills):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.mp = mp
        self.inventory = inventory
        self.skills = skills
    def show_enemy(self):
        print(f"{self.name}'s status: ")
        print(f"Health: {self.hp}")
        print(f"Mana: {self.mp}")
        print(f"Attack: {self.atk}")
        print(f"Inventory: {self.inventory}")
        print(f"Skills: {self.skills}")
    def damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} too {amount} damage. Hp is now {self.hp}")
    def alive(self):
        return self.hp > 0








Goblin = Enemy("Goblin", 45, 3, 5, {"title": "Wooden Dagger", "atk": 2}, {"title": "Stab", "atk": 2, "mp": -1})
Goblin_Archer = Enemy("Goblin Archer", 35, 4, 10, {"title": "Short Bow", "atk": 3}, {"title": "Aim", "atk": 5, "mp": -2})
Goblin_Brute = Enemy("Goblin Brute", 75, 2, 5, {"title": "Leather Armor", "hp": 10}, {"title": "Taunt", "atk": 2})
enemies_list = [Goblin, Goblin_Archer, Goblin_Brute]

