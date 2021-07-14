import random
class bBoard:
    """A data type representing a battleship board
       with 10 rows and 10 columns.
    """
    def __init__(self, width=10, height=10):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            if row == 9:
                s += str(row +1) + '|'
            else:
                s += str(row +1) + ' ' + '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        

        s += ' ' + (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here
        s += '\n'
        for i in range(97, 107):
            if i == 97:
                s += '  '
            s += ' ' + chr(i)

        return s       # the board is complete, return it
    
    def createShips(self):
        """createShips creates 3 ships, represented as O, that are randomly placed on the board.
           One ships has a length of 4, one has length of 3, and one has length of 2
           Argument: self is an object of the bBoard class
           Result: updates the board to have 3 ships
        """
        two = random.randint(0,100)
        three = random.randint(0,100)
        four = random.randint(0,100)
        vh2 = random.randint(0,2)
        vh3 = random.randint(0,2)
        vh4 = random.randint(0,2)
        while two == three or two == four or three == four:
            two = random.randint(0,100)
            three = random.randint(0,100)
            four = random.randint(0,100)
        if two%10 < self.width-2 and two//10 < self.height - 2:
            if vh2 == 0:
                self.data[two//10][two%10] = '2'
                self.data[two//10][two%10+1] = '2'
            else:
                self.data[two//10][two%10] = '2'
                self.data[two//10+1][two%10] = '2'
        else:
            if two%10 - 2 > 0:
                self.data[two//10][two%10] = '2'
                self.data[two//10][two%10-1] = '2'
            else:
                if two//10 - 1 < 0:
                    self.data[two//10][two%10] = '2'
                    self.data[two//10+1][two%10] = '2'
                elif two//10 + 1> 9:
                    self.data[two//10-1][two%10-1] = '2'
                    self.data[two//10-2][two%10-1] = '2'
                else:
                    self.data[two//10][two%10] = '2'
                    self.data[two//10+1][two%10] = '2'

        if three%10 < self.width - 3 and three//10 <self.height - 3:
            if vh3 == 0:
                self.data[three//10][three%10] = '3'
                self.data[three//10][three%10+1] = '3'
                self.data[three//10][three%10+2] = '3'
            else:
                self.data[three//10][three%10] = '3'
                self.data[three//10+1][three%10] = '3'
                self.data[three//10+2][three%10] = '3'
        else:
            if three%10 - 3 > 0:
                self.data[three//10][three%10] = '3'
                self.data[three//10][three%10-1] = '3'
                self.data[three//10][three%10-2] = '3'
            else:
                if three//10 -1 < 0:
                    self.data[three//10][three%10] = '3'
                    self.data[three//10+1][three%10] = '3'
                    self.data[three//10+2][three%10] = '3'
                elif three//10 + 1 > 9:
                    self.data[three//10-1][three%10-1] = '3'
                    self.data[three//10-2][three%10-1] = '3'
                    self.data[three//10-3][three%10-1] = '3'
                else:
                    self.data[three//10][three%10] = '3'
                    self.data[three//10+1][three%10] = '3'
                    self.data[three//10-1][three%10] = '3'

        if four%10 < self.width - 4 and four//10 < self.height - 4:
            if vh4 == 0:
                self.data[four//10][four%10] = '4'
                self.data[four//10][four%10+1] = '4'
                self.data[four//10][four%10+2] = '4'
                self.data[four//10][four%10+3] = '4'
                
            else:
                self.data[four//10][four%10] = '4'
                self.data[four//10+1][four%10] = '4'
                self.data[four//10+2][four%10] = '4'
                self.data[four//10+3][four%10] = '4'
                
        else:
            if four%10 - 4 > 0:
                self.data[four//10][four%10] = '4'
                self.data[four//10][four%10-1] = '4'
                self.data[four//10][four%10-2] = '4'
                self.data[four//10][four%10-3] = '4'
                
            else:
                if four//10 -1 < 0:
                    self.data[four//10][four%10] = '4'
                    self.data[four//10+1][four%10] = '4'
                    self.data[four//10+2][four%10] = '4'
                    self.data[four//10+3][four%10] = '4'
                    
                elif four//10 + 1 >= 9:
                    self.data[four//10-1][four%10-1] = '4'
                    self.data[four//10-2][four%10-1] = '4'
                    self.data[four//10-3][four%10-1] = '4'
                    self.data[four//10-4][four%10-1] = '4'
                    
                else:
                    self.data[four//10][four%10] = '4'
                    self.data[four//10][four%10+1] = '4'
                    self.data[four//10][four%10+2] = '4'
                    self.data[four//10][four%10-1] = '4'
            
    def ifShipOverlap(self):
        """ifShipOverlap checks if there are any overlapping ships. If there is, it would rerun true
        """
        x = 0
        for row in range(0, self.height):
            for col in range(0, self.width):
                if (inarow_Nsouth('2', row - (2-1), col, self.data, 2) == True or \
                    inarow_Neast('2', row, col, self.data, 2) == True):
                    x += 1
                if (inarow_Nsouth('3', row - (3-1), col, self.data, 3) == True or \
                    inarow_Neast('3', row, col, self.data, 3) == True):
                    x += 1
                if (inarow_Nsouth('4', row - (4-1), col, self.data, 4) == True or \
                    inarow_Neast('4', row, col, self.data, 4) == True):
                    x += 1
                if x == 3:
                    return False
        return True
                    

    def addMove(self, letter, number):
        """addMove X into the gameboard. letter and number indicate where the X is added. 
           Argument: self is an object of the Board class. letter is a string from a to j. number is a number from 1 to 10
           Result: Modifies the game board so that it contains an X at the specified location.
        """
        if letter in '0123456789':
            if letter == '0':
                letter = 'a'
            if letter == '1':
                letter = 'b'
            if letter == '2':
                letter = 'c'
            if letter == '3':
                letter = 'd'
            if letter == '4':
                letter = 'e'
            if letter == '5':
                letter = 'f'
            if letter == '6':
                letter = 'g'
            if letter == '7':
                letter = 'h'
            if letter == '8':
                letter = 'i'
            if letter == '9':
                letter = 'j'
        l = ord(letter) - 97
        if self.data[number-1][l] == '2':
            self.data[number-1][l] = 'b'
            print ('hit!')
            if self.ifSunk(2) == True:
                print('Ship of length two has sunk!')
        elif self.data[number-1][l] == '3':
            self.data[number-1][l] = 'c'
            print ('hit!')
            if self.ifSunk(3) == True:
                print('Ship of length three has sunk!')
        elif self.data[number-1][l] == '4':
            self.data[number-1][l] = 'd'
            print ('hit!')
            if self.ifSunk(4) == True:
                print('Ship of length four has sunk!')
        elif self.data[number-1][l] == ' ':
            self.data[number-1][l] = 'M'
            print ('miss!')
    
    def allowMove(self, letter, number):
        """allowMove checks if a move has already been played so that there would be no repeats for the AI.
           Argument: self is an object of the bBoard class. Letter is a string and number is an integer.
           Result: Returns true if the spot is open and no move has been made there. Returns false otherwise.
        """
        l = int(ord(letter) - 97)
        if self.data[number-1][l] in 'bcdM':
            return False
        else: 
            return True

    def ifSunk(self, N):
        """ifSunk scans the board to see if there are any ships sunk.
           Argument: self is an object of bBoard class. N is an integer that represents the length of a ship.
           Result: returns true if a ship of length N is sunk
        """
        H = self.height
        W = self.width
        D = self.data

        if N == 2:
            for row in range(0, H):
                for col in range(0, W):
                    if inarow_Neast('b', row, col, D, N):
                        return True
                    if inarow_Nsouth('b', row-(N-1), col, D, N):
                        return True
        if N == 3:
            for row in range(0, H):
                for col in range(0, W):
                    if inarow_Neast('c', row, col, D, N):
                        return True
                    if inarow_Nsouth('c', row-(N-1), col, D, N):
                        return True
        if N == 4:
            for row in range(0, H):
                for col in range(0, W):
                    if inarow_Neast('d', row, col, D, N):
                        return True
                    if inarow_Nsouth('d', row-(N-1), col, D, N):
                        return True
        return False
    
    def ifHit(self, letter, number):
        """ifHit checks if the last move played hit one of the ships
           Argument: self is an object of the bBoard class
           Result: Returns true if the move is a hit. Returns false otherwise.
        """
        l = int(ord(letter) - 97)
        if self.data[number-1][l] in 'bcd':
            return True
        else: 
            return False
    
    def ailvl1(self):
        """ level 1 of ai plays random moves"""
        letterchoiceb = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
        numberchoiceb = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        while self.allowMove(letterchoiceb, numberchoiceb) == False:
            letterchoiceb = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
            numberchoiceb = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        return letterchoiceb, numberchoiceb
            
    
    def ailvl2(self):
        """level 2 ai plays by starting its first shot at the top left corner and
            then goes from top to bottom to the bottom right corner.
        """
        H = self.height
        W = self.width
        letterMove = []
        numberMove = []
        for i in range(0,H):
            for j in range(0,W):
                letterMove += [i]
                numberMove += [j]
        return letterMove, numberMove


    def ailvl3(self):
        """ailvl 3 is the hardest difficult ai. It will win in 15 moves.
        """
        D = self.data
        H = self.height
        W = self.width
        letMove = []
        numMove = []
        holder = 0
        for i in range(0, H):
            for j in range(0, W):
                if D[i][j] == '2':
                    letMove += [j]
                    letMove += [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
                    letMove += [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
                    numMove += [i]
                    numMove += [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
                    numMove += [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
                if D[i][j] == '3':
                    letMove += [j]
                    letMove += [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
                    numMove += [i]
                    numMove += [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
                if D[i][j] == '4':
                    if holder < 2:
                        letMove += [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
                        numMove += [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
                    letMove += [j]
                    numMove += [i]
                    holder += 1
        return letMove, numMove

r = 0
t = 0
def hostGame():
    """ hostGame should alternate between board a and board b, board a being first. Each player should be able to 
    launch a missile creating an "X" wherever it lands. It will ask the human player for an input and the ai should play 
    against the human. board a is the human board 
    """ 
    global r
    global t
    a = bBoard()
    b = bBoard()
    turn = 0
    letterchoicea = ''
    numberchoicea = 0
    letterchoiceb = ''
    numberchoiceb = 0
    
    while (a.ifShipOverlap() or b.ifShipOverlap()):
        a = bBoard()
        b = bBoard()
        a.createShips()
        b.createShips()
    print()
    print("Welcome to BattleShip!")
    print()
    print("This is your board!")
    print(a)
    c = input('Would you like to change boards? (y/n): ')
    while c == 'y':
        a = bBoard()
        while (a.ifShipOverlap() or b.ifShipOverlap()):
            a = bBoard()
            a.createShips()
        print(a)
        c = input('Change? (y/n): ')
    print("What level AI would you like to play against?: (1, 2, 3) ")
    print("(1) level 1 plays random moves")
    print("(2) level 2 plays moves in order from top left to bottom right going vertically")
    print("(3) level 3 will win in between 15 to 18 moves everytime")
    ailevel = input("1/2/3 : ")
    while ailevel not in "123":
        ailevel = input("Please pick 1, 2, or 3: ")
    if ailevel == '3':
        ai3L = []
        ai3N = []
        ai3L, ai3N = a.ailvl3()
    if ailevel == '2':
        ai2L = []
        ai2N = []
        ai2L, ai2N = a.ailvl2()
    print("Let's Begin!")
    print("Make sure you remember your moves!")
    while True:
        letterchoicea = input("human letter choice: ")
        numberchoicea = input("human number choice: ")
        while letterchoicea not in 'abcdefghij' or numberchoicea not in '12345678910' or len(letterchoicea) != 1:
            letterchoicea = input("please pick a letter from a to j ")
            numberchoicea = input("please pick a number from 1 to 10 ")
        while b.data[int(numberchoicea)-1][ord(letterchoicea) - 97] in 'Mbcd':
            letterchoicea = input("You already shot there! Pick another letter: ")
            numberchoicea = input("human number choice: ")
        b.addMove(str(letterchoicea), int(numberchoicea))
        if ailevel == '3':
            letterchoiceb = ai3L[turn]
            numberchoiceb = ai3N[turn]
            a.addMove(str(letterchoiceb), int(numberchoiceb+1))
        if ailevel == '2':
            letterchoiceb = ai2L[turn]
            numberchoiceb = ai2N[turn]
            a.addMove(str(letterchoiceb), int(numberchoiceb+1))
        if ailevel == '1':
            letterchoiceb = a.ailvl1()[0]
            numberchoiceb = a.ailvl1()[1]
            a.addMove(str(letterchoiceb), numberchoiceb)
        print(a)
        turn += 1
        if a.ifSunk(2) == True and a.ifSunk(3) == True and a.ifSunk(4) == True:
            print(a)
            print(b)
            print ('You Lost!')
            r += 1
            print("You lost ", r, " times")
            print("You won ", t , " times")
            print("Total number games ", r + t)
            print()
            pa = ''
            pa = input("Would you like to play again? (y/n): ")
            if pa == 'y':
                return hostGame()
            elif pa == 'n':
                return 'Thanks for playing!'
            else:
                print("You didn't pick y or n so I will assume you are done")
                return "Thanks for playing!"
        if b.ifSunk(2) == True and b.ifSunk(3) == True and b.ifSunk(4) == True:
            print(a)
            print(b)
            print("You Won!")
            t += 1
            print("You lost ", r, " times")
            print("You won ", t , " times")
            print("Total number games ", r + t)
            pa = ''
            pa = input("Would you like to play again? (y/n): ")
            if pa == 'y':
                return hostGame()
            elif pa == 'n':
                return 'Thanks for playing!'
            else:
                print("You didn't pick y or n so I will assume you are done")
                return "Thanks for playing!"


def inarow_Nsouth(ch, r_start, c_start, A, N):
    """inarow_Nsouth checks if there are N number of the argument ch in a row going down.
       Argument: ch is a character (string), r_start and c_start are integers. N is an integer and A is the array
       Result: returns true if there is N number of ch going south.
    """
    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start < 0 or r_start >= NR:
        return False # out of bounds in rows

    # other out-of-bounds checks...
    if c_start < 0 or c_start > NC - N:
        return False # out of bounds in cols

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start+i][c_start] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True      

def inarow_Neast(ch, r_start, c_start, A, N):
    """inarow_Neast checks if there are N number of the argument ch in a row going to the right.
       Argument: ch is a character (string), r_start and c_start are integers. N is an integer and A is the array
       Result: returns true if there is N number of ch going to the right.
    """
    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start < 0 or r_start >= NR:
        return False # out of bounds in rows

    # other out-of-bounds checks...
    if c_start < 0 or c_start > NC - N:
        return False # out of bounds in cols

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True 