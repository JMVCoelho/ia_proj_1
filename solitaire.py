#Francisco Santos - 87658 ; Joao Coelho - 86448
#GROUP 72

#ARTIFICIAL INTELIGENCE - 1ST ASSIGNMENT
#Peg Solitaire



#IMPORTS
from search import *
from utils import *


#ADT content
def c_peg():
    return "O"

def c_empty():
    return "_"

def c_blocked():
    return "X"

def is_empty(e):
    return e == c_empty()

def is_peg(e):
    return e == c_peg()

def is_blocked(e):
    return e == c_blocked()
#__________________________

#ADT pos
#Tuple (l, c)
def make_pos(l,c):
    return (l,c)

def pos_l(pos):
    return pos[0]

def pos_c(pos):
    return pos[1]
#__________________________


#ADT move
#List [p_initial, p_final]
def make_move(i, f):
    return [i, f]

def move_initial(move):
    return move[0]

def move_final(move):
    return move[1]
#___________________________

#ADT board
#List of lists [[entry1, entry2,..., entryN],[...],...,[...]]
def board_line(board,i): #get line i, i starts at 0
    return board[i]

def entry_from_line(board,i,x): #get entry x, from line i (i starts at 0)
    return board_line(board,i)[x]

def board_column(board,j): #get column j, j starts at 0
    line_size = len(board)
    
    line = []
    for i in range(line_size):
        line.append(entry_from_line(board,i,j))
    
    return line

def entry_from_column(board, j, x): #get entry x from column j. x,j start at 0.
    return board_coulmn(board,j)[x]
   

def set_entry(board, l, c, x): #dont use with the original board
    board[l][c] = x
    return board

def get_entry(board, l, c):
    return board[l][c]

def is_goal(board): #checks wheter or not a board only has one peg.
    numberOfPegs = 0
    for line in board:
        for entry in line:
            if is_peg(entry):
                numberOfPegs += 1;
    
    if numberOfPegs == 1:
        return True
    else:
        return False

def board_moves(board): #returns all the possible moves for a specific board
    moves = []
    for line_index, line in enumerate(board):
        for entry_index, entry in enumerate(line):
            if is_empty(entry):
                if(entry_index+2 <= len(line)-1 and is_peg(entry_from_line(board,line_index,entry_index+2)) and is_peg(entry_from_line(board,line_index,entry_index+1))):
                    initial_pos = make_pos(line_index, entry_index+2)
                    final_pos = make_pos(line_index, entry_index)
                    move = make_move(initial_pos,final_pos)
                    moves.append(move)
                    
                if(entry_index-2 >= 0 and is_peg(entry_from_line(board,line_index,entry_index-2)) and is_peg(entry_from_line(board,line_index,entry_index-1))):
                    initial_pos = make_pos(line_index, entry_index-2)
                    final_pos = make_pos(line_index, entry_index)
                    move = make_move(initial_pos,final_pos)
                    moves.append(move)
                    
                if(line_index+2 <= len(board)-1 and is_peg(entry_from_line(board, line_index+2, entry_index)) and is_peg(entry_from_line(board, line_index+1, entry_index))):
                    initial_pos = make_pos(line_index+2, entry_index)
                    final_pos = make_pos(line_index, entry_index)
                    move = make_move(initial_pos,final_pos)
                    moves.append(move)
                    
                if(line_index-2 >= 0 and is_peg(entry_from_line(board, line_index-2, entry_index)) and is_peg(entry_from_line(board, line_index-1, entry_index)) ):
                    initial_pos = make_pos(line_index-2, entry_index)
                    final_pos = make_pos(line_index, entry_index)
                    move = make_move(initial_pos,final_pos)
                    moves.append(move)
    return moves


def board_perform_move(board, move): #performs a chosen move. original board is preserved.
    new_board = [line[:] for line in board]
    
    initial = move_initial(move)
    initial_line = pos_l(initial)
    initial_column = pos_c(initial)
    
    new_board = set_entry(new_board, initial_line, initial_column, c_empty())
    
    final = move_final(move)
    final_line = pos_l(final)
    final_column = pos_c(final)
    
    new_board = set_entry(new_board, final_line, final_column, c_peg())
    
    
    if initial_line == final_line:
        if initial_column < final_column:
            new_board = set_entry(new_board, final_line, final_column-1, c_empty())
            
        elif initial_column > final_column:
            new_board = set_entry(new_board, final_line, final_column+1, c_empty())
            
    elif initial_column == final_column:
        if initial_line < final_line:
            new_board = set_entry(new_board, final_line-1, final_column, c_empty())
            
        elif initial_line > final_line:
            new_board = set_entry(new_board, final_line+1, final_column, c_empty())
    
    return new_board


