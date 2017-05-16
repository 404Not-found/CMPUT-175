# Yunshu Zhao
# 2016 Winter Term
# University of Alberta

import random

class BattleshipGame:
#-------------------------------------------------------------------------------    
    def __init__(self):  # Initialize the lists
        
        self.__computerBoard = []
        self.__dupBoard = []
        self.__userBoard = []
        self.__letter=['A','B','C','D','E','F','G','H','I','J']
        self.__ship = ['A','B','S','D','P']
        self.__userList = []
        self.__computerList = []
        self.__sinkList = [['Aircraft Carrier','Destroyer','Battleship','Patrol Boat','Submarine'],[]]
        
#------------------------------------------------------------------------------- 
    def getBoard(self):  # Get a 10x10 Computer board and a duplicate board
        
        for x in range(10):
            self.__computerBoard.append([])
            self.__dupBoard.append([])
            for y in range(10):
                self.__computerBoard[x].append(' ')
                self.__dupBoard[x].append(' ')
                
        for x in range(11):     # Get a 11x11 user board since the 0 position is always empty
            self.__userBoard.append([])
            for y in range(11):
                self.__userBoard[x].append(' ') 
                
        return self.__computerBoard,self.__userBoard
                
#-------------------------------------------------------------------------------
    def drawBoard(self):    # Draw the board
        
        print("    Computer's board:        User's board:  ")          #dupBoard")                  # For testing print the duplicate board
        print('   1 2 3 4 5 6 7 8 9 10      1 2 3 4 5 6 7 8 9 10')     #1 2 3 4 5 6 7 8 9 10')      # For testing
        for x in range(10):
            print(str(self.__letter[x])+' |'+str('|'.join(self.__computerBoard[x])+'|   '+str(self.__letter[x])+str('|'.join(self.__userBoard[x]))+'| '))#+str(self.__letter[x])+'  |'+str('|'.join(self.__dupBoard[x])+'|'))                   # For testing 
            
#-------------------------------------------------------------------------------        
    def remaining(self):    # Return how many ships wait to be dropped 
            return len(self.__ship)
        
#-------------------------------------------------------------------------------      
    def selectShip(self,ship):  # Delete the ship that already dropped
        self.__ship.remove(ship)
        return self.__ship
    
#-------------------------------------------------------------------------------   
    def validatePlacement(self, col, size, x, y, orientation):  # Validating the movement
        move = 'yes'                        # Create the move variable to check is the move is eligible 
        if int(size) == 5: ship = 'A'       # and also prevent computer move if the player made a mistake
        elif int(size) == 4: ship = 'B'     # Transform the size input to the specific ship
        elif int(size) == 3:
            if 'S' in self.__ship: ship = 'S'
            elif 'D' in self.__ship: ship = 'D'
            else: print('This ship is already token')
        elif int(size) == 2: ship = 'P'
        
        if orientation == 'v':          # Drop the ship verticaly is the orientation is v
            check = 'pass'          # The check variable is use to check if the ship have been took 
            try:                # Use try to validate and avoid any kind of problems that may have
                if ship in self.__ship:
                    try:
                        for a in range(int(x),int(x)+int(size)):      # Check if that every upcoming move is took
                            if not self.__userBoard[int(a)][int(y)] == ' ':
                                print('Cannot place a Submarine there. Stern is out of the board or collides with other ship.',
                                      'Please take a look at the board and try again.',sep = '\n')
                                input('Hit ENTER to continue')                                
                                check = 'fail'
                                move = 'no'
                                break
                    except:
                        check = 'fail'
                        print('index out of range')
                        
                    if check == 'pass':         #  If the check pass, place the ship
                        
                        self.selectShip(ship)
                        for a in range(int(x),int(x)+int(size)):
                            self.__userBoard[int(a)][int(y)] = ship
                else:
                    print('This ship is already token')
                    move = 'no'
            except UnboundLocalError:
                print('This ship is already token')
                move = 'no'
                
        elif orientation == 'h':            # Same thing here for the horizontal
            check = 'pass'
            try:
                if ship in self.__ship:
                    try:
                        for a in range(int(y),int(y)+int(size)):
                            
                            if not self.__userBoard[int(x)][int(a)] == ' ':
                                
                                print('Cannot place a Submarine there. Stern is out of the board or collides with other ship.',
                                      'Please take a look at the board and try again.',sep = '\n')
                                input('Hit ENTER to continue')
                                check = 'fail'   
                                move = 'no'
                                break
                    except IndexError:
                        check = 'fail'
                        print('index out of range ')
                        
                    if check == 'pass':
                        
                        self.selectShip(ship)
                        for a in range(int(y),int(y)+int(size)):
                            self.__userBoard[int(x)][int(a)] = ship
                else:
                    print('This ship is already token')
                    move = 'no'
            except UnboundLocalError:
                print('This ship is already token')
                move = 'no'            
        return (move,ship)
