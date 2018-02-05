import pygame
from block import Block
from consts import BLOCK_SIZE, LINE_PX, BLACK, RED

"""Represents a Sudoku puzzle and contains methods to handle solving it"""
class Board():
    """Sets up a puzzle with all blocks empty and divides it into rows, columns, and sections"""
    def __init__(self):
        self.spriteList = pygame.sprite.Group()
        self.rows = []
        self.columns = []
        self.sections = []
        self.selected_block = []
        
        #make rows
        tmp = []
        xNext = LINE_PX/2
        yNext = LINE_PX/2
        for i in range(9):
            for j in range(9):
                block = Block()
                    
                block.rect.x = xNext
                block.rect.y = yNext
                
                xExtraSpace = LINE_PX if j == 2 or j == 5 else 0
                xNext = xNext + BLOCK_SIZE + xExtraSpace
                
                self.spriteList.add(block)
                tmp.append(block)
                
            yExtraSpace = LINE_PX if i == 2 or i == 5 else 0
            
            xNext = LINE_PX/2
            yNext = yNext + BLOCK_SIZE + yExtraSpace
            
            self.rows.append(tmp)
            tmp = []
            
        #make columns
        for i in range(9):
            for row in self.rows:
                tmp.append(row[i])
            
            self.columns.append(tmp)
            tmp = []
            
        #make sections
        for i in range(0,7,3):
            for j in range(0,7,3):
                for k in range(3):
                    for l in range(3):
                        tmp.append(self.rows[i+k][j+l])
                self.sections.append(tmp)
                tmp = []
                
        #self.test() #for debugging
                
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
            self.selected_block[0].setNum(num, BLACK)
    
    """Removes the number associated with the selected block if a block is selected"""        
    def deleteSelected(self):
        if len(self.selected_block) > 0:
            self.selected_block[0].removeNum
    
    """Prints all the rows for debugging"""
    def printRows(self):
        for row in self.rows:
            for block in row:
                print str(block.getNum()),
            print "\n"
    
    """Prints all the columns for debugging"""        
    def printCols(self):      
        for col in self.columns:
            for block in col:
                print str(block.getNum()),
            print "\n"
    
    """Prints all the sections for debugging"""
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
        
        #iterate through the entire board
        for row in range(9):
            for col in range(9):
                block = self.rows[row][col]
                num = block.getNum()
                
                #if we find an empty block
                if num == '':
                    possible = 0
                    sec = self.getSection(block)
                    #check all possible numbers
                    for check in range(1,10):                        
                        #check that the number isn't in the same row, column or section
                        if (
                            self.checkNoBlockInListHasNum(self.rows[row], check) and
                            self.checkNoBlockInListHasNum(self.columns[col], check) and
                            self.checkNoBlockInListHasNum(self.sections[sec], check)
                            ):
                            #make sure we only have one possible value, otherwise we move on to the next block
                            if possible != 0:
                                possible = 0
                                break
                            else:
                                possible = check
                    #if only one value was found, we use it and return, otherwise we continue
                    if possible != 0:
                        block.setNum(possible, RED)
                        return True
        return False
    
    """Loads a test puzzle into the board for debuggung"""    
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
                self.rows[row][block].setNum(test[row][block], BLACK)
        
        
        
        
        