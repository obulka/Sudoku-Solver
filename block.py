import pygame
from consts import *          

"""Each square of the sudoku puzzle is represented by a Block"""
class Block(pygame.sprite.Sprite):
    size = BLOCK_SIZE - LINE_PX - 2*LINE_PX/9 #the actual size of the white area
    
    """initialize a block with no number and white colour"""
    def __init__(self):
        super(Block, self).__init__()
        
        #setable properties
        self.number = ''
        self.colour = WHITE
        self.font_colour = BLACK

        #constant properties
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
    
    """Change the colour of the block to green if it is selected"""
    def select(self):
        self.colour = GREEN
        self.update()
    
    """Returns the colour to white when deselecting"""    
    def deselect(self):
        self.colour = WHITE
        self.update()
    
    """
    Set the number to be displayed on a block
    @param number: the number to display
    @param colour: the font colour used to print the number
    """    
    def setNum(self, number, colour):
        if number >= 1 and number <= 9:
            self.number = number
            self.font_colour = colour
        
        self.update()
    
    """@returns the number that is associated with the block"""        
    def getNum(self):
        return self.number
    
    """Delete the number on a block"""
    def removeNum(self):
        self.number = ''
        self.update()
    
    """Updates the image with the block's current colour and number"""    
    def update(self):
        self.image.fill(self.colour)
        text = pygame.font.SysFont('Calibri', Block.size, True, False).render(str(self.number), True, self.font_colour)
        self.image.blit(text, [Block.size/2 - text.get_rect().width/2,Block.size/2 - text.get_rect().height/2])   
        
        