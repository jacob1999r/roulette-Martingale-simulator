import random

def random_bankroll(min: int, max: int):
    # randomise the bankroll, ensuring it falls within the given range
    x = (max - min)* random.random()
    return round(min + x)