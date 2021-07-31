"""
Реализация клиентской части игры "Быки и коровы"
"""

from engine import check_number, is_gameover, start_game

attempt_count = 0

user_number = input('Hello! It is a game "Bulls and cows". Input your number in format XXXX, please: ')

while not is_gameover():

    if check_number(user_number) and len(user_number) == 4:
        result = start_game(user_number)
        if result["bulls"] != 4:
            attempt_count += 1
            print(f'bulls - {result["bulls"]}, cows - {result["cows"]}')
            user_number = input('Next attempt: ')
        else:
            print(f'This number is {user_number}! You are winner! Your attempt count is {attempt_count}. Game over, see you later, lucky!')
    else:
        num = input("Try again, but your number is not valid: ")