"""
Реализация движка консольной версии игры "Быки и коровы"

функции модуля:

check_number(number:str) -> bool - возвращает результат проверки на уникальность вхождения каждой
цифры в число number.

start_game(number) -> dict[str, int] - возвращает словарь с результатом проверки на схожесть загаданного числа и числа,
введенного пользователем.

is_gameover() -> bool - возвращает результат проверки на совпадение загаданного числа и числа, введенного пользователем

переменные модуля:

_result = {"bulls": 0, "cows": 0} - результирующий словарь, который возвращает результат очередного хода игрока

_hidden_number = str(randint(1000, 9999)) - случайно генерируемое число, которое необходимо отгадать пользователю

"""


from random import randint

_result = {"bulls": 0, "cows": 0}
_hidden_number = str(randint(1000, 9999))

def check_number(number):
    temp_lst = [0 if number[i] in number[i+1:] else 1 for i in range(0, len(number)-1)]
    return all(temp_lst)

while not check_number(_hidden_number):
    _hidden_number = str(randint(1000, 9999))

def start_game(number):

    global _result, _hidden_number
    _result = {"bulls": 0, "cows": 0}

    for i in range(len(_hidden_number)):
        if number[i] == _hidden_number[i]:
            _result["bulls"] += 1
        elif number[i] in _hidden_number:
            _result["cows"] += 1
    return _result

def is_gameover():
    return _result["bulls"] == 4

