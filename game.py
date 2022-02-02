'''Implements the logic for the game Reversi, based on the "Othello"
version trademarked by Mattel.'''
"""
Haolin Ye
420-LCU Computer Programming
R. Vincent , instructor
"""
from board import *

HUMAN = 1
COMPUTER = 2

def game_start():
    '''Create and initialize the game data.

    Returns a properly initialized board object.
    '''
    # Create a board object.
    board = board_create()
    # Set up the initial board configuration for Reversi.
    board_put(board, 3, 3, COMPUTER)
    board_put(board, 4, 4, COMPUTER)
    board_put(board, 3, 4, HUMAN)
    board_put(board, 4, 3, HUMAN)
    # Return the newly-created board object.
    return board

def game_turn(board, row, col):
    '''
    board (list): an object returned by board_create()
    row (int): The row coordinate where the piece should be placed.
    col (int): The column coordinate where the piece should be placed.

    Place the human player's piece on the board at the coordinates 
    row, col.

    If the move is not legal, this function will return False.

    If the move is legal, this function will 'flip over' all of the opponent's
    pieces affected by this move.

    It will then allow the computer player to choose and perform a move, 
    turning over all of the human player's affected pieces.
    '''
    if _is_legal_move(board, row, col, HUMAN):
        # Perform the human player's chosen move.
        board_put(board, row, col, HUMAN)
        _do_flips(board, row, col, HUMAN)
        while True:
            moves = _get_legal_moves(board, COMPUTER)
            if len(moves) > 0:
                row, col = _choose_move(board, moves, COMPUTER)
                board_put(board, row, col, COMPUTER)
                _do_flips(board, row, col, COMPUTER)
            else:
                break
            # See if the human has any legal moves left.
            moves = _get_legal_moves(board, HUMAN)
            if len(moves) > 0:
                break
        return True
    else:
        return False


def game_over(board):
    return not (len(_get_legal_moves(board,HUMAN)) or len(_get_legal_moves(board,COMPUTER)))
    #return True if both COM and HUM do not have any legal move

def game_winner(board):
    if board_count(board, HUMAN) > board_count(board, COMPUTER):
    #if Human player has more pieces than the Computer
        return HUMAN
    elif board_count(board, HUMAN) < board_count(board, COMPUTER):
    #if COMPUTER has more pieces than the HUMAN 
        return COMPUTER
    #if game ends in a tie, return 0
    else:
        return 0

def _get_opponent(player):
    '''
    player (int): HUMAN or COMPUTER
    
    Returns the opponent of the given player.
    '''
    if player == HUMAN:
        return COMPUTER
    else:
        return HUMAN

def _get_flips(board, r0, c0, player, opponent):
    '''
    board (list): an object returned from board_create()
    r0 (int): row number of the proposed move.
    c0 (int): column number of the proposed move.
    player (int): HUMAN or COMPUTER
    opponent (int): COMPUTER or HUMAN
    
    Returns a list of pieces that would change color if the player
    moves to position r0,c0.

    The algorithm here just starts at the r0,c0 position and searches
    along each of the eight directions for possible pieces to flip.
    '''
    # Reflects the 8 directions relative to a board position.
    deltas = (( 1, 0), (-1, 0), ( 0, 1), ( 0,-1),
              (-1,-1), ( 1, 1), (-1, 1), ( 1,-1))
    result = []
    n_rows = board_rows(board)
    n_cols = board_cols(board)
    for dr, dc in deltas:
        row = r0 + dr
        col = c0 + dc
        if 0 <= row < n_rows and 0 <= col < n_cols:
            if board_get(board, row, col) == opponent:
                # Start assembling possible flips
                possible = [(row, col)]
                while 0 <= row < n_rows and 0 <= col < n_cols:
                    row += dr
                    col += dc
                    if board_get(board, row, col) == opponent:
                        possible += [(row, col)]
                    elif board_get(board, row, col) == player:
                        # If we found one of our anchor pieces, everything
                        # up to this position will flip, so this should
                        # be saved in the result list.
                        result += possible
                        break
                    else:
                        # No anchor piece found, so we won't flip anything
                        # along this direction.
                        break
    return result

