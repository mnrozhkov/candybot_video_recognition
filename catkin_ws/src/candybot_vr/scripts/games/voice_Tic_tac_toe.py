import speech_recognizer as sr

X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9
 
def display_instr():
    print(
        """

         Добро пожаловать в игру 'Крестики-нолики'.
         Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соответсвуют полям доски - так, как показано ниже:
         0|1|2
         -----
         3|4|5
         -----
         6|7|8
         """
        )
 
def ask_yes_no(question):
    respone = None
    while respone not in ("да","нет"):
        respone = sr.listen()
    return respone

numbers = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8}

def ask_number(question, low, high):
    respone = None
    while respone not in range(low,high) or (not respone in number.keys()):
        print(question)
        respone = number[sr.listen()]
    return respone
 
def pieces():
    go_first = ask_yes_no("Хочешь сделать первый ход? (да/нет): ")
    if go_first == "да":
        print("Играй крестиками")
        human = X
        computer = O
    else:
        print("Хорошо,буду начинать я.")
        human = O
        computer = X
    return computer,human
 
def new_board():
    board=[]
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
 
def display_board(board):
    print("\n\t",board[0],"|",board[1],"|", board[2])
    print("\t","----------")
    print("\n\t",board[3],"|",board[4],"|", board[5])
    print("\t","----------")
    print("\n\t",board[6],"|",board[7],"|", board[8], "\n")
 
def legal_moves(board):
    moves=[]
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
 
def winner(board):
    WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    empty_count = 0
    #проверяем каждую строку, столбец и диагональ
    for row in WAYS_TO_WIN:
        #если есть 3 клетки подряд с одинаковым символом, то это символ победил
        if board[row[0]] == board[row[1]]==board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    #если нет победы, то считаем число пустых клеток
    for cell in range(0,9):
        if board[cell] == EMPTY:
            empty_count += 1
    #если пустых клеток не осталось, то ничья
    if empty_count == 0:
        return TIE
    return None
        
def human_move(board,human):
    legal = legal_moves(board)
    move = None
    while not move in legal:
        move = ask_number("Твой ход. Выбери поля (0-8):", 0, NUM_SQUARES)
        if not move  in legal:
            print("Это поле уже занято.")
        else:
            return move
 
def computer_move(board, computer, human):
    board = board[:]
    #приоритеты ходов компьютера
    BEST_MOVES=(4,0,2,6,8,1,3,5,7)
    print("Я выберу поле номер", end = " ")
    #сначала проверяем, есть ли у противника выигрышаный следующий ход
    for move in legal_moves(board):
        board[move]=human
        if winner(board) == human:
            print(move)
            #если такой ход есть (в одной из строк, столбцов или диагоналей
            #есть уже 2 символа противника), то препятствуем выигрышу противника -
            #ставим свой символ
            return move
        board[move] = EMPTY
    #если не существует следующего выигрышного хода противника,
    #то выбираем для хода певую незанятую клетку из приоритетных
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
 
 
def next_turn(turn):
    if turn==X:
        return O
    else:
        return X
 
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print("Три", the_winner, "в ряд")
    else:
        print("Ничья")
    if the_winner == computer:
        print("Победа за мной.")
    elif the_winner == human:
        print("Поздравляю,ты смог обойти меня.")


def main():
    sr.min_rms = 500
    if sr.init('ru-ru','TicTacToe.dic','TicTacToe.lm.bin'):
        display_instr()
        computer, human = pieces()
        turn = X
        board = new_board()
        display_board(board)
        while not winner(board):
            if turn == human:
                move = human_move(board,human)
                board[move]=human
            else:
                move = computer_move(board,computer,human)
                if not move is None:
                    board[move] = computer
            display_board(board)
            turn=next_turn(turn)
        the_winner = winner(board)
        congrat_winner(the_winner, computer, human)
 
if __name__ == '__main__':
    main()
