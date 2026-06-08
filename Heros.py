class Hero:
    def __init__(self, name, exp, exp_limit, lvl, hp, health_max, mp, mana_max, atk, inventory, skills):
        self.name = name
        self.exp = exp
        self.exp_limit = exp_limit
        self.lvl = lvl
        self.hp = hp
        self.health_max = health_max
        self.mana_max = mana_max
        self.mp = mp
        self.atk = atk
        self.inventory = inventory
        self.skills = skills
    def lvl_up(self):
        if self.exp >= self.exp_limit:
            self.exp = 0
            self.exp_limit += 100
            self.lvl += 1
            self.hp += 20
            self.mp += 2
            self.health_max += 20
            self.mana_max += 2
            self.atk += 2
            print(f"{self.name} has leveled up! Level: {self.lvl}")
    def show_status(self):
        print("=====================================")
        print(f"{self.name}'s status: ")
        print("=====================================")
        print(f"Level: {self.lvl}")
        print(f"Experience: {self.exp}/{self.exp_limit}")
        print(f"Health: {self.hp}/{self.health_max}")
        print(f"Mana: {self.mp}/{self.mana_max}")
        print(f"Attack: {self.atk}")
        print(f"Inventory: {self.inventory}")
        print(f"Skills: {self.skills}")
    def max(self):
        if self.mp >= self.mana_max:
            print("Gavin is already max hp")
        else:
            self.mp += 1
            if self.mp > self.mana_max:
                self.mp = self.mana_max

Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 10, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
Gavin.show_status()