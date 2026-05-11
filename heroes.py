class Hero:
    def __init__(self, name, exp, exp_limit, lvl, hp, mp, atk, inventory, skills):
        self.__name = name
        self.__exp = exp
        self.__exp_limit = exp_limit
        self.__lvl = lvl
        self.__hp = hp
        self.__mp = mp
        self.__atk = atk
        self.__inventory = inventory
        self.__skills = skills
    def lvl_up(self):
        self.__exp = 0
        self.__exp_limit += 100
        self.__lvl += 1
        self.__hp += 20
        self.__mp += 5
        self.__atk += 2
        print(f"{self.__name} has leveled up! Level: {self.__lvl}")
    def show_status(self):
        print(f"{self.__name}'s status: ")
        print(f"Level: {self.__lvl}")
        print(f"Experience: {self.__exp}")
        print(f"Health: {self.__hp}")
        print(f"Mana: {self.__mp}")
        print(f"Attack: {self.__atk}")
        print(f"Inventory: {self.__inventory}")
        print(f"Skills: {self.__skills}")
    def attack(self, target):
        damage = self.__atk
        print(f"{self.__name} attacks!")
        target.take_damage(damage)
    

Bob = Hero("Bob", 0, 1, 100, 10, 5, {"title": "Iron Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
Bob.show_status

