import pygame
from scr import gamelogic_lower as gl_l
from scr.gamelogic_lower import *
from scr.massages_player import *

pygame.init()

pygame.display.set_caption("Dungeon Explorer")

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
AVAILABLE_MAP_HEIGHT = SCREEN_HEIGHT * 4 // 5
AVAILABLE_MAP_WIDTH = SCREEN_WIDTH * 3 // 5
CELL_SIZE = min(AVAILABLE_MAP_WIDTH // count_hall, AVAILABLE_MAP_HEIGHT // count_floor)
HEIGHT_INDENT_MAP = 100
INDENT_HEIGHT_MASSAGE = 30
INDENT_WIDTH_MAP = (SCREEN_WIDTH // 5 * 3 - CELL_SIZE * count_hall) // 2
current_message = "Добро пожаловать в подземелье!"

MAP_X = INDENT_WIDTH_MAP
MAP_Y = HEIGHT_INDENT_MAP
WIDTH_MAP = CELL_SIZE * count_hall
HEIGHT_MAP = CELL_SIZE * count_floor

map_rect = pygame.Rect(MAP_X, MAP_Y, WIDTH_MAP, HEIGHT_MAP)

MASSAGE_X = map_rect.left
MASSAGE_Y = map_rect.height + HEIGHT_INDENT_MAP + INDENT_HEIGHT_MASSAGE
WIDTH_MASSAGE = map_rect.width
HEIGHT_MASSAGE = (SCREEN_HEIGHT - HEIGHT_MAP - HEIGHT_INDENT_MAP ) / 2

message_rect = pygame.Rect(MASSAGE_X, MASSAGE_Y, WIDTH_MASSAGE, HEIGHT_MASSAGE+20)

CHARACTER_X = map_rect.right + INDENT_WIDTH_MAP
CHARACTER_Y = map_rect.top
WIDTH_CHARACTER = SCREEN_WIDTH - map_rect.width - INDENT_WIDTH_MAP*3
HEIGHT_CHARACTER = SCREEN_HEIGHT - HEIGHT_INDENT_MAP - INDENT_HEIGHT_MASSAGE

character_rect = pygame.Rect(CHARACTER_X, CHARACTER_Y, WIDTH_CHARACTER , HEIGHT_CHARACTER + 20)

TITLE_X = INDENT_WIDTH_MAP
TITLE_Y = 0
WIDTH_TITLE = WIDTH_MAP + WIDTH_CHARACTER + (character_rect.left - map_rect.right)
HEIGHT_TITLE = HEIGHT_INDENT_MAP - INDENT_HEIGHT_MASSAGE

title_rect = pygame.Rect(INDENT_WIDTH_MAP, TITLE_Y, WIDTH_TITLE, HEIGHT_TITLE)

CHARACTER_CONTROL_Y = character_rect.y + character_rect.height * 2/3
CHARACTER_INFO_HEIGHT =  character_rect.height * 2/3

font = pygame.font.Font("textures\GothicFont.ttf", 35)
font_massage = pygame.font.Font("textures\GothicFont.ttf", 20)

hero_condition = "up"

def draw_dungeon(condition="up"):

    for floor in range(count_floor):
        for hall in range(count_hall):

            x = map_rect.x + hall * CELL_SIZE
            y = map_rect.y + floor * CELL_SIZE

            cell = gl_l.game_map[floor][hall]

            if cell == "#":
                screen.blit(wall_destructible, (x, y))

            elif cell == "?":
                screen.blit(floor_unexplored, (x, y))

            elif cell == "*":
                screen.blit(wall_undestructible, (x, y))

            elif cell == "B":
                screen.blit(chest, (x, y))

            elif cell == "Ш":
                screen.blit(trap, (x, y))

            elif cell == "H":
                screen.blit(hero_textures[condition], (x, y))

            else:
                screen.blit(floor_explored, (x, y))

            pygame.draw.rect(screen,(0, 0, 7),(x, y, CELL_SIZE, CELL_SIZE),1,10)

def draw_message(current_message):

    if current_message == None:
        current_message = ""

    pygame.draw.rect(screen, (35, 35, 35), message_rect)

    lines = current_message.split("\n")

    y = message_rect.y + 4

    for line in lines:
        text_surface = font_massage.render(line,True,(255, 255, 255))

        screen.blit(text_surface,(message_rect.x + 10, y))

        y += font_massage.get_linesize()

def draw_character_rect():

    text_character_info = f"hp: {str(inv.hp)}\n\nwariness: {str(inv.counter_scan)} out of {str(inv.max_counter_scan)}\n\ndamage: {str(inv.damage)}\n\n"

    text_character_inventory = f"health potion: {str(inv.health_potion)}\n\npower potion: {str(inv.power_potion)}\n\nkey: {str(inv.key)}"

    pygame.draw.rect(screen,(35, 35, 35), character_rect)

    text_control = font.render(text_control_key,True,(255, 255, 255))
    screen.blit(text_control,(character_rect.x + 30, CHARACTER_CONTROL_Y + 30))
    pygame.draw.rect(screen, (20, 20, 20), (character_rect.x, CHARACTER_CONTROL_Y, character_rect.width, character_rect.height * 1/3 + 1), 1)

    text_character = font.render(text_character_info, True, (255, 255, 255))
    screen.blit(text_character, (character_rect.x + 30, character_rect.y + 30))
    pygame.draw.rect(screen, (20, 20, 20),(character_rect.x, character_rect.y, character_rect.width / 2, CHARACTER_INFO_HEIGHT), 1)

    text_character_inv = font.render(text_character_inventory, True, (255, 255, 255))
    screen.blit(text_character_inv, (character_rect.x + (character_rect.width / 2) + 30, character_rect.y + 30))
    pygame.draw.rect(screen, (20, 20, 20),(character_rect.x + (character_rect.width / 2), character_rect.y, character_rect.width / 2 + 1, CHARACTER_INFO_HEIGHT), 1)

def draw_title_rect():
    pygame.draw.rect(screen,(35, 35, 35), title_rect)

    text_surface = font.render("KeyFinder",True,(255, 255, 255))

    screen.blit(text_surface,(title_rect.x + WIDTH_TITLE / 2 - text_surface.width / 2 , title_rect.y + HEIGHT_TITLE / 2 - text_surface.height / 2 ))

def draw_menu():

    screen.blit(menu_background, (0, 0))

    text_menu = f"Play \n\nExit"

    title = font.render("KeyFinder", True, (255, 255, 255))
    start_text = font.render(text_menu, True, (255, 255, 255))

    screen.blit(title,(SCREEN_WIDTH // 2 - title.get_width() // 2, 200))

    screen.blit(start_text,(SCREEN_WIDTH // 2 - start_text.get_width() // 2, 500))

def draw_background():

    screen.blit(game_background, (0, 0))

game_background = pygame.image.load("textures/title_game.png").convert()
game_background = pygame.transform.scale(game_background,(SCREEN_WIDTH, SCREEN_HEIGHT))

menu_background = pygame.image.load("textures/title_menu.png").convert()
menu_background = pygame.transform.scale(menu_background,(SCREEN_WIDTH, SCREEN_HEIGHT))

floor_unexplored = pygame.image.load("textures/floor_unexplored.png").convert()
floor_explored = pygame.image.load("textures/floor_explored.png").convert()
wall_destructible = pygame.image.load("textures/wall_destructible.png").convert()
wall_undestructible = pygame.image.load("textures/wall_undestructible.png").convert()
trap = pygame.image.load("textures/trap.png").convert()
chest = pygame.image.load("textures/chest.png").convert()

hero_up = pygame.image.load("textures/character_up.png").convert()
hero_down = pygame.image.load("textures/character_down.png").convert()
hero_left = pygame.image.load("textures/character_left.png").convert()
hero_right = pygame.image.load("textures/character_right.png").convert()

hero_textures = {"up": hero_up, "down": hero_down, "left": hero_left, "right": hero_right}

