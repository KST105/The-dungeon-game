from scr import inventory as inv

def print_massage(massage):
    return print(massage)

def meeting_with_enemy(enemy):
    massage = f"While exploring another dungeon room too carelessly, you attracted too much attention. {enemy} has spotted you and is preparing for battle."
    return massage

def hp_recovery(hp):
    massage = f"Нou have restored 3 hp. You have {str(hp)} health points."
    return massage

def receiving_damage(dm, hp):
    massage = f"You took {str(dm)} damage. You have {str(hp)} health points."
    return massage

def taking_damage_opponent(dm, hp, enemy):
    massage = f"You have dealt damage of {str(dm)}. {enemy} health points of {str(hp)}."
    return massage

massage_choose_tactics = "Choose your battle tactics for the next turn. (attack / defense)"

massage_select_attack = "Select attack type (melee/range/magic)"

massage_select_defense = "Select parry type (melee/range/magic)"

massage_beginnin_battle = "The battle begins..."

massage_repeat_visit = "Have you visited this hall yet"

massage_repeat_research = "Have you explored this hall yet"