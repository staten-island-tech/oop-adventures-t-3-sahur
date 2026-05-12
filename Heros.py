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
    def show_status(self):
        print(f"{self.__name}'s status: ")
        print(f"Level: {self.__lvl}")
        print(f"Experience: {self.__exp}")
        print(f"Health: {self.__hp}")
        print(f"Mana: {self.__mp}")
        print(f"Attack: {self.__atk}")
        print(f"Inventory: {self.__inventory}")
        print(f"Skills: {self.__skills}")
