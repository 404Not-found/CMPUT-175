# Yunshu Zhao
# 2016 Winter Term
# University of Alberta

import random

class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0]="#"
        
#-------------------------------------------------------------         
    def drawBoard(self):
    # This method prints out the board with current plays adjacent to a board with index.
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9],' 7 | 8 | 9 ', sep='\t')
        print('-----------','-----------', sep='\t')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6],' 4 | 5 | 6 ', sep='\t')
        print('-----------','-----------', sep='\t')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3],' 1 | 2 | 3 ', sep='\t')
           
#------------------------------------------------------------- 
    def boardFull(self):
    # This method checks if the board is already full and returns True. Returns false otherwise      
        if " " in self.board:
            return False
        else:
            return True
        
#-------------------------------------------------------------         
    def cellIsEmpty(self, cell):
        if cell==0 or cell>9:
            return False
        else:
            return self.board[cell]==" "

#------------------------------------------------------------- 
    def assignMove(self, cell,ch):
        # assigns the cell of the board to the character ch
        if cell<10 and cell>0:
            self.board[cell]=ch            
        
#-------------------------------------------------------------  
    def whoWon(self):
        # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

#-------------------------------------------------------------     
    def isWinner(self, ch):
    # Given a player's letter, this method returns True if that player has won.
        return ((self.board[7] == ch and self.board[8] == ch and self.board[9] == ch) or # across the top
                (self.board[4] == ch and self.board[5] == ch and self.board[6] == ch) or # across the middle
                (self.board[1] == ch and self.board[2] == ch and self.board[3] == ch) or # across the bottom
                (self.board[7] == ch and self.board[4] == ch and self.board[1] == ch) or # down the left side
                (self.board[8] == ch and self.board[5] == ch and self.board[2] == ch) or # down the middle
                (self.board[9] == ch and self.board[6] == ch and self.board[3] == ch) or # down the right side
                (self.board[7] == ch and self.board[5] == ch and self.board[3] == ch) or # diagonal
                (self.board[9] == ch and self.board[5] == ch and self.board[1] == ch)) # diagonal  
    
# Check if the first avilable cell is empty and place the symbol  
    def dumbComputer(self,ch):
        for x in range(1,10):
            if self.cellIsEmpty(x):
                self.assignMove(x,ch)
                break
            
# Randomly select cell from avilable position
    def randomComputer(self,ch,randomMove):
        freePosition = []
        for x in range(1,10):
            if self.cellIsEmpty(x):
                freePosition.append(x) 
        
        if randomMove in freePosition:
            self.assignMove(randomMove,ch)
        elif randomMove not in freePosition:
            self.assignMove(random.choice(freePosition),ch)

#----------------------------------------------- 
    def smartComputer(self,ch):
        
        corner = []
        side = []
        freePosition = []
        cell = []          
        
        for x in range(1,10):
            if x == 1 or 3 or 7 or 9:
                if self.board[x] == ' ':
                    corner.append(x)
            if x == 2 or 4 or 6 or 8:
                if self.board[x] == ' ':
                    side.append(x) 
                    
            if self.cellIsEmpty(x):
                freePosition.append(x)
                
            if not self.cellIsEmpty(x):
                cell.append(x)
                
        if self.board[5] == ' ':     # If the center is empty, place the symbol their
            self.assignMove(5,ch)
            
        elif self.board[5] != ' ' and len(freePosition) == 7:        
            self.assignMove(random.choice(corner),ch)  
               
        elif len(freePosition) == 8 or 6:
            if len(corner) != 0:
                self.assignMove(random.choice(side),ch)
                                       
            else:
                self.assignMove(random.choice(corner),ch) 

# Check every posible win position---------------------------    
        elif self.board[7] == ch and self.board[8] == ch:
            if self.cellIsEmpty(9):
                self.assignMove(9,ch)  
            else:
                self.assignMove(random.choice(freePosition),ch)                
        elif self.board[8] == ch and self.board[9] == ch:
            if self.cellIsEmpty(7):
                self.assignMove(7,ch) 
            else:
                self.assignMove(random.choice(freePosition),ch)                
        elif self.board[7] == ch and self.board[9] == ch:
            if self.cellIsEmpty(8):
                self.assignMove(8,ch) 
            else:
                self.assignMove(random.choice(freePosition),ch)                
