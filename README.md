# Python_TelegremBot_Alisultanov
Проект: Telegram-бот с функцией календаря
Магомед Алисултанов
Magus80
alisultanov@mail.ru

# Функция авторизации игрока и назначение  X или 0
def name_game_select():
    player1 = player2 = ''
    # Вводим имена и проверяем чтобы не было пустого  имени и не были похожими.
    while player1 == player2 or player1.strip() == '' or player2.strip() == '':
        print('Имя не может быть пустым и не может быть похожим!')
        player1 = input('Введите имя первого игрока:')
        player2 = input('Введите имя второго игрока:')
    else:
        print(f'Игрок {player1} начинает и ходит "Крестиком"')
        print(f'Игрок {player2} ходит вторым  "Ноликом"')
        return dict(name1=player1, name2=player2, )


# Функция "Рисуем доску 3 на 3
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def draw_board(board):
    print('    1   2   3')
    print('  --------------')
    for i in range(3):  # делаем итерацию от 0 до 3 ( в диапазоне от 0 до 2)
        print(i + 1, '|', ' | '.join(board[i]), '|')
        print('  --------------')


# функция, которая позволяет сделать ход прнимает двумерный список и принимает имя Х или О,
# проверяет не занята ли ячейка
def ask_and_make_move(game_player_use, fig, board):
    x = 0
    y = 0
    pl = game_player_use  # поменять на переменную какой игрок можно тут на входе указать
    while not (1 <= x <= 3) or not (1 <= y <= 3):  # ждем корректные координаты от 1 до 3
        x = int(input(f"Игрок {pl} введите координату  для {fig} по горизонтали (От 1 до 3):"))
        y = int(input(f"Игрок {pl} введите координату для  {fig} по вертикали (От 1 до 3):"))
        if not (1 <= x <= 3) or not (1 <= y <= 3):
            print('Неверные координаты. Прошшу ввести от 1 до 3!')
        if 1 <= x <= 3 and 1 <= y <= 3 and board[x - 1][y - 1] == ' ':  # проверяем что клетка не пустая
            board[x - 1][y - 1] = fig  # Указать переменную о или икс будет входной можно тут два условия делать
        else:
            x, y = 0, 0
            print('Клетка занята, выберите другую!')
            continue
    return x, y


# Функция проверки выигрыша
def win_check(board):
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        return 'win'
    if board[0][0] == board[1][1] == board[2][2] == '0':
        return 'win'
    if board[2][0] == board[1][1] == board[0][2] == 'Y':
        return 'win'
    if board[2][0] == board[1][1] == board[0][2] == '0':
        return 'win'
    board_t = [list(j) for j in zip(*board)]  # транспонируем массив чтобы проверить столбцы
    for i in range(3):  # делаем итерацию от 0 до 3 ( в диапазоне от 0 до 2)
        abc = (''.join(board[i]))  # объедияем ячейки и смотри строки на заполнение
        if abc == 'XXX' or abc == '000':
            return 'win'
        abc = (''.join(board_t[i]))
        if abc == 'XXX' or abc == '000':  # объедияем ячейки и смотрим столбцы на заполнение
            return 'win'


# цикл игры пока не будет условие выигрыша.
player_sequence = 2
# name_game_select()
game_player = name_game_select()  # Начало игры. Получаем словарь с именем игрока

while win_check(board) != 'win':  # Пока игрок не вымграл. Функция проdерки выигрыша
    if player_sequence % 2 == 0:
        player_name = game_player['name1']
        fig = 'X'
    else:
        player_name = game_player['name2']
        fig = '0'

    print(player_name, fig)
    draw_board(board) # Рисуем доску
    ask_and_make_move(player_name, fig, board)  # делаем ход и получаем массив с введеными данными
    player_sequence += 1

print('-------------------------------------------')
print(f'Игрок {player_name} победил. \nПоздравляю!')
print('-------------------------------------------')
