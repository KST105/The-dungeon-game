import random
from scr import inventory as inv


counter_guarantee_box = 0
counter_guarantee_key = 0

probability_appearing_objects = [3, 3.5, 1.5, 2]
map_objects = ["trap", "nothing", "loot box", "impasse"]

size_dungeon = 11 #odd value
curren_floor = 0
curren_hall = 5

counter_scan = 0

probability_enemy_type = ["Dark Elf", "Goblin Marauder", "Cursed Knight"]

def enemy_attack_options(type_enemy):
    if type_enemy == "Dark Elf":
        dark_elf_attack = ["range", "magic"]
        return dark_elf_attack
    elif type_enemy == "Goblin Marauder":
        goblin_marauder_attack = ["melee ", "range"]
        return goblin_marauder_attack
    elif type_enemy == "Cursed Knight":
        cursed_knight_attack = ["magic", "melee"]
        return cursed_knight_attack

def enemy_attack_generator(attack):
    probability_attack = [2, 1]
    result_investigation = random.choices(attack, weights=probability_attack)[0]
    return result_investigation

def map_generation():

    game_map = [["#" for hall in range(size_dungeon)] for floor in range(size_dungeon)]

    for floor in range(1, size_dungeon-1):
        for hall in range(1, size_dungeon-1):
            game_map[floor][hall] = "?"

    game_map[curren_floor][curren_hall] = "H"

    return game_map

game_map = map_generation()

def exploring_room():

    result_investigation = random.choices(map_objects, weights=probability_appearing_objects)[0]

    if result_investigation == "trap":
        result = "Ш"
    elif result_investigation == "nothing":
        result = "O"
    elif result_investigation == "loot box":
        result = "B"
    elif result_investigation == "impasse":
        result = "#"

    return result

def show_map():

    for i in range(0, size_dungeon):
        for j in range(0, size_dungeon):
            print(game_map[i][j], end=" ")
        print(end="\n")

    return ""

def enemy_hp_generator():
    enemy_hp = random.randint(30, 70)
    return enemy_hp

def enemy_damage_generator():
    enemy_damage = random.randint(10, 30)
    return enemy_damage

def hit(attack_damage, defenders_hp ):
        defenders_hp -= attack_damage

def use_health_potion():
    inv.health_potion -= 1
    inv.hp += 25

    if inv.hp > 100:
        inv.hp = 100

    return""

def generation_enemy_type():
    enemy_type = random.choice(probability_enemy_type)
    return enemy_type

def use_power_potion():

    inv.damage += 5
    if inv.damage > 50:
        inv.damage = 100

    return""