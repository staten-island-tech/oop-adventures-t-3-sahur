class Hero:
    def __init__(self, name, exp, exp_limit, lvl, hp, hp_limit, mp, mp_limit, atk, inventory, skills):
        self.name = name
        self.exp = exp
        self.exp_limit = exp_limit
        self.lvl = lvl
        self.hp = hp
        self.hp_limit = hp_limit
        self.mp = mp
        self.mp_limit = mp_limit
        self.atk = atk
        self.inventory = inventory
        self.skills = skills
    def lvl_up(self):
        if self.exp >= self.exp_limit:
            self.exp = 0
            self.exp_limit += 100
            self.lvl += 1
            self.hp_limit += 10
            self.mp += 2
            self.atk += 2
        print(f"{self.name} leveled up to {self.lvl}!")
    def show_status(self):
        print(f"{self.name}'s status: ")
        print(f"Level: {self.lvl}")
        print(f"Experience: {self.exp}/{self.exp_limit}")
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
        print("You have died.")
Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 5, 5, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
Gavin.show_status()