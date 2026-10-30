import random
from pickle import GLOBAL

from scr import gamelogic_lower as gl_l
from scr import inventory as inv
from scr import massages_player as mp


counter_guarantee_chest = 0
value_guaranteed_chest = 4
counter_guarantee_key = 0
value_guarantee_key = 4
size_dungeon = 13
count_floor = size_dungeon
count_hall = size_dungeon + 2
current_floor = 12
current_hall = count_hall  // 2
trap_damage = 15
triumphant_number_keys = 5
max_health_potion = 6
max_power_potion = 5

probability_appearing_objects = [30, 30, 15,25]
probability_appearing_rewards = [15, 85]

map_objects = ["trap", "nothing", "chest", "impasse"]
probability_reward_type = ["key", "potion"]
probability_enemy_type = ["Dark Elf", "Goblin Marauder", "Cursed Knight"]
map_objects_in_destruction = ["nothing", "chest"]
probability_appearing_objects_in_destruction = [70, 30]

def exploring_room_in_destruction():

    result_investigation = random.choices(map_objects_in_destruction, weights=probability_appearing_objects_in_destruction)[0]

    if result_investigation == "nothing":
        result = "O"
        return result

    elif result_investigation == "chest":
        result = "B"
        return result


def reward_from_chest(counter_guarantee_key):

    counter_guarantee_key += 1
    gl_l.counter_guarantee_key = counter_guarantee_key

    if counter_guarantee_key == value_guarantee_key:
        inv.key += 1
        gl_l.counter_guarantee_key = 0

        return mp.print_massage(mp.found_key)

    reward_chest = random.choices(probability_reward_type, weights=probability_appearing_rewards)[0]

    if reward_chest == "key":
        inv.key += 1
        gl_l.counter_guarantee_key = 0

        mp.print_massage(f"You have found the key. There are still {5 - int(inv.key)} left to find.")

    if inv.health_potion == max_health_potion and  inv.power_potion >= max_power_potion:

        inv.key += 1

        gl_l.counter_guarantee_key = 0

        return mp.print_massage (f"Your potion supplies are full. You found a key instead!")

    if inv.health_potion == max_health_potion:
        inv.power_potion += 1

        return mp.print_massage(f"You have found a power potion. Current count: {inv.power_potion}.")

    elif inv.power_potion == max_power_potion:

        inv.health_potion += 1

        return mp.print_massage(f"You have found a healing potion. Current count: {inv.health_potion}.")

    else:

        number = random.randint(0, 1)

        if number == 0:

            inv.health_potion += 1
            return mp.print_massage(f"You have found a healing potion. Current count: {inv.health_potion}.")

        else:

            inv.power_potion += 1
            return mp.print_massage(f"You have found a power potion. Current count: {inv.power_potion}.")

def enemy_attack_options(type_enemy):

    if type_enemy == "Dark Elf":
        dark_elf_attack = ["magic", "range"]
        return dark_elf_attack

    elif type_enemy == "Goblin Marauder":
        goblin_marauder_attack = ["range", "melee"]
        return goblin_marauder_attack

    elif type_enemy == "Cursed Knight":
        cursed_knight_attack = ["melee", "magic"]
        return cursed_knight_attack

def enemy_attack_generator(attack):

    probability_attack = [2, 1]
    result_investigation = random.choices(attack, weights=probability_attack)[0]
    return result_investigation

def map_generation():

    global game_map

    game_map = [["*" for hall in range(count_hall)] for floor in range(count_floor)]

    for floor in range(1, count_floor-1):
        for hall in range(1, count_hall-1):
            game_map[floor][hall] = "?"

    game_map[current_floor][current_hall] = "H"

    return game_map

game_map = map_generation()

def verification_guaranteed_chest(result):

    if result != "chest":
        gl_l.counter_guarantee_chest += 1

        if gl_l.counter_guarantee_chest == value_guaranteed_chest:
            result = "chest"
            gl_l.counter_guarantee_chest = 0
            return result

        return result

def exploring_room():

    result_investigation = random.choices(map_objects, weights=probability_appearing_objects)[0]

    if result_investigation == "trap":
        result = "Ш"
        return result

    elif result_investigation == "nothing":
        result = "O"
        return result

    elif result_investigation == "chest":
        result = "B"
        return result

    elif result_investigation == "impasse":
        result = "#"
        return result

def show_map():

    for i in range(0, count_floor):
        for j in range(0, count_hall):
            print(game_map[i][j], end=" ")
        print(end="\n")

    return ""

def enemy_hp_generator():

    enemy_hp = random.randint(20, 50)
    return enemy_hp

def enemy_damage_generator():

    enemy_damage = random.randint(10, 30)
    return enemy_damage

def use_health_potion():

    if inv.health_potion == 0:
        return mp.is_no_potion

    inv.health_potion -= 1
    inv.hp += 15

    if inv.hp > 100:
        inv.hp = 100

    return mp.drink_healing_potion

def use_power_potion():

    if inv.power_potion == 0:
        return mp.is_no_potion

    inv.power_potion -= 1
    inv.damage += 5

    return mp.drink_power_potion

def generation_enemy_type():

    enemy_type = random.choice(probability_enemy_type)
    return enemy_type

enemy = {}

def enemy_generator():

    enemy_type = generation_enemy_type()

    enemy["hp"] = enemy_hp_generator()
    enemy["damage"] = enemy_damage_generator()
    enemy["type"] = enemy_type
    enemy["attack"] = enemy_attack_options(enemy_type)

    massage = f"{mp.meeting_with_enemy(enemy_type)} {mp.massage_beginnin_battle} \n{mp.massage_choose_tactics}"

def reset_characteristics():
    inv.hp = 100
    inv.damage = 20
    inv.health_potion = 1
    inv.power_potion = 0
    inv.key = 0
    inv.counter_scan = 0
    inv.max_counter_scan = 6

def world_reset():
    global current_floor, current_hall
    global game_map, counter_guarantee_chest, counter_guarantee_key

    current_floor = 12
    current_hall = count_hall // 2

    counter_guarantee_chest = 0
    counter_guarantee_key = 0

    game_map = [["*" for _ in range(count_hall)]for _ in range(count_floor)]

    for floor in range(1, count_floor - 1):
        for hall in range(1, count_hall - 1):
            game_map[floor][hall] = "?"

    game_map[current_floor][current_hall] = "H"

    enemy.clear()