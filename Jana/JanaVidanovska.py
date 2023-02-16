import random
from copy import deepcopy

# задолжителена променлива, потполни ја со твои податоци
NAME = 'Јана Видановска'


def find_queen(state, queen_symbol):
    N = len(state)
    for y in range(N):
        for x in range(N):
            if state[y][x] == queen_symbol:
                return x, y


def possible_moves(state, x, y):
    N = len(state)
    deltas = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < N:
            if state[ny][nx] == '·':
                yield nx, ny
            else:
                break
            nx += dx
            ny += dy


def expand_state(state, symbol):
    qx, qy = find_queen(state, symbol)
    for mx, my in possible_moves(state, qx, qy):
        state_after_move = list([list(row) for row in state])
        state_after_move[my][mx] = symbol
        state_after_move[qy][qx] = '·'
        for sx, sy in possible_moves(state_after_move, mx, my):
            state_after_shot = deepcopy(state_after_move)
            state_after_shot[sy][sx] = 'x'
            state_after_shot = tuple([tuple(row) for row in state_after_shot])
            yield state_after_shot, (mx, my, sx, sy)


def other_queen_symbol(queen_symbol):
    return 'P' if queen_symbol == 'S' else 'S'


def check_victory(state, queen_to_move__symbol):
    queen_to_move__symbol
    qx, qy = find_queen(state, queen_to_move__symbol)
    if list(possible_moves(state, qx, qy)) == []:
        return other_queen_symbol(queen_to_move__symbol)
    return 'keep_playing'


def get_move_official(queue, state, symbol):
    """ Ова е официјалната функција која ќе биде повикана.

        НЕ МЕНУВАЈ НИШТО ВО ОВАА ФУНКЦИЈА.

        queue: multiprocessing.Queue
            Редица за да може да се проследи потегот до главниот процес.
        state: string
            Ова е моменталната состојба на таблата.
        symbol: str, {'S', 'P'}
            Ова е симболот на кралицата со која вие играте.

        Оваа функцијата не враќа податоци. Резултатот на играта треба да
        се запише во редицата `queue`. Структурата на одговорот е
        торка од две торки, една за новата позиција на кралицата,
        а другата за испуканото поле.
                        ((mx, my), (sx, sy))
        mx, my: се позициите на новата позиција на кралицата
        sx, sy: се позициите на испуканото поле

    """
    move = get_move(state, symbol)
    queue.put(move)
    

# _____________________________ MOJ DEL __________________________________________

# x-kolona y-redica
def can_reach_directly_evolved(goal_position, queen_position, state):
    gx, gy = goal_position
    qx, qy = queen_position
    if qy == gy:
        minx, maxx = (qx, gx) if qx < gx else (gx, qx)
        for x in range(minx+1, maxx):
            if state[qy][x] != '·':
                return False
        return True
    
    if qx == gx:
        miny, maxy = (qy, gy) if qy < gy else (gy, qy)
        for y in range(miny+1, maxy):
            if state[y][qx] != '·':
                return False
        return True
    
    if qx-qy == gx-gy: # na glavna dijagonala
        minx, maxx, miny = (qx, gx, qy) if qx < gx else (gx, qx, gy)
        for i in range(1, maxx-minx): # indekso odi pr od 0 do 5
            if state[miny+i][minx+i] != '·':
                return False
        return True
    
    if qx+qy == gx+gy: # na sporedna dijagonala
        minx, maxx, miny = (qx, gx, qy) if qx < gx else (gx, qx, gy)
        for i in range(1, maxx-minx): # indekso odi pr od 0 do 5
            if state[miny-i][minx+i] != '·':
                return False
        return True
    
    return False
    
def how_many_squares_in_one_move_evolved(state, queen_position):
    how_many = 0
    for row_index, row in enumerate(state):
        for col_index, element in enumerate(row):
            if element == '·':
                if can_reach_directly_evolved((col_index, row_index), queen_position, state):
                    how_many += 1
    return how_many
            

def mobility(state):
    s_position = find_queen(state, 'S')
    p_position = find_queen(state, 'P')
    s_mobility = how_many_squares_in_one_move_evolved(state, s_position)
    p_mobility = how_many_squares_in_one_move_evolved(state, p_position)
    return (s_mobility - p_mobility) / 19 # max ima do 19 polinja mobilnost
    # ako se naogja vo centarot na 6x6 board

    
def chebyshev(pos_1, pos_2):
    x1, y1 = pos_1
    x2, y2 = pos_2
    return max(abs(x1-x2), abs(y1-y2))

    
def who_owns_square(state, square_position):
    s_position = find_queen(state, 'S')
    p_position = find_queen(state, 'P')
    s_dist = chebyshev(s_position, square_position)
    p_dist = chebyshev(p_position, square_position)
    if s_dist == p_dist:
        return 0
    return 1 if s_dist < p_dist else -1

# Ne e precizno zosto ne zema vo predvid dali ima iksovci


def territory(state):
    score = 0
    how_many_squares = 0
    for row_index, row in enumerate(state):
        for col_index, element in enumerate(row):
            if element == '·':
                how_many_squares += 1
                score += who_owns_square(state, (col_index, row_index))
    return score / how_many_squares


def freedom_queen(state, symbol):
    N = len(state)
    how_many = 0
    x, y = find_queen(state, symbol)
    deltas = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and state[ny][nx] == '·':
            how_many += 1
            nx += dx
            ny += dy
    return how_many/8


def freedom(state):
    freedom_s = freedom_queen(state, 'S')
    freedom_p = freedom_queen(state, 'P')
    return freedom_s - freedom_p


def evaluate_state(state, symbol):
    return (3*mobility(state) + territory(state) + freedom(state)) / 5

# ________________________________________________________________________________ 


def get_move(state, symbol):
    other_symbol = 'S' if symbol == 'P' else 'P'
    player = 'MAX' if symbol == 'S' else 'MIN'
    minimax.scores = {symbol: 1, other_symbol: -1}
    result, move = minimax(state, player, symbol)
    return move


def minimax(state, player, symbol, alpha=-2, beta=2, depth=0):
    winner = check_victory(state, symbol)
    if winner != 'keep_playing':
        return minimax.scores[winner], None
    # пример како да се прекине со пребарување после длабочина 3
    if depth == 3:
        return evaluate_state(state, symbol), None
    best_value = 2 if player == 'MIN' else -2
    best_move = None
    for child, move in expand_state(state, symbol):
        other_player = 'MIN' if player == 'MAX' else 'MAX'
        other_symbol = 'S' if symbol == 'P' else 'P'
        result, _ = minimax(
            child, other_player, other_symbol, alpha, beta, depth+1)
        if player == 'MIN':
            if result <= alpha:
                return result, best_move
            if result < beta:
                beta = result
            if result < best_value:
                best_value = result
                best_move = move
        elif player == 'MAX':
            if result >= beta:
                return result, best_move
            if result > alpha:
                alpha = result
            if result > best_value:
                best_value = result
                best_move = move
    return best_value, best_move