# Check every posible win position----------------------------                
        elif self.board[4] == ch and self.board[5] == ch:
            if self.cellIsEmpty(6):
                self.assignMove(6,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)                
        elif self.board[5] == ch and self.board[6] == ch:
            if self.cellIsEmpty(4):
                self.assignMove(4,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
        elif self.board[4] == ch and self.board[6] == ch:
            if self.cellIsEmpty(5):
                self.assignMove(5,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
# Check every posible win position----------------------------                 
        elif self.board[1] == ch and self.board[2] == ch :
            if self.cellIsEmpty(3):
                self.assignMove(3,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
        elif self.board[2] == ch and self.board[3] == ch :
            if self.cellIsEmpty(1):
                self.assignMove(1,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
        elif self.board[1] == ch and self.board[3] == ch :
            if self.cellIsEmpty(2):
                self.assignMove(2,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
# Check every posible win position----------------------------            
        elif self.board[7] == ch and self.board[4] == ch:
            if self.cellIsEmpty(1):
                self.assignMove(1,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
        elif self.board[7] == ch and self.board[1] == ch:
            if self.cellIsEmpty(4):
                self.assignMove(4,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
        elif self.board[1] == ch and self.board[4] == ch:
            if self.cellIsEmpty(7):
                self.assignMove(7,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
# Check every posible win position----------------------------              
        elif self.board[8] == ch and self.board[5] == ch:
            if self.cellIsEmpty(2):
                self.assignMove(2,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
        elif self.board[8] == ch and self.board[2] == ch:
            if self.cellIsEmpty(5):
                self.assignMove(5,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
        elif self.board[2] == ch and self.board[5] == ch:
            if self.cellIsEmpty(8):
                self.assignMove(8,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)                
# Check every posible win position----------------------------                          
        elif self.board[9] == ch and self.board[6] == ch:
            if self.cellIsEmpty(3):
                self.assignMove(3,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)                
        elif self.board[9] == ch and self.board[3] == ch:
            if self.cellIsEmpty(6):
                self.assignMove(6,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)                
        elif self.board[3] == ch and self.board[6] == ch:
            if self.cellIsEmpty(9):
                self.assignMove(9,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
# Check every posible win position----------------------------          
        elif self.board[7] == ch and self.board[5] == ch:
            if self.cellIsEmpty(3):
                self.assignMove(3,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)                
        elif self.board[7] == ch and self.board[3] == ch:
            if self.cellIsEmpty(5):
                self.assignMove(5,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
        elif self.board[5] == ch and self.board[3] == ch:
            if self.cellIsEmpty(7):
                self.assignMove(7,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
# Check every posible win position----------------------------              
        elif self.board[9] == ch and self.board[5] == ch:
            if self.cellIsEmpty(1):
                self.assignMove(1,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)                
        elif self.board[9] == ch and self.board[1] == ch:
            if self.cellIsEmpty(5):
                self.assignMove(5,ch)
            else:
                self.assignMove(random.choice(freePosition),ch)            
        elif self.board[1] == ch and self.board[5] == ch:
            if self.cellIsEmpty(9):
                self.assignMove(9,ch)  
            else:
                self.assignMove(random.choice(freePosition),ch)
        print(len(freePosition))

#------------------------------------------------------------- 
# The main program
def main():
    print ("Welcome to Tic Tac Toe Series")
    myGameLoop=True
    
    while myGameLoop:
        myBoard=TicTacToe()
        gameIsOn=True
        nameInput = ' '
        typeInput = ' '
        while typeInput not in '1 2 3 4 5 6'.split():
            print('User against user ...............1',
                  'User against dumb computer ......2',
                  'User against random computer ....3',
                  'User against smart computer......4',
                  'Randomly selected game...........5', 
                  'Quit ............................6',
                  'Enter your choice: ',
                  sep='\n')
            typeInput = input()    
        
        if typeInput == '5':   
                typeInput = str(random.randint(1,4)) # Random select from option 1 to 4
        if typeInput != '6':
            nameInput = input('what is your name?  ') # If input is 6 then the program quit, else ask user for name
                
            
        turnInput=" "
        while turnInput not in 'x o r'.split():
            turnInput = input(nameInput+', do you want to play x or o? Type r if you want me to chose for you.'+'\n').lower() 
            
        turn = 'x'   # x is always go first
        
        if turnInput =='o':
            computer = 'x'   # Set the computer letter
            
        elif turnInput == 'x':
            computer = 'o'
            
        elif turnInput == 'r':
            turnInput = random.choice('xo')
            
            if turnInput == 'x':       # Since the turnInput is random, I use this method t
                computer = 'o'
            elif turnInput == 'o':
                computer ='x'
            
    #------------------------------------------------------------- 
        while gameIsOn:
            
    #------------------------------------------------------------- 
    # User against user        
            if typeInput == '1':              
                    
                print('User against user') 
                
                myBoard.drawBoard()
                print ("It is the turn for", turn,". ",end="")
                move="0"
                while not myBoard.cellIsEmpty(int(move)):
                    move="0"
                    while move not in "1 2 3 4 5 6 7 8 9".split():
                        move=input("what is your move?")
                    if not myBoard.cellIsEmpty(int(move)):
                        print (move,"is not available.    ",end='')
                        move="0"
                myBoard.assignMove(int(move),turn)
                winner=myBoard.whoWon()
                if winner!='':
                    myBoard.drawBoard()
                    print (turn,"wins. Congrats!")
                    input("Press Enter to continue")           
                    gameIsOn=False
                elif myBoard.boardFull():
                    myBoard.drawBoard()
                    print ("It's a tie.")
                    input("Press Enter to continue")                
                    gameIsOn=False
                elif turn=="x":
                    turn="o"
                else:
                    turn="x"
                    
    #-------------------------------------------------------------
    # This part is use to against the computer
            elif typeInput == '2' or '3' or '4':      
                    
                if typeInput == '2':
                    print('User against dumb computer')
                elif typeInput == '3':
                    print('User against random computer') 
                    randomMove = random.randint(1,9)
                elif typeInput == '4':
                    print('User against smart computer')
                      
                myBoard.drawBoard()
                print('-------------------------------')
                
                if turn == turnInput:   
                    print ("It is the turn for", turn,". ",end="")
                           
                    move="0"
                    while not myBoard.cellIsEmpty(int(move)):
                        move="0"
                        while move not in "1 2 3 4 5 6 7 8 9".split():
                            
                            move=input("what is your move?")
                        if not myBoard.cellIsEmpty(int(move)):
                            print (move,"is not available.    ",end='')
                            move="0"
                
                    myBoard.assignMove(int(move),turnInput)
                   
                else:
                    if typeInput == '2':
                        myBoard.dumbComputer(computer)
                    elif typeInput == '3':
                        myBoard.randomComputer(computer,randomMove)
                    elif typeInput == '4':
                        myBoard.smartComputer(computer)
                    
                winner=myBoard.whoWon()
                if winner!='':  
                    myBoard.drawBoard()
                    print (turn,"wins. Congrats!")
                    input("Press Enter to continue")           
                    gameIsOn=False
                elif myBoard.boardFull():
                    myBoard.drawBoard()
                    print ("It's a tie.")
                    input("Press Enter to continue")                
                    gameIsOn=False
                elif turn=="x":
                    turn="o"
                else:
                    turn="x"                    
    #-------------------------------------------------------------                
    # Check whether the player wants to play again
        answer='x'
        while answer.upper() not in "YN":
            answer=input("Do you want to play another game? (Y/N)")
        if answer.upper() == "N":
            myGameLoop=False
    if typeInput == '6':
        gameIsOn=False

main() # Call main function