# Функция авторизации игрока
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
    from colorama import init
    init()
    from colorama import Fore, Back, Style
    print(Back.BLACK, Fore.GREEN, '  1   2   3')
    print('   -----------')
    for i in range(3):  # делаем итерацию от 0 до 3 ( в диапазоне от 0 до 2)
        print(Fore.GREEN, i + 1, end='|')
        for j in range(3):
            if board[i][j] == 'X':
                print(Fore.BLACK, Back.RED, board[i][j], end=''), print(Back.BLACK, Fore.GREEN, end='|')
            if board[i][j] == ' ':
                print(Fore.BLACK, Back.GREEN, board[i][j], end=''), print(Back.BLACK, Fore.GREEN, end='|')
            if board[i][j] == '0':
                print(Fore.BLACK, Back.YELLOW, board[i][j], end=''), print(Back.BLACK, Fore.GREEN, end='!')

        # print(i + 1, '|', ' | '.join(board[i]), '|')
        print()
        print(Back.BLACK, '   -----------')


# функция, которая позволяет сделать ход прнимает двумерный список и принимает имя Х или О,
# проверяет не занята ли ячейка
def ask_and_make_move(game_player_use, fig, board):
    x, y = 0, 0
    pl = game_player_use  # Какой игрок играет
    while not (1 <= x <= 3) or not (1 <= y <= 3):  # ждем корректные координаты от 1 до 3
        x = int(input(f"Игрок {pl} введите координату  для {fig} по горизонтали (От 1 до 3):"))
        y = int(input(f"Игрок {pl} введите координату для  {fig} по вертикали (От 1 до 3):"))
        if not (1 <= x <= 3) or not (1 <= y <= 3):
            print('Неверные координаты. Прошшу ввести от 1 до 3!')
        if 1 <= x <= 3 and 1 <= y <= 3 and board[x - 1][y - 1] == ' ':  # проверяем что клетка не пустая
            board[x - 1][y - 1] = fig  # Указать переменную о или икс будет входной можно тут два условия делать
        elif 1 <= x <= 3 and 1 <= y <= 3 and board[x - 1][y - 1] != ' ':
            print('Клетка занята, выберите другую!')
            ask_and_make_move(game_player_use, fig, board)
    return x, y


# Функция проверки выигрыша
def win_check(board, player_sequence, fig):
    if board[0][0] == board[1][1] == board[2][2] == fig:
        return 'win'
    if board[2][0] == board[1][1] == board[0][2] == fig:
        return 'win'
    board_t = [list(j) for j in zip(*board)]  # транспонируем массив чтобы проверить столбцы
    for i in range(3):  # делаем итерацию от 0 до 3 ( в диапазоне от 0 до 2)
        abc = (''.join(board[i]))  # объедияем ячейки и смотри строки на заполнение
        if abc == fig * 3:
            return 'win'
        abc = (''.join(board_t[i]))
        if abc == fig * 3:  # объедияем ячейки и смотрим столбцы на заполнение
            return 'win'
        if player_sequence == 9:  # проверка на ничью. Сделаны ли все ходы
            return 'nothing'
    return 'next'


while True:  # цикл игры пока не будет нажат выход из игры
    player_sequence = 0
    game_player = name_game_select()  # Начало игры. Получаем словарь с именем игрока
    fig = 'X'
    while win_check(board, player_sequence,
                    fig) == 'next':  # Цикл игры Пока игрок не вымграл. Функция проверки выигрыша
        if player_sequence % 2 == 0:  # Чередуем игрока
            game_player_use = game_player['name1']
            fig = 'X'
        else:
            game_player_use = game_player['name2']
            fig = '0'
        draw_board(board)  # Рисуем доску
        ask_and_make_move(game_player_use, fig, board)  # делаем ход и получаем массив с введеными данными
        player_sequence += 1  # Счетчик для подсчета ничьи и для чередования игрока
    draw_board(board)  # Рисуем доску итоговую
    if win_check(board, player_sequence, fig) == 'win':
        print(f'Игрок {game_player_use} победил. \nПоздравляю!!!')
    else:
        print('У ВАС НИЧЬЯ!!!')
    # спросить игроков, хотят ли они сыграть еще раз
    restart = input("Хотите сыграть еще раз? (y/n) ")
    if restart.lower() == 'y':
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # если да обнуляем доску
    if restart.lower() != "y":
        break