#-------------------------------------------------------------------------------               
    def computerPlacement(self,size,symbol,orientation):        # Create a function to simplify 
        ComputerX = random.randint(1,10-int(size))          # the movement for different size
        ComputerY = random.randint(1,10-int(size)) 
        
        if orientation == 'v':      # For vertical
            for a in range(int(ComputerX),int(ComputerX)+int(size)):    # check to avoid the intersection 
                if self.__dupBoard[int(a)][int(ComputerY)] != ' ':      # that may have when computer placing the ship
                    raise                                               # If they have intersection point, raise the problem
            for a in range(int(ComputerX),int(ComputerX)+int(size)):
                self.__dupBoard[int(a)][int(ComputerY)] = str(symbol)   # I put every computer ship in the duplicate board
                                         # because the computer board is hide and empty
        if orientation == 'h':      # For horizontal                    # I check in the duplicate board if the player hits the ship
            for a in range(int(ComputerY),int(ComputerY)+int(size)):    # and put the symbols # * in the computer board
                if self.__dupBoard[int(ComputerX)][int(a)] != ' ':
                    raise
            for a in range(int(ComputerY),int(ComputerY)+int(size)):
                self.__dupBoard[int(ComputerX)][int(a)]= str(symbol)            
            
#-------------------------------------------------------------------------------              
    def getComputerShip(self, size, move):
        orientation = random.choice('vh')       # Randomly select the computer orientation 
        if int(size) == 5: symbol = 'A'         # Transform the size to specific ship
        elif int(size) == 4: symbol = 'B'
        elif int(size) == 3:                    
            if any('S' in x for x in self.__dupBoard):      # Since there are two ships for size 3 
                symbol = 'D'                                # If Submarine placed then place Destroyer
            else:
                symbol = 'S'
        elif int(size) == 2: symbol = 'P'
        
        if move != 'no':
            self.computerPlacement(size,symbol,orientation)
        else:
            print()
            
#-------------------------------------------------------------------------------
    def makeA_Move(self, x, y):             # Make a move and check if it hits the ship by checking the duplicate board
        if self.__dupBoard[int(x)][int(y)] != ' ':
            self.__computerBoard[int(x)][int(y)] = '#'
            self.__dupBoard[int(x)][int(y)] = ' '
        else:
            self.__computerBoard[int(x)][int(y)] = '*'
            self.__dupBoard[int(x)][int(y)] = ' '
            
#-------------------------------------------------------------------------------
    def ComputerHit(self):          # Randomly select a position to hit
        x = random.randint(0,9)
        y = random.randint(1,10)
        
        if x == 0: col = 'A'
        if x == 1: col = 'B'        # Transform the coordinate to the letter 
        if x == 2: col = 'C'
        if x == 3: col = 'D'
        if x == 4: col = 'E'
        if x == 5: col = 'F'
        if x == 6: col = 'G'
        if x == 7: col = 'H'
        if x == 8: col = 'I'
        if x == 9: col = 'J'        
        
        if self.__userBoard[int(x)][int(y)] == ' ':     # Check if the computer hit
            self.__userBoard[int(x)][int(y)] = '*'
            return (col,y,False)
            
        elif self.__userBoard[int(x)][int(y)] != ' ' and self.__userBoard[int(x)][int(y)] != '*':
            self.__userBoard[int(x)][int(y)] = '#'
            return (col,y,False)
        else:
            pass
    
#-------------------------------------------------------------------------------    
    def getEnemyFleet(self,ship):       # Return the sink list contain two lists
        
        self.__sinkList[0].remove(str(ship))
        self.__sinkList[1].append(str(ship))
        
        return self.__sinkList
    
