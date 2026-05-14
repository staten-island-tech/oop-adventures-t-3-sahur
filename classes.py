class Hero:
    def __init__(self, name, exp, lvl, hp, mp, atk, inventory, skills):
        self.__name = name
        self.__exp = exp
        self.__lvl = lvl
        self.__hp = hp
        self.__mp = mp
        self.__atk = atk
        self.__inventory = inventory
        self.__skills = skills
    def lvl_up(self, exp, lvl, hp, mp, atk):
        exp = 0
        lvl += 1
        hp += 100
        mp += 50
        atk += 5
        print(f"{self.__name} has leveled up! Levekl: {self.__lvl}")
    def show_status(self):
        print(f"{self.__name}'s status: ")
        print(f"Level: {self.__lvl}")
        print(f"Experience: {self.__exp}")
        print(f"Health: {self.__hp}")
        print(f"Mana: {self.__mp}")
        print(f"Attack: {self.__atk}")
        print(f"Inventory: {self.__inventory}")
        print(f"Skills: {self.__skills}")

Bob = Hero("Bob", 0, 1, 100, 100, 15, {"title": "Iron Sword", "atk": 5}, {"title": "Slash", "atk": 10, "mp": 25})
Bob.show_status