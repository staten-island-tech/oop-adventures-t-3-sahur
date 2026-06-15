import random
class Enemy:
    def __init__(self, name, hp, atk, mp, exp_given, inventory, skills,):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.mp = mp
        self.exp_given = exp_given
        self.inventory = inventory
        self.skills = skills
    def show_enemy(self):
        print(f"{self.name}'s status: ")
        print(f"Health: {self.hp}")
        print(f"Attack: {self.atk}")
        print(f"Experience: {self.exp_given}")
        print("-----------------------------------------------------------------------")
        for skill in self.skills:
            print(f" - {skill["title"]} (Atk: {skill["atk"]}, MP: {skill["mp"]})")
    def choose_atk(self):
        return random.choice(self.skills)


Goblin = Enemy("Goblin", 50, 3, 5, 15, {"title": "Wooden Dagger", "atk": 2},
                [{"title": "Stab", "atk": 2, "mp": -1}, {"title": "Flurry", "atk": 4, "mp": -2}])
Goblin_Archer = Enemy("Goblin Archer", 40, 4, 10, 20, {"title": "Short Bow", "atk": 3},
                       [{"title": "Aim", "atk": 5, "mp": -2}, {"title": "Piercing Shot", "atk": 4, "mp": -1}])
Goblin_Brute = Enemy("Goblin Brute", 80, 2, 5, 25, {"title": "Leather Armor", "hp": 10},
                      [{"title": "Taunt", "atk": 2, "mp": -1}, {"title": "Headbutt", "atk": 5, "mp": -3}])
enemies_list = [Goblin, Goblin_Archer, Goblin_Brute]
""" Goblin_skills_list = ["name: Stab", "name: Flurry"]
Goblin_Archer_skills_list = ["name: Aim", "name: Piercing Shot"]
Goblin_Brute_skills_list = ["name: Taunt", "name: Headbutt"]
Goblin_skills_attack = random.choice(Goblin_skills_list)
Goblin_Archer_skills_attack = random.choice(Goblin_Archer_skills_list)
Goblin_Brute_skills_attack = random.choice(Goblin_Brute_skills_list) """
""" if enemies_list == Goblin:
    print(Goblin_skills_attack)
elif enemies_list == Goblin_Archer:
    print(Goblin_Archer_skills_attack)
else:
    print(Goblin_Brute_skills_attack) """