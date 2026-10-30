from scr import gamelogic_lower as gl_l
from scr import inventory as inv
from scr import massages_player as mp
from scr import gamelogic_ui as pg


def battle_round(enemy, battle_tactic, battle_action):

    if battle_tactic == "attack":

        enemy_attack = gl_l.enemy_attack_generator(enemy["attack"])

        if enemy_attack == battle_action:

            enemy["hp"] -= inv.damage
            inv.hp -= enemy["damage"]

            message = f"{mp.receiving_damage(enemy["damage"], inv.hp)} \n{mp.taking_damage_opponent(inv.damage, enemy["hp"], enemy["type"])} \n{mp.massage_choose_tactics}"

        elif (enemy_attack == "melee" and battle_action == "range") or (enemy_attack == "range" and battle_action == "magic") or (enemy_attack == "magic" and battle_action == "melee"):

            enemy["hp"] -= inv.damage * 0.5
            inv.hp -= enemy["damage"] * 2

            message = f"{mp.receiving_damage(enemy["damage"] * 2, inv.hp)} \n{mp.taking_damage_opponent(inv.damage * 0.5, enemy["hp"], enemy["type"])} \n{mp.massage_choose_tactics}"

        elif (enemy_attack == "melee" and battle_action == "magic") or (enemy_attack == "range" and battle_action == "melee") or (enemy_attack == "magic" and battle_action == "range"):

            enemy["hp"] -= inv.damage * 2
            inv.hp -= enemy["damage"] * 0.5

            message = f"{mp.receiving_damage(enemy["damage"] * 0.5, inv.hp)} \n{mp.taking_damage_opponent(inv.damage * 2, enemy["hp"], enemy["type"])} \n{mp.massage_choose_tactics}"

    elif battle_tactic == "defence":

        enemy_attack = gl_l.enemy_attack_generator(enemy["attack"])

        if enemy_attack == battle_action:
            enemy["hp"]-= inv.damage * 0.5

            message = f"{mp.taking_damage_opponent(inv.damage * 0.5, enemy["hp"], enemy["type"])} \n{mp.massage_choose_tactics}"

        else:
            inv.hp -= enemy["damage"] * 2
            message = f"{mp.receiving_damage(enemy["damage"] * 2, inv.hp)} \n{mp.massage_choose_tactics}"

    inv.counter_scan = 0

    return message

def dungeon_movement(direction_movement):

    if direction_movement == "s":

        gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "X"
        gl_l.current_floor += 1

        if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "?":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room()

            inv.counter_scan -= 0.5
            if inv.counter_scan < 0:
                inv.counter_scan = 0

        if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "Ш":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            inv.hp -= gl_l.trap_damage
            return mp.receiving_damage(gl_l.trap_damage, inv.hp)

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "O":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            return mp.massage_empty_hall

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "B":
            gl_l.reward_from_chest(gl_l.counter_guarantee_key)
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            return mp.massage_chest_found

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] in ("#","*"):

            gl_l.current_floor -= 1
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            return mp.massage_dead_end

        gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
        return mp.massage_repeat_visit

    elif direction_movement == "w":

        gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "X"
        gl_l.current_floor -= 1

        if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "?":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room()

            inv.counter_scan -= 0.5
            if inv.counter_scan < 0:
                inv.counter_scan = 0

        if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "Ш":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            inv.hp -= gl_l.trap_damage
            return mp.receiving_damage(gl_l.trap_damage, inv.hp)

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "O":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            return mp.massage_empty_hall

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "B":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            gl_l.reward_from_chest(gl_l.counter_guarantee_key)
            return mp.massage_chest_found

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall]in ("#","*"):

            gl_l.current_floor += 1
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            return mp.massage_dead_end

        gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
        return mp.massage_repeat_visit

    elif direction_movement == "a":

        gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "X"
        gl_l.current_hall -= 1

        if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "?":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room()

            inv.counter_scan -= 0.5
            if inv.counter_scan < 0:
                inv.counter_scan = 0

        if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "Ш":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            inv.hp -= gl_l.trap_damage
            return mp.receiving_damage(gl_l.trap_damage, inv.hp)

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "O":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            return mp.massage_empty_hall

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "B":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            gl_l.reward_from_chest(gl_l.counter_guarantee_key)
            return mp.massage_chest_found

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] in ("#","*"):

            gl_l.current_hall += 1
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            return mp.massage_dead_end

        gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
        return mp.massage_repeat_visit

    elif direction_movement == "d":

        gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "X"
        gl_l.current_hall += 1

        if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "?":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room()

            inv.counter_scan -= 0.5
            if inv.counter_scan < 0:
                inv.counter_scan = 0

        if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "Ш":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            inv.hp -= gl_l.trap_damage
            return mp.receiving_damage(gl_l.trap_damage, inv.hp)

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "O":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            return mp.massage_empty_hall

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "B":
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            gl_l.reward_from_chest(gl_l.counter_guarantee_key)
            return mp.massage_chest_found

        elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] in ("#","*"):
            gl_l.current_hall -= 1
            gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
            return mp.massage_dead_end

        gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = "H"
        return mp.massage_repeat_visit

