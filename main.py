from player import *
from config import *
import sys

player = Player()
running = True


def intro_screen():
    print("Welcome Traveler, what is your name? ")
    name = input()
    print("Are you a warrior, rogue, wizard, or cleric? ")
    player_class = input()
    player_selections = (name, player_class)
    return player_selections


def game_loop():
    while running:
        direction = input()
        player.move(direction)


player.name, player.player_class = intro_screen()
player.print_stats()
print(player.name, player.player_class)
print(mapdictionary[tilemap[player.player_pos_row][player.player_pos_column]])
game_loop()
