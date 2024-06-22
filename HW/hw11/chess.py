# 使用chatGPT生成

import copy

# 棋盤初始狀態
initial_board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

# 簡單的評估函數
def evaluate(board):
    piece_values = {
        'K': 1000, 'Q': 9, 'R': 5, 'B': 3, 'N': 3, 'P': 1,
        'k': -1000, 'q': -9, 'r': -5, 'b': -3, 'n': -3, 'p': -1
    }
    value = 0
    for row in board:
        for piece in row:
            if piece in piece_values:
                value += piece_values[piece]
    return value

# 生成所有合法移動（這裡只實現基本移動邏輯）
def generate_legal_moves(board, color):
    moves = []
    for i in range(8):
        for j in range(8):
            if (color == 'white' and board[i][j].isupper()) or (color == 'black' and board[i][j].islower()):
                moves += generate_piece_moves(board, i, j)
    return moves

# 生成單個棋子的合法移動（這裡只實現兵的基本移動邏輯）
def generate_piece_moves(board, x, y):
    piece = board[x][y]
    moves = []
    if piece == 'P':
        if x > 0 and board[x-1][y] == '.':
            moves.append((x, y, x-1, y))
        if x == 6 and board[x-2][y] == '.':
            moves.append((x, y, x-2, y))
    elif piece == 'p':
        if x < 7 and board[x+1][y] == '.':
            moves.append((x, y, x+1, y))
        if x == 1 and board[x+2][y] == '.':
            moves.append((x, y, x+2, y))
    return moves

# 應用移動
def apply_move(board, move):
    new_board = copy.deepcopy(board)
    x1, y1, x2, y2 = move
    new_board[x2][y2] = new_board[x1][y1]
    new_board[x1][y1] = '.'
    return new_board

# Minimax 算法
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0:
        return evaluate(board), None

    legal_moves = generate_legal_moves(board, 'white' if maximizing_player else 'black')
    if not legal_moves:
        return evaluate(board), None

    best_move = None
    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            new_board = apply_move(board, move)
            eval, _ = minimax(new_board, depth-1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in legal_moves:
            new_board = apply_move(board, move)
            eval, _ = minimax(new_board, depth-1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# 主程序
def play_game():
    board = initial_board
    while True:
        print_board(board)
        eval, move = minimax(board, 3, float('-inf'), float('inf'), True)
        if move:
            board = apply_move(board, move)
        else:
            print("White wins!" if eval > 0 else "Black wins!")
            break
        print_board(board)
        eval, move = minimax(board, 3, float('-inf'), float('inf'), False)
        if move:
            board = apply_move(board, move)
        else:
            print("White wins!" if eval > 0 else "Black wins!")
            break

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

play_game()