#-------------------------------------------------------------------------------
    def checkIfSunk(self):      
        
        if not any('S'  in x for x in self.__dupBoard):     # Check every element in the board
            try:                                            # Check if the ship is in the sink list
                ship = 'Submarine'                          # try and except is to make sure it only show once
                self.getEnemyFleet(ship)                    # If its already removed from the sink list, ignore it
                print('Submarine sunk')
            except:
                pass
            
        if not any('D'  in x for x in self.__dupBoard):     # Chekc for Destroyer
            try:
                ship = 'Destroyer'
                self.getEnemyFleet(ship)   
                print('Destroyer sunk')
            except:
                pass           
            
        if not any('P'  in x for x in self.__dupBoard):     # Check for Patrol Boat
            try:
                ship = 'Patrol Boat'
                self.getEnemyFleet(ship)            
                print('Patrol Boat sunk')   
            except:
                pass
                
        if not any('B'  in x for x in self.__dupBoard):     # Check for Battleship
            try:
                ship = 'Battleship'
                self.getEnemyFleet(ship)             
                print('Battleship sunk')
            except:
                pass
            
        if not any('A'  in x for x in self.__dupBoard):     # Check for Aircraft Carrier
            try:
                ship = 'Aircraft Carrier'
                self.getEnemyFleet(ship)             
                print('Aircraft Carrier sunk')
            except:
                pass
                
        print('Ships to sink: '+str(self.__sinkList[0])+' Ships sunk: '+str(self.__sinkList[1]))
        # Print the list that contain two lists, to sink and sunk ship
        
#-------------------------------------------------------------------------------
    def checkWinning(self):
        userCount = 0               # Both count are variables for count the none ship letter space
        computerCount = 0           # Such as ' ', '#', '*' are count in this variable, but not 'A','B','S','D','P'
        
        win = 'x'                   # Ser defult win variable to any string 
        for x in self.__dupBoard:
            for y in x:
                if y == ' ':
                    userCount += 1  # Check every elements in the board and count for none ship element
        if userCount == 100:        # If count to 100 means their are no ship left, and set the win to a string 'yes'
            print('Congratulations! User WON!')
            win = 'yes'
        for x in self.__userBoard:
            for y in x:
                if y ==' ' or y =='#' or y == '*':
                    computerCount += 1
        
        if computerCount == 121:            # Since the user board is 11x11
            print('Sorry, Computer won')    # If total none ship space is 121 computer win
            win = 'yes'
            
        if win == 'yes':                # Check if someone win
            return False
        else:
            return True
#-------------------------------------------------------------------------------
def Input(size):        # A user define function out of the class to valid the coordinate input
    
    col = 'str'
    y = 99    
    while y == None or int(size)>5 or col.lower() not in 'a,b,c,d,e,f,g,h,i,j'.split(',') or y not in '1,2,3,4,5,6,7,8,9,10'.split(','):
        coord = input('Enter coordinates x y (x in [A..J] and y in [1..10]): ')
    
        try: col,y = coord.split()
        except ValueError: y = None
            
    if col.upper() == 'A': x = 0
    elif col.upper() == 'B': x = 1      # Transfrom the letter to number for coordinate
    elif col.upper() == 'C': x = 2      
    elif col.upper() == 'D': x = 3
    elif col.upper() == 'E': x = 4            
    elif col.upper() == 'F': x = 5
    elif col.upper() == 'G': x = 6    
    elif col.upper() == 'H': x = 7
    elif col.upper() == 'I': x = 8       
    elif col.upper() == 'J': x = 9 
    
    return (x,y,col)            # Return the letter and coordinate
#-------------------------------------------------------------------------------
def main():
    battle = BattleshipGame()
    battle.getBoard()
    battle.drawBoard()
    playedList= []  # append in the previous move 
    
    while battle.remaining()>0:             # Drop ships 
        
        size = 'a str'    # a value for validation
        while size not in '5,4,3,2'.split(','):
            size = input('Placing a Battleship of size ') 
        
        x,y,col = Input(size)
        
        orientation = 'a'  # create a value for validation
        while orientation not in 'v,h'.split(','):      # Ask for orientation
            orientation = input('This ship is vertical or horizontal (v,h)?')        
        
        move,ship = battle.validatePlacement(col,size, x, y, orientation)
        
        computer = True
        while computer == True:         # Computer drop the ship, drop again if any intersection happened 
            try: 
                battle.getComputerShip(size,move)
                computer = False
            except:
                computer = True
        print('you placed at '+col+' '+y)
        battle.drawBoard()
        
    input('Done placing user ships. Hit ENTER to continue')
    
    game = True                 
    while game == True:                 # Hit ships
        x,y,location = Input(size)
        
        while [location.upper(),y] in playedList:
            print('You already droped at '+str(location)+' '+str(y))
            x,y,location = Input(size)
            
        playedList.append([location.upper(),y])   
        
        battle.makeA_Move(x,int(y)-1)
        print('Hit at '+location.upper()+' '+y)
        
        computer = True
        while computer == True:
            Computer_X, ComputerY, computer = battle.ComputerHit()
               
        print('Computer hit at '+str(Computer_X)+' '+str(ComputerY))
        battle.drawBoard() 
        battle.checkIfSunk()
        
        game = battle.checkWinning()     # game is equals to the value that checkWinning() returned 
                                         # If someone win, return False and the game end 
main()