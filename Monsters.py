import random

class Enemy:
    def __init__(self, name, hp, hp_limit, atk, mp, mana_limit, exp_given, inventory, skill):
        self.name = name
        self.hp = hp
        self.hp_limit = hp_limit
        self.atk = atk
        self.mana_limit = mana_limit
        self.mp = mp
        self.exp_given = exp_given
        self.inventory = inventory
        self.skill = skill
    def show_enemy(self):
        print(f"{self.name}'s status: ")
        print(f"Health: {self.hp}/{self.hp_limit}")
        print(f"Mana: {self.mp}/{self.mana_limit}")
        print(f"Attack: {self.atk}")
        print(f"Inventory: {self.inventory}")
        print(f"Skills: {self.skill}")


Goblin = Enemy("Goblin", 50, 50, 3, 5, 5, 15, {"title": "Wooden Dagger", "atk": 2}, {"title": "Stab", "atk": 2, "mp": -1})
Goblin_Archer = Enemy("Goblin Archer", 40, 40, 4, 10, 10, 20, {"title": "Short Bow", "atk": 3}, {"title": "Aim", "atk": 5, "mp": -2})
Goblin_Brute = Enemy("Goblin Brute", 80, 80, 2, 5, 5, 25, {"title": "Leather Armor", "hp": 10}, {"title": "Taunt", "atk": 2})
enemies_list = [Goblin, Goblin_Archer, Goblin_Brute]
""" Goblin_skills_list = ["name: Stab", "name: Flurry"]
Goblin_Archer_skills_list = ["name: Aim", "name: Piercing Shot"]
Goblin_Brute_skills_list = ["name: Taunt", "name: Headbutt"]
Goblin_skill_atk = random.choice(Goblin_skills_list)
Goblin_Brute_skill_atk = random.choice(Goblin_Archer_skills_list)
Goblin_Archer_skill_atk = random.choice(Goblin_Brute_skills_list)
print(Goblin_skill_atk)
print(Goblin_Archer_skill_atk)
print(Goblin_Brute_skill_atk) """