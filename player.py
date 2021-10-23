from gamemap import *


class Player:
    def __init__(self):

        self.hp = 100
        self.mp = 100
        self.str = 10
        self.int = 10
        self.con = 10
        self.agi = 10
        self.cha = 10
        self.wis = 10
        self.player_pos_row = 0
        self.player_pos_column = 0

        self.stats = {
            "hp": self.hp,
            "mp": self.mp,
            "strength": self.str,
            "intelligence": self.int,
            "constitution": self.con,
            "agility": self.agi,
            "charisma": self.cha,
            "wisdom": self.wis
        }
        self.name = None
        self.player_class = None

    def print_stats(self):
        for stat in self.stats:
            print(stat, self.stats[stat])

    def move(self, direction):

        match direction:
            case 'n':
                self.player_pos_row += 1
            case 's':
                self.player_pos_row -= 1
            case 'e':
                self.player_pos_column += 1
            case 'w':
                self.player_pos_column -= 1
            case _:
                print("Try again")
        try:
            print(mapdictionary[tilemap[self.player_pos_row][self.player_pos_column]])
        except IndexError:
            print("You have gone too far. Retrace your steps.")
