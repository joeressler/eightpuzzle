#
# searcher.py (ps18)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """ constructs a searcher with depth_limit 'depth_limit'
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def should_add(self, state):
        """ returns False if a state's num_moves is greater
        than the depth limit or if the state creates a cycle
        and True otherwise.
        """
        if self.depth_limit != -1:
            if state.num_moves > self.depth_limit:
                return False
            elif state.creates_cycle():
                return False
            else:
                return True
        else:
            if state.creates_cycle():
                return False
            else:
                return True

    def add_state(self, new_state):
        """ adds state 'new_state' to self.states
        """
        self.states.append(new_state)   
    
    def add_states(self, new_states):
        """evaluates all states in list new_states and
        adds them to self.states if they should be added.
        """
        for s in new_states:
            if self.should_add(s):
                self.add_state(s)
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        self.add_states([init_state])
        while len(self.states) > 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal():
                return s
            s1 = s.generate_successors()
            self.add_states(s1)
        return None


### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):

    def next_state(self):
        s = self.states[0]
        self.states.remove(s)
        return s
    

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###