def get_x_neighbours(board): #gets the number of X surrounding each peg, taking diagonals into account. 
    x_neighbours = 0
    for line_index, line in enumerate(board):
        for entry_index, entry in enumerate(line):
            if is_peg(entry):
                if entry_index+1 <= len(line)-1 and is_blocked(entry_from_line(board,line_index,entry_index+1)):
                    x_neighbours += 1
                if entry_index-1 >= 0 and is_blocked(entry_from_line(board,line_index,entry_index-1)):
                    x_neighbours += 1
                if line_index+1 <= len(board)-1 and is_blocked(entry_from_line(board,line_index+1,entry_index)):
                    x_neighbours += 1
                if line_index-1 >= 0 and is_blocked(entry_from_line(board,line_index-1,entry_index)):
                    x_neighbours += 1
                
                if entry_index+1 <= len(line)-1 and line_index-1 >= 0 and is_blocked(entry_from_line(board,line_index-1,entry_index+1)):
                    x_neighbours += 1
                if entry_index-1 >= 0 and line_index-1 >= 0 and is_blocked(entry_from_line(board,line_index-1,entry_index-1)):
                    x_neighbours += 1
                if entry_index+1 <= len(line)-1 and line_index+1 <= len(board)-1 and is_blocked(entry_from_line(board,line_index+1,entry_index+1)):
                    x_neighbours += 1
                if entry_index-1 >= 0 and line_index+1 <= len(board)-1 and is_blocked(entry_from_line(board,line_index+1,entry_index-1)):
                    x_neighbours += 1
    return x_neighbours


def get_wall_and_corner_pegs(board): #gets the number of pegs in corners and next to a limit.
    wallPegs = 0
    cornerPegs = 0
    
    upper_line = board_line(board, 0)
    for i in upper_line[1:-1]:
        if is_peg(i):
            wallPegs+=1
    
    lower_line = board_line(board, len(board)-1)
    for i in lower_line[1:-1]:
        if is_peg(i):
            wallPegs+=1
    
    left_column = board_column(board, 0)
    for i in left_column[1:-1]:
        if is_peg(i):
            wallPegs+=1
    
    right_column = board_column(board, len(upper_line)-1)
    for i in right_column[1:-1]:
        if is_peg(i):
            wallPegs+=1
    
    
    top_left_corner = make_pos(0,0)
    entryTL = get_entry(board, pos_l(top_left_corner), pos_c(top_left_corner))
    if is_peg(entryTL):
        cornerPegs+=1
        
    bot_left_corner = make_pos(len(board)-1,0)
    entryBL = get_entry(board, pos_l(bot_left_corner), pos_c(bot_left_corner))
    if is_peg(entryBL):
        cornerPegs+=1    
    
    top_right_corner = make_pos(0,len(upper_line)-1)
    entryTR = get_entry(board, pos_l(top_right_corner), pos_c(top_right_corner))
    if is_peg(entryTR):
        cornerPegs+=1 
        
    bot_right_corner = make_pos(len(board)-1,len(upper_line)-1)
    entryBR = get_entry(board, pos_l(bot_right_corner), pos_c(bot_right_corner))
    if is_peg(entryBR):
        cornerPegs+=1  
        
    return wallPegs, cornerPegs
#_____________________________________________________________________________#

class sol_state:
    
    def __init__(self, board):
        #each state is initialized with a board
        self.board = board
        
    def __lt__(self, other):
        # self < other : if other has more empty spaces its true.
        selfSpaces = 0
        otherSpaces= 0
        for line in self.board:
            for entry in line:
                if is_empty(entry):
                    selfSpaces += 1
        
        for line in other.board:
            for entry in line:
                if is_empty(entry):
                    otherSpaces += 1    
        return selfSpaces < otherSpaces

class solitaire(Problem):
    """Models a solitaire problem as a satisfaction problem.
       A solution cannot have more than 1 peg on the board."""
    
    def __init__(self, board):
        #initial board state.
        self.initial = sol_state(board)
        
    def actions(self, state):
        #returns list of possible moves
        return board_moves(state.board)
    
    def result(self, state, action):
        #preforms the move chosen from the list returned by actions.
        return sol_state(board_perform_move(state.board, action))
    
    def goal_test(self, state):
        #tests wheter or not the state board is goal
        return is_goal(state.board)
    
    def path_cost(self, c, state1, action, state2):
        #all solutions will have the same path cost. nonetheless, the cost is incremented by 1 every time we take a path down the search tree 
        return c+1
    
    def h(self, node):
        #heuristic function for informed searches
        numberOfXNeighbours = get_x_neighbours(node.state.board)
        numberOfWallPegs, numberOfCornerPegs = get_wall_and_corner_pegs(node.state.board)
        
        h_value = numberOfXNeighbours*1 + numberOfWallPegs*3 + numberOfCornerPegs*6
        return h_value