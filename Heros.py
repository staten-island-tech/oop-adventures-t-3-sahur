class Hero:
<<<<<<< HEAD
    def __init__(self, name, exp, exp_limit, lvl, hp, hp_limit, mp, mp_limit, atk, inventory, skills):
=======
    def __init__(self, name, exp, exp_limit, lvl, hp, health_max, mp, mana_max, atk, inventory, skills):
>>>>>>> 2dbc03c30e4a7ad4c1ed18a625c72e8318dc1506
        self.name = name
        self.exp = exp
        self.exp_limit = exp_limit
        self.lvl = lvl
        self.hp = hp
<<<<<<< HEAD
        self.hp_limit = hp_limit
=======
        self.health_max = health_max
        self.mana_max = mana_max
>>>>>>> 2dbc03c30e4a7ad4c1ed18a625c72e8318dc1506
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
            self.hp += 20
            self.hp_limit += 20
            self.mp += 2
<<<<<<< HEAD
            self.mp_limit += 2
=======
            self.health_max += 20
            self.mana_max += 2
>>>>>>> 2dbc03c30e4a7ad4c1ed18a625c72e8318dc1506
            self.atk += 2
        print(f"{self.name} has leveled up! Level: {self.lvl}")
    def show_status(self):
        print(f"{self.name}'s status: ")
        print(f"Level: {self.lvl}")
        print(f"Experience: {self.exp}/{self.exp_limit}")
        print(f"Health: {self.hp}/{self.health_max}")
        print(f"Mana: {self.mp}/{self.mana_max}")
        print(f"Attack: {self.atk}")
        print(f"Inventory: {self.inventory}")
        print(f"Skills: {self.skills}")
<<<<<<< HEAD
    def attack(self):
        damage = self.atk
        print(f"{self.name} attcks")
    def death(self):
        if self.hp > 0:
            self.hp = 0
        print("You have died.")
<<<<<<< Updated upstream
Gavin = Hero("Gavin", 0, 100, 1, 100, 5, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
=======
Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 10, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3})
>>>>>>> Stashed changes
=======

Gavin = Hero("Gavin", 0, 100, 1, 100, 100, 10, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})
>>>>>>> 2dbc03c30e4a7ad4c1ed18a625c72e8318dc1506
Gavin.show_status()