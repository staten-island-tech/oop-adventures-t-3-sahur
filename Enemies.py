import random
class Enemy:
    def __init__(self, name, hp, atk, mp, exp_given, inventory, skills, skill):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.mp = mp
        self.exp_given = exp_given
        self.inventory = inventory
        self.skills = skills
        self.skill = skill
    def show_enemy(self):
        print(f"{self.name}'s status: ")
        print(f"Health: {self.hp}")
        print(f"Mana: {self.mp}")
        print(f"Attack: {self.atk}")
        print(f"Experience Given: {self.exp_given}")
        print(f"Inventory: {self.inventory}")
        print(f"Skills: {self.skills}, {self.skill}")
"""     def damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} too {amount} damage. Hp is now {self.hp}")
    def alive(self):
        return self.hp > 0
 """



Goblin = Enemy("Goblin", 50, 3, 5, 15, {"title": "Wooden Dagger", "atk": 2}, {"title": "Stab", "atk": 2, "mp": -1}, {"title": "Flurry", "atk": 4, "mp": -2})
Goblin_Archer = Enemy("Goblin Archer", 40, 4, 10, 20, {"title": "Short Bow", "atk": 3}, {"title": "Aim", "atk": 5, "mp": -2}, {"title": "Piercing Shot", "atk": 4, "mp": -1})
Goblin_Brute = Enemy("Goblin Brute", 80, 2, 5, 25, {"title": "Leather Armor", "hp": 10}, {"title": "Taunt", "atk": 2, "mp": -1}, {"title": "Headbutt", "atk": 5, "mp": -3})
enemies_list = [Goblin, Goblin_Archer, Goblin_Brute]