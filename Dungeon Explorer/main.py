import pygame

from scr.gamelogic_upper import *
from scr.gamelogic_ui import *

running = True
scanning = False
destruction = False
combat_action = False
battle_state = "tactic"
game_state = "menu"

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if game_state == "menu":

                if event.key == pygame.K_1:
                    game_state = "game"

                elif event.key == pygame.K_2:
                    running = False

            elif game_state == "game":

                if combat_action:

                    if battle_state == "tactic":

                        if event.key == pygame.K_1:
                            battle_tactic = "attack"
                            battle_state = "action"
                            current_message = massage_select_attack

                        elif event.key == pygame.K_2:
                            battle_tactic = "defence"
                            battle_state = "action"
                            current_message = massage_select_defense

                    elif battle_state == "action":

                        if event.key == pygame.K_1:
                            battle_action = "melee"

                        elif event.key == pygame.K_2:
                            battle_action = "range"

                        elif event.key == pygame.K_3:
                            battle_action = "magic"

                        current_message = battle_round(enemy, battle_tactic, battle_action)
                        battle_state = "tactic"

                        if inv.hp <= 0 or enemy["hp"] <= 0:
                            combat_action = False
                            current_message = message_movement_direction

                elif event.key == pygame.K_q:
                    scanning = True
                    current_message = message_scan_direction

                elif scanning:

                    if event.key == pygame.K_w:

                        result = scan_halls_around("w")

                        if result is True:

                            current_message = enemy_generator()
                            combat_action = True
                            battle_state = "tactic"

                        else:
                            current_message = result

                        scanning = False

                    elif event.key == pygame.K_a:

                        result = scan_halls_around("a")

                        if result is True:

                            current_message = enemy_generator()
                            combat_action = True
                            battle_state = "tactic"

                        else:
                            current_message = result

                        scanning = False

                    elif event.key == pygame.K_s:

                        result = scan_halls_around("s")

                        if result is True:

                            current_message = enemy_generator()
                            combat_action = True
                            battle_state = "tactic"

                        else:
                            current_message = result

                        scanning = False

                    elif event.key == pygame.K_d:

                        result = scan_halls_around("d")

                        if result is True:

                            current_message = enemy_generator()
                            combat_action = True
                            battle_state = "tactic"

                        else:
                            current_message = result

                        scanning = False

                    elif event.key == pygame.K_x:
                        scanning = False

                elif event.key == pygame.K_r:
                    destruction = True
                    current_message = message_destruction_direction

                elif destruction:

                    if event.key == pygame.K_w:
                        current_message = destroy_object("w")
                        destruction = False
                        if current_message != mp.message_invalid_destruction_object:
                            current_message = enemy_generator()
                            combat_action = True
                            battle_state = "tactic"

                    elif event.key == pygame.K_a:
                        current_message = destroy_object("a")
                        destruction = False
                        if current_message != mp.message_invalid_destruction_object:
                            current_message = enemy_generator()
                            combat_action = True
                            battle_state = "tactic"

                    elif event.key == pygame.K_s:
                        current_message = destroy_object("s")
                        destruction = False
                        if current_message != mp.message_invalid_destruction_object:
                            current_message = enemy_generator()
                            combat_action = True
                            battle_state = "tactic"

                    elif event.key == pygame.K_d:
                        current_message = destroy_object("d")
                        destruction = False
                        if current_message != mp.message_invalid_destruction_object:
                            current_message = enemy_generator()
                            combat_action = True
                            battle_state = "tactic"

                    elif event.key == pygame.K_x:
                        destruction = False

                else:

                    if event.key == pygame.K_w:

                        hero_condition = "up"
                        current_message = dungeon_movement("w")

                    elif event.key == pygame.K_a:

                        hero_condition = "left"
                        current_message = dungeon_movement("a")

                    elif event.key == pygame.K_s:

                        hero_condition = "down"
                        current_message = dungeon_movement("s")

                    elif event.key == pygame.K_d:

                        hero_condition = "right"
                        current_message = dungeon_movement("d")

                    elif event.key == pygame.K_h:

                        current_message = use_health_potion()

                    elif event.key == pygame.K_g:

                        current_message = use_power_potion()

                    elif event.key == pygame.K_ESCAPE:
                        game_state = "menu"

    if inv.hp <= 0:

        world_reset()
        reset_characteristics()

        game_state = "menu"

    if game_state == "menu":
        draw_menu()

    if game_state == "game":

        draw_background()
        draw_dungeon(hero_condition)
        draw_title_rect()
        draw_character_rect()
        draw_message(current_message)

    pygame.display.flip()

pygame.quit()









