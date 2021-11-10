#
# eight_puzzle.py
#
# driver/test code for state-space search on Eight Puzzles
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, depth_limit = -1, heuristic = None):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
            
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(depth_limit)
    elif algorithm == 'BFS':
        searcher = BFSearcher(depth_limit)
    elif algorithm == 'DFS':
        searcher = DFSearcher(depth_limit)
    elif algorithm =='Greedy':
        searcher = GreedySearcher(depth_limit, heuristic)
    elif algorithm =='A*':
        searcher = AStarSearcher(depth_limit, heuristic)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, depth_limit = -1, heuristic = None):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, depth_limit, heuristic)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
    
def process_file(filename, algorithm, depth_limit = -1, heuristic = None):
    """takes the following inputs
    filename - a string specifying the name of a text file in which each line is a digit string for an eight puzzle.
    algorithm - a string that specifies which state-space search algorithm should be used to solve the puzzles ('random', 'BFS', 'DFS', 'Greedy', or 'A*')
    depth_limit - an integer that can be used to specify an optional parameter for the depth limit
    heuristic - an optional parameter which will be used to pass in a reference to the heuristic function to use.
    """
    
    file = open(filename, 'r')
    data = []
    with file as topo_file:
        for line in topo_file:
            data += [line.strip()]
    file.close()
    moves = []
    states = []
    puzzlenumber = 0
    term = ''
    for puzzle in data:
        init_board = Board(puzzle)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, depth_limit, heuristic)
        soln = None
        try:
            soln = searcher.find_solution(init_state)
        except KeyboardInterrupt:
            soln = None
            term = 'search terminated,'
        if soln != None:
            puzzstring = '%s: %d moves, %d states tested' % (puzzle, soln.num_moves, searcher.num_tested)
            puzzlenumber += 1
        else:
            if term == 'search terminated,':
                puzzstring = '%s: %s no solution' % (puzzle, term)
            else:
                puzzstring = '%s: no solution' % (puzzle)
            print(puzzstring)
            continue
        moves.append(soln.num_moves)
        states.append(searcher.num_tested)
        
        print(puzzstring)
    if len(moves) > 0 and len(states) > 0:
        avgmoves = sum(moves) / len(moves)
        avgstates = sum(states) / len(states)
    print()
    print('solved %d puzzles' % (puzzlenumber))
    if puzzlenumber > 0:
        print('averages: %g moves, %g states tested' % (avgmoves, avgstates))


