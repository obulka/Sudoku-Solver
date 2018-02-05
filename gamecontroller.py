import pygame
from block import Block

"""
Represents a Sudoku puzzle and contains methods to handle solving it
"""
class GameController():
    debugMode = True
    
    NAME = "Sudoku Solver"  # Window title
    BLOCK_SIZE = 50         # Block size in pixels
    LINE_PX = 4             # Line width in pixels
    FRAME_RATE = 5
    
    ACTUAL_BLOCK_SIZE = BLOCK_SIZE - LINE_PX - 2*LINE_PX/9 # The actual size of the white area
    SCREEN_SIZE = 9*BLOCK_SIZE + 2*LINE_PX
    
    #RGB
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    
    """
    Sets up a puzzle with all blocks empty and divides it into rows, columns, and sections
    """
    def __init__(self): 
        pygame.init() # Initialize the pygame library
 
        self.screen = pygame.display.set_mode((GameController.SCREEN_SIZE, GameController.SCREEN_SIZE)) # Initialize a window
 
        pygame.display.set_caption(GameController.NAME) # Set window title
 
        self.clock = pygame.time.Clock()
        
        self.done = False
        self.computing = False
        self.solvedObvious = False      # Used by the solving algorithm to track whether or not the obvious solutions have been filled
        
        self.solve_head = [0,0]         # Tracks where the brute force algorithm currently is
        
        self.spriteList = pygame.sprite.Group()
        
        self.rows = []                  # A list of every row
        self.columns = []               # A list of every column
        self.sections = []              # A list of every section
        
        self.selected_block = []        # Contains the block that is currently selected
        
        # Make rows
        tmp = []
        xNext = GameController.LINE_PX/2
        yNext = GameController.LINE_PX/2
        for i in range(9):
            for j in range(9):
                block = Block(GameController.GREEN, GameController.WHITE, GameController.ACTUAL_BLOCK_SIZE)
                    
                block.rect.x = xNext
                block.rect.y = yNext
                
                xExtraSpace = GameController.LINE_PX if j == 2 or j == 5 else 0
                xNext = xNext + GameController.BLOCK_SIZE + xExtraSpace
                
                self.spriteList.add(block)
                tmp.append(block)
                
            yExtraSpace = GameController.LINE_PX if i == 2 or i == 5 else 0
            
            xNext = GameController.LINE_PX/2
            yNext = yNext + GameController.BLOCK_SIZE + yExtraSpace
            
            self.rows.append(tmp)
            tmp = []
            
        # Make columns
        for i in range(9):
            for row in self.rows:
                tmp.append(row[i])
            
            self.columns.append(tmp)
            tmp = []
            
        # Make sections
        for i in range(0,7,3):
            for j in range(0,7,3):
                for k in range(3):
                    for l in range(3):
                        tmp.append(self.rows[i+k][j+l])
                self.sections.append(tmp)
                tmp = []
        
        if GameController.debugMode:        
            self.test()
    
    """
    Contains the main game loop
    Will continue to run until self.done is set to False and will quit after this occurs
    """
    def play(self):
        while not self.done:
            self.processInputs()
            self.processLogic()
            self.draw()       
            
        self.clock.tick(GameController.FRAME_RATE)
     
        pygame.quit()
    
    """
    Processes user input
    Processes all logic that is user dependent
    Current Inputs:
        Click: Select block
        Keys 1-9: Input the number to the selected block
        Back Space: Clear the selected block
        Delete: Clear the entire board
        Return: Solve the puzzle
        Escape: Quit the game
    """
    def processInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exit if the window is closed
                self.done = True
            elif event.type == pygame.MOUSEBUTTONUP and not self.computing:
                self.click(pygame.mouse.get_pos()) # Select a block on click
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # The user can also quit with the escape key
                    self.done = True               
                elif not self.computing:
                    # Set the initial puzzle numbers
                    if event.key == pygame.K_1:
                        self.enterNum(1)
                        
                    elif event.key == pygame.K_2:
                        self.enterNum(2)
                        
                    elif event.key == pygame.K_3:
                        self.enterNum(3)
                        
                    elif event.key == pygame.K_4:
                        self.enterNum(4)
                        
                    elif event.key == pygame.K_5:
                        self.enterNum(5)
                        
                    elif event.key == pygame.K_6:
                        self.enterNum(6)
                        
                    elif event.key == pygame.K_7: 
                        self.enterNum(7)
                        
                    elif event.key == pygame.K_8:
                        self.enterNum(8)
                        
                    elif event.key == pygame.K_9:
                        self.enterNum(9)
                    
                    # Clear entire board
                    elif event.key == pygame.K_DELETE:
                        self.clearBoard()
                        
                    # Clear the selected block
                    elif event.key == pygame.K_BACKSPACE:
                        self.deleteSelected()
                    
                    # Solve the puzzle 
                    elif event.key == pygame.K_RETURN:
                        self.computing = True   
    
    """
    Processes all logic that is user independent
    """
    def processLogic(self):
        if self.computing:
            solved = self.checkSolved() # Check if the board has been solved
            
            self.computing = False if solved else self.solve() # Stop solving if the board is solved otherwise solve another block
            
    """
    Draws self.spriteList onto a black background
    """
    def draw(self):
        self.screen.fill(GameController.BLACK)
        
        self.spriteList.draw(self.screen) # Draw the board to the screen

        pygame.display.flip()
                         
    """
    If the user clicked on a block, this method selects the block
    The selected block will then take numerical input
    @param pos: the position of the mouse when the user clicked
    """
    def click(self, pos):
        clicked_on = [b for b in self.spriteList if b.rect.collidepoint(pos)]
        
        if len(clicked_on) > 0:
            if len(self.selected_block) > 0:
                self.selected_block[0].deselect()
                
            self.selected_block = clicked_on
            self.selected_block[0].select()
    
    """
    Sets the number associated with the selected block if a block is selected
    @param num: the number to display on the selected block
    """
    def enterNum(self, num):
        if len(self.selected_block) > 0:
            self.selected_block[0].setNum(num, GameController.BLACK)
    
    """
    Removes the number associated with the selected block if a block is selected
    """        
    def deleteSelected(self):
        if len(self.selected_block) > 0:
            self.selected_block[0].removeNum
    
    """
    
    """
    def clearBoard(self):
        for row in self.rows:
            for block in row:
                block.removeNum()
        
    """
    Prints all the rows for debugging
    """
    def printRows(self):
        for row in self.rows:
            for block in row:
                print str(block.getNum()),
            print "\n"
    
    """
    Prints all the columns for debugging
    """        
    def printCols(self):      
        for col in self.columns:
            for block in col:
                print str(block.getNum()),
            print "\n"
    
    """
    Prints all the sections for debugging
    """
    def printSecs(self):        
        for sec in self.sections:
            for block in sec:
                print str(block.getNum()),
            print "\n"
    
    """
    Checks whether or not the board is solved
    @returns True if solved, False otherwise
    """
    def checkSolved(self):
        for row in self.rows:
            for block in row:
                if block.getNum() == '':
                    return False
        return True
    
    """
    Finds the index of the section that contains block
    @param block: the block whose section we want to find
    @return: An integer index of the section that contains block and -1 if it is not found
    """
    def getSection(self, block):
        for s in range(9):
            for check_block in self.sections[s]:
                if check_block is block:
                    return s
        return -1
    
    """
    Checks whether or not a block in check_list has a number of check_num
    @param check_list: the list of blocks to check
    @param check_num: the number to check each block against
    @return: False if any block in check_list DOES contain check_num, True if no block contains check_num
    """
    def checkNoBlockInListHasNum(self, check_list, check_num):
        for i in check_list:
            if i.getNum() == check_num:
                return False
        return True
                
    """
    Solves one block on every call and displays it to the screen
    @return: True if a block was solved, False if no solution could be found
    """        
    def solve(self):
        if len(self.selected_block) > 0:
            self.selected_block[0].deselect()
        
        # First we fill in blocks that can only take one possible value
        if not self.solvedObvious:
            # Iterate through the entire board
            for row in range(9):
                for col in range(9):
                    block = self.rows[row][col]
                    num = block.getNum()
                    
                    # If we find an empty block
                    if num == '':
                        possible = 0
                        sec = self.getSection(block)
                        # Check all possible numbers
                        for check in range(1,10):                        
                            # Check that the number isn't in the same row, column or section
                            if (
                                self.checkNoBlockInListHasNum(self.rows[row], check) and
                                self.checkNoBlockInListHasNum(self.columns[col], check) and
                                self.checkNoBlockInListHasNum(self.sections[sec], check)
                                ):
                                # Make sure we only have one possible value, otherwise we move on to the next block
                                if possible != 0:
                                    possible = 0
                                    break
                                else:
                                    possible = check
                        # If only one value was found, we use it and return, otherwise we continue
                        if possible != 0:
                            block.setNum(possible, GameController.RED)
                            return True
            self.solvedObvious = True
        
        # Brute force the rest of the solution
        for guess in range(9):
            pass
        
        return False
    
    """
    Loads a test puzzle into the board for debuggung
    """    
    def test(self):
        test = [[3,6,'',7,'',1,'',5,''],\
                ['',7,4,'','','','','',9],\
                ['','',8,'','','','','',''],\
                ['',5,'',4,3,'',1,'',''],\
                ['','','',2,7,8,'','',''],\
                ['','',9,'',6,5,'',4,''],\
                ['','','','','','',5,'',''],\
                [8,'','','','','',9,3,''],\
                ['',1,'',9,'',3,'',6,4]]
        
        for row in range(9):
            for block in range(9):
                self.rows[row][block].setNum(test[row][block], GameController.BLACK)
        
        
        
        
        