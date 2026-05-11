class Enemy:
    def __init__(self, name, hp, atk, mp, inventory, skills):
        self.__name = name
        self.__hp = hp
        self.__atk = atk
        self.__mp = mp
        self.__inventory = inventory
        self.__skills = skills
    def show_enemy(self):
        print(f"{self.__name}'s status: ")
        print(f"Health: {self.__hp}")
        print(f"Mana: {self.__mp}")
        print(f"Attack: {self.__atk}")
        print(f"Inventory: {self.__inventory}")
        print(f"Skills: {self.__skills}")
    def damage(self, amount):
        self.__hp -= amount
        if self.__hp < 0:
            self.__hp = 0
        print(f"{self.__name} too {amount} damage. Hp is now {self.__hp}")
    def alive(self):
        return self.__hp > 0


Goblin = Enemy("Goblin", 45, 3, 5, {"title": "Wooden Dagger", "atk": 2}, {"title": "Stab", "atk": 2, "mp": -1})
Goblin_Archer = Enemy("Goblin Archer", 35, 4, 10, {"title": "Short Bow", "atk": 3}, {"title": "Aim", "atk": 5, "mp": -2})
Goblin_Brute = Enemy("Goblin Brute", 75, 2, 5, {"title": "Leather Armor", "hp": 10}, {"title": "Taunt", "atk": 2})
enemies_list = [Goblin, Goblin_Archer, Goblin_Brute]
