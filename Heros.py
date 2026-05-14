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
        print(f"{self.name}'s status: ")
        print(f"Level: {self.lvl}")
        print(f"Experience: {self.exp}")
        print(f"Health: {self.hp}")
        print(f"Mana: {self.mp}")
        print(f"Attack: {self.atk}")
        print(f"Inventory: {self.inventory}")
        print(f"Skills: {self.skills}")
    def attack(self):
        damage = self.atk
        print(f"{self.name} attcks")
    def death(self):
        if self.hp > 0:
            self.hp = 0
Gavin = Hero("Gavin", 0, 1, 100, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
Gavin.show_status()