# Yunshu Zhao
# 2016 Winter Term
# University of Alberta

import random             

class OceanTreasure:
#-----------------------------------------------------------------------------   
    def __init__(self):             
        self.__board = []        
        self.__chests = []
        self.__dupChests = []
    
#-----------------------------------------------------------------------------        
    def getBoard(self):           # Get a board with 15 rows and 60 columns total is 15x60 elements
        for x in range(15):
            self.__board.append([])     # The board contain a list and 15 sub-list
                                        # Every sub-list have 60 elements
            for y in range(60):
                self.__board[x].append('~')
        
        return self.__board
    
#-----------------------------------------------------------------------------        
    def drawBoard(self):
        
        print('             1         2         3         4         5')
        print('   012345678901234567890123456789012345678901234567890123456789')
       
        for x in range(15):
            print(''+str(x).rjust(2)+' '+str(''.join(str(self.__board[x]))).replace("'","").replace(",","").replace('[','').replace(']','').replace(' ','')+' '+str(x).ljust(2))
        
        print('             1         2         3         4         5')
        print('   012345678901234567890123456789012345678901234567890123456789' )  
        
#-----------------------------------------------------------------------------    
    def getChests(self):        # Randomly generate 3 chests
        for x in range(3):
            self.__chests.append([random.randint(0,59),random.randint(0,14)])
        
        return self.__chests
#-----------------------------------------------------------------------------
    def dupChests(self):        # Duplicate 3 chests use to count how many chests left and where are they
        for x in range(0,3):    # If I set __dupChests = __chests, 
                                # every time I remove the __dup, it will also remove from the __chests
            self.__dupChests.append(self.__chests[x])
        
        return self.__dupChests
    
#-----------------------------------------------------------------------------        
    def showDup(self):          # Show the elements in __dupChests that left
        return self.__dupChests
    
#-----------------------------------------------------------------------------

    def showChest(self):        # Show the chests. Only for testing 
        return self.__chests
        
#-----------------------------------------------------------------------------
    def remove(self,x,y):       # Remove the element from the __dupChest 
        try:                    # Validate whether the sonar already droped their
            self.__dupChests.remove([int(x),int(y)])
        except ValueError:
            print('')
            print('--------------------------------------------------------------------')
            print('| You already dropped a sonar there. You lost another sonar device |')
            print('--------------------------------------------------------------------')
            
        return self.__dupChests
#-----------------------------------------------------------------------------        
    def getTreasuresLeft(self):         # Get how many Treasure left
        return len(self.__dupChests)
    
#-----------------------------------------------------------------------------    
    def dropSonar(self,x, y, sonar,lefts):    # Let the element in the position equal to the symbol
        if self.__board[int(y)][int(x)] != '~':    # Check if the enter position already have somthing in their
            self.drawBoard()
            print('')
            print('--------------------------------------------------------------------')
            print('| You already dropped a sonar there. You lost another sonar device |')
            print('--------------------------------------------------------------------')
        else:
            self.__board[int(y)][int(x)] = sonar    # If not, put the sonar their
            self.drawBoard()
            print('You have '+str(lefts)+' sonar devices available. Treasures found:'+str(3-self.getTreasuresLeft())+'. Still to be found:'+str(self.getTreasuresLeft())+'.')
#-----------------------------------------------------------------------------   
    def checkDistance(self,x ,y):
        
        distance = 1000    # The distance can't be greater then 1000
        
        for chest_X, chest_Y in self.__chests:  
            if abs(chest_X - int(x)) > abs(chest_Y - int(y)):   # Use the absolute value to check the distance
                currentDis = abs(chest_X - int(x))          
            else:
                currentDis = abs(chest_Y - int(y)) 
            if currentDis < distance: 
                distance = currentDis            
        
        if distance == 0:
            return 'X'
        else:
            if distance < 10:
                if int(chest_X)==int(x):        # return a,b,c,d instead of 1,2,3,4
                    if distance == 1:
                        return 'a'
                    elif distance == 2:
                        return 'b'
                    elif distance == 3:
                        return 'c'
                    elif distance == 4:
                        return 'd'
                    elif distance == 5:
                        return 'e'
                    else:
                        return distance
                else:
                    return distance
            else:                           # return O if the distance is out of 10
                return 'O'
                        
#-----------------------------------------------------------------------------        
def main():      
    
    ocean = OceanTreasure()
    
    ocean.getBoard()
    chest = ocean.getChests()
    ocean.drawBoard()
    ocean.dupChests()
    sonar = 20

    while sonar > 0:
        
        print('\n'+'Where do you want to drop your sonar?'+'\n'+
              'Enter coordinates x y (x in [0..59] and y in [0..14]) (or Q to quit and H for help): ')
        
        print(ocean.showChest())   # To show where the chests are. Only for testing 
        
        move = input()
        
        try:                            # Validate the input
            x, y = move.split()
        except ValueError:
            x = move
            y = None
        
        if x.upper() == 'Q':    # Quit the game
            print('\n'+'the chests were in '+ str(chest))
            print('Thank you for playing Ocean Treasures')
            return None
        
        elif x.upper() == 'H':  # Print the instruction copied from eclass Assignment 3 instruction
            print('Ocean treasures is a simple game in which you have to find treasure chests lost in the ',
                  'bottom of the ocean. The ocean is represented by a grid of 60 columns by 15 rows and the ',
                  'chests can be in any one cell. To find a chest you need to drop sonar devices at given locations.',sep='\n')
            
            print('You have a total of 20 sonar devices and there are 3 treasure chests to find, randomly ',
                  'scattered in the ocean. The game ends when you do not have sonar devices left or you ',
                  'found all three chests. To find a chest you need to drop a sonar device at the exact ',
                  'x,y coordinates of the chest. In that case the sonar would indicate "X". The sonar devices ',
                  'are twice as sensitive on the column axis than the rows. It can detect a chest 9 units away ',
                  'on both sides of the x axis and 5 units away on the y axis. If the sonar is dropped too far ',
                  '(more than 9 units away on the x axis and 6 on the y axis) from a chest, the sonar would ',
                  'indicate "O", meaning nothing detected. Again, the maximum range of the sonar device is ',
                  '9 units on the x axis and 5 units on the y axis. If the sonar is less than 10 units away from ',
                  'a chest on the x axis, the sonar would indicate the currentDis (1, 2, ..., 9). Since the the sonar ',
                  'devices are twice as sensitive on the column axis than the rows, on the y axis (rows), if the sonar ',
                  'device is closer than 6 units, closer on the y than half the x axis, and still in the range, the sonar ',
                  'would indicate a for 1, b for 2, c for 3, d for 4 and e for 5 distance units.',sep='\n')
            
        elif y != None:
            while int(x) < 0 or int(x) > 59 or int(y) < 0 or int(y) > 14:       # validating the move input
                print('Input Error, please enter coordinates x y (x in [0..59] and y in [0..14])')
                x,y = input().split()
            
            sonar -= 1
            if ocean.checkDistance(x,y) == 'X':
                
                ocean.remove(x,y)           # remove the element in the duplicate list 
                
            ocean.dropSonar(x,y,ocean.checkDistance(x,y),sonar)
                    
            if ocean.getTreasuresLeft() == 0:       
                    
                    print('\n'+'Well done! You found all the 3 treasure Chests using '+str(sonar)+' out of 20 sonar devices.')  
                    return None                    
        else:
            print('Input Error')            
        
    if sonar == 0:
        print('\n'+'You lost all your 20 sonar devises.')
        print('The remaining chests were in: '+ str(ocean.showDup()))
    
main()  