def scan_halls_around(scan_direction):

    while scan_direction in ("w", "a", "s", "d"):

        if scan_direction in ("w", "a", "s", "d"):
            inv.counter_scan += 1

            if inv.counter_scan >= inv.max_counter_scan:
                mp.print_massage(mp.massage_beginnin_battle)
                return True

            if scan_direction == "a":
                gl_l.current_hall -= 1

                if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "?":
                    gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room()

                else:
                    gl_l.current_hall += 1
                    return mp.massage_repeat_research

                if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "Ш":
                    message = mp.message_detection_trap

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "O":
                    message = mp.message_detection_empty

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "#":
                    message = mp.message_detection_impasse

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "B":
                    message = mp.message_detection_chest

                gl_l.current_hall += 1
                return message

            elif scan_direction == "d":
                gl_l.current_hall += 1

                if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "?":
                    gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room()


                else:
                    gl_l.current_hall -= 1
                    return mp.massage_repeat_research

                if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "Ш":
                    message = mp.message_detection_trap

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "O":
                    message = mp.message_detection_empty

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "#":
                    message = mp.message_detection_impasse

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "B":
                    message = mp.message_detection_chest

                gl_l.current_hall -= 1
                return message

            elif scan_direction == "s":
                gl_l.current_hall += 1

                if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "?":
                    gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room()

                else:
                    gl_l.current_floor -= 1
                    return mp.massage_repeat_research

                if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "Ш":
                    message = mp.message_detection_trap

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "O":
                    message = mp.message_detection_empty

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "#":
                    message = mp.message_detection_impasse

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "B":
                    message = mp.message_detection_chest

                gl_l.current_floor -= 1
                return message

            elif scan_direction == "w":
                gl_l.current_floor -= 1

                if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "?":
                    gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room()

                else:
                    gl_l.current_floor += 1
                    return mp.massage_repeat_research

                if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "Ш":
                    message = mp.message_detection_trap

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "O":
                    message = mp.message_detection_empty

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "#":
                    message = mp.message_detection_impasse

                elif gl_l.game_map[gl_l.current_floor][gl_l.current_hall] == "B":
                    message = mp.message_detection_chest

                gl_l.current_floor += 1
                return message

    return

def destroy_object(direction):

    while direction in ("w", "a", "s", "d"):

        if direction == "a":
            gl_l.current_hall -= 1

            if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] in ("#","Ш"):
                gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room_in_destruction()
                gl_l.current_hall += 1
                return

            else:
                gl_l.current_hall += 1
                return mp.message_invalid_destruction_object

        elif direction == "d":
            gl_l.current_hall += 1

            if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] in ("#","Ш"):
                gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room_in_destruction()
                gl_l.current_hall -= 1
                return

            else:
                gl_l.current_hall -= 1
                return mp.message_invalid_destruction_object

        elif direction == "s":
            gl_l.current_floor += 1

            if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] in ("#","Ш"):
                gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room_in_destruction()
                gl_l.current_floor -= 1
                return

            else:
                gl_l.current_floor -= 1
                return mp.message_invalid_destruction_object

        elif direction == "w":
            gl_l.current_floor -= 1

            if gl_l.game_map[gl_l.current_floor][gl_l.current_hall] in ("#","Ш"):
                gl_l.game_map[gl_l.current_floor][gl_l.current_hall] = gl_l.exploring_room_in_destruction()
                gl_l.current_floor += 1
                return

            else:
                gl_l.current_floor += 1
                return mp.message_invalid_destruction_object
