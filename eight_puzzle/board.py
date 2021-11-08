#
# board.py (ps17pr1)
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1   
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = int(digitstr[3 * r + c])
                if self.tiles[r][c] == 0:
                    self.blank_r = r
                    self.blank_c = c

        

    ### Add your other method definitions below. ###
    def __repr__(self):
        """Represents self
        """
        s = ''         # begin with an empty string
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == 0:
                    s += '_'
                else:
                    s += str(self.tiles[row][col])
                s += ' '
            s += '\n'
        return s
    
    def move_blank(self, direction):
        """moves the blank of self in direction
        'direction' without overflowing
        """
        if not direction in ['up', 'down', 'right', 'left']:
            print('Error: Direction not valid')
            return False
        currentloc = [ self.blank_r, self.blank_c]
        newloc = [self.blank_r, self.blank_c]
        if direction == 'up':
            newloc[0] -= 1
        elif direction == 'down':
            newloc[0] += 1
        elif direction == 'right':
            newloc[1] += 1
        else:
            newloc[1] -= 1
        if newloc[0] > (len(self.tiles) - 1) or newloc[1] > (len(self.tiles[0]) - 1) or newloc[0] < 0 or newloc[1] < 0:
            return False
        else:
            swapper = self.tiles[newloc[0]][newloc[1]]
            self.tiles[currentloc[0]][currentloc[1]] = swapper
            self.tiles[newloc[0]][newloc[1]] = 0
            self.blank_r = newloc[0]
            self.blank_c = newloc[1]
            return True
    
    def digit_string(self):
        """ recreates the digitstr of self
        """
        self.digitstr = ''
        for i in self.tiles:
            for j in i:
                self.digitstr += str(j)
        return self.digitstr
    
    def copy(self):
        """ creates a deep copy of self
        """
        digitstr = self.digit_string()
        copyboard = Board(digitstr)
        return copyboard
    
    def num_misplaced(self):
        """ finds the number of tiles 
        that are different from the goal state,
        not counting the blank tile
        """
        goalstate = '012345678'
        digitstr = self.digit_string()
        num = 0
        for i in range(len(digitstr)):
            if digitstr[i] != '0':
                if digitstr[i] != goalstate[i]:
                    num += 1
        return num
    
#    def __eq__(self, other):
#        """ untested alternate __eq__ method
#        """
#        selfdigitstr = self.digit_string()
#        otherdigitstr = other.digit_string()
#        if selfdigitstr == otherdigitstr:
#            return True
#        else:
#            return False
    
    def __eq__(self, other):
        """ overloads ==
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False
