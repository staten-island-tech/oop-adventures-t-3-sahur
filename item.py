def weapon_upgrade(Gavin, round_count):
    if round_count == 100:
        Gavin.inventory = {"title": "Stone Sword", "atk": 5}
        print(f"Gavin's weapon upgraded to a Stone Sword!")
    elif round_count == 250:
        Gavin.inventory = {"title": "Iron Sword", "atk": 10}
        print(f"Gavin's weapon upgraded to a Iron Sword!")
    elif round_count == 500:
        Gavin.inventory = {"title": "Diamond Sword", "atk": 20}
        print(f"Gavin's weapon upgraded to a Diamond Sword!")
    elif round_count == 1000:
        Gavin.inventory = {"title": "Netherite Sword", "atk": 40}
        print(f"Gavin's weapon upgraded to a Netherite Sword!")