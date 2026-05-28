from fight import round
from Heros import Hero
Gavin = Hero("Gavin", 0, 100, 1, 100, 10, 5, {"title": "Wooden Sword", "atk": 2}, {"title": "Slash", "atk": 3, "mp": -2})

if round == 100:
    Gavin.inventory = {"title": "Stone Sword", "atk": 5}
if round == 250:
    Gavin.inventory = {"title": "Iron Sword", "atk": 10}
if round == 500:
    Gavin.inventory = {"title": "Diamond Sword", "atk": 20}
if round == 1000:
    Gavin.inventory = {"title": "Netherite Sword", "atk": 40}