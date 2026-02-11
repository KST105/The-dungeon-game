from scr.businesslogic_upper import *
from scr.businesslogic_lower import *
import os


user_input = 0

while user_input != "exit":
    print(show_map())
    user_input = input("введите направлении сканирования")
    scan_halls_around(user_input)
    print(bl.show_map())
    user_input = input("введите направлении движения")
    dungeon_movement(user_input)
    print(bl.show_map())
    user_input = input("exit?")


