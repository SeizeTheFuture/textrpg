import random


class Weapon:

    special_abilities = ["Vampiric"]

    def __init__(self):
        self.damage = 1 * random.randint(1, 10)
        self.type = None
        self.abilities = None