def _is_legal_move(board, row, col, player):
    '''
    board (list): an object created by board_create()
    row (int): the row coordinate of the proposed move.
    col (int): the column coordinate of the proposed move.
    player (int): HUMAN or COMPUTER

    Return True if a given move is legal.
    '''
    if board_get(board, row, col): # Square is occupied.
        return False
    opponent = _get_opponent(player)
    flips = _get_flips(board, row, col, player, opponent)
    return len(flips) != 0      # A move must flip at least one piece.

def _do_flips(board, row, col, player):
    '''
    board (list): an object created by board_create()
    row (int): the row coordinate of the proposed move.
    col (int): the column coordinate of the proposed move.
    player (int): HUMAN or COMPUTER

    Flip all of the appropriate pieces in response to a move.

    Returns None
    '''
    opponent = _get_opponent(player)
    for rp, cp in _get_flips(board, row, col, player, opponent):
        board_put(board, rp, cp, player)
    
def _get_legal_moves(board, player):
    '''
    board (list): an object created by board_create()
    player (int): HUMAN or COMPUTER

    Return a list containing all of the possible legal moves for this 
    player. A move is represented as a tuple of integers of the form
    (row, col).'''
    result = []
    for row in range(board_rows(board)):
        for col in range(board_cols(board)):
            if _is_legal_move(board, row, col, player):
                result += [(row, col)]
    return result
# The COMP AI
def _choose_move(board, moves, player):
    c_move = None
    lis_flips = []
    for row,col in moves:
        lis_flips.append(len(_get_flips(board, row, col, COMPUTER, HUMAN)))
    max_flip = lis_flips.index(max(lis_flips)) 
    #if COMPUTER gets on top of HUMAN which COMPUTER has more pieces than HUMAN, it wants to end the game as soon as possible.
    #COM will choose the move that can minimize the moves for HUM.
    if board_count(board,COMPUTER) > board_count(board,HUMAN):
        lis_legal = [] 
        n_legal = 0 
        for row,col in moves:
            c = board_copy(board) #define c to be a new copy of the board every time to keep the initial game board unchanged
            board_put(c, row, col, COMPUTER) #put the move on the copy to see how many legal moves will be left to HUMAN
            n_legal = len(_get_legal_moves(c,HUMAN)) #compute the number of legal moves of HUMAN
            lis_legal.append(n_legal)  
        min_legal =lis_legal.index(min(lis_legal)) # find the index of the move which will lead to a situation where HUM has the least legal moves
        c_move = moves[min_legal] 
    else: #when COMPUTER is losing the game, it wants to choose the move which can do most flips to catch up.
        c_move = moves[max_flip] #used the index found at the beginning to find the move which can do the most flips.
    return c_move 
    
    

# When running standalone, run a few tests of the provided functions.

if __name__ == "__main__":
    print("Testing the game logic.")
    from random import randint
    # Play ten randomized games and make sure nothing breaks.
    for trial in range(10):
        board = game_start()
        moves = _get_legal_moves(board, HUMAN)
        assert len(moves) == 4
        assert (2, 3) in moves
        assert (3, 2) in moves
        assert (4, 5) in moves
        assert (5, 4) in moves

        assert not game_over(board)

        assert game_turn(board, 3, 2)

        # Now play a game automatically.
        n_turns = 1
        while not game_over(board):
            moves = _get_legal_moves(board, HUMAN)
            if len(moves) > 0:
                assert all(_is_legal_move(board, r, c, HUMAN) for r, c in moves)
                # Select move at random.
                move = moves[randint(0, len(moves) - 1)]
                assert game_turn(board, *move)
            assert n_turns < 64 # avoid possible infinite loop
            n_turns += 1

        n_h = board_count(board, HUMAN)
        n_c = board_count(board, COMPUTER)
        print("Trial game ends with:", n_h, n_c)
        if n_h > n_c:
            assert game_winner(board) == HUMAN
        elif n_h < n_c:
            assert game_winner(board) == COMPUTER
        else:
            assert game_winner(board) == 0

    print("All tests passed.")
