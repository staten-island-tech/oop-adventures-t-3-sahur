import fight

def Score(kills):
    if kills <= 5:
        return "F"
    elif kills <= 10:
        return "E"
    elif kills <= 15:
        return "D"
    elif kills <= 20:
        return "C"
    elif kills <= 30:
        return "B"
    elif kills <= 50:
        return "A"
    else:
        return "S"