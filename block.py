import pygame          

"""
Each square of the sudoku puzzle is represented by a Block
Each block is initialized with a selected and unselected colour in (r,g,b) form
Each block can be selected, unselected, and have a number in the range 1-9 printed on it
"""
class Block(pygame.sprite.Sprite):
    """
    Initialize an unselected block with no number
    @param selectedColour: the (r,g,b) value of the selected block
    @param unselectedColour: the (r,g,b) value of the unselected block
    @param size: the number of pixels on the edge of the block
    """
    def __init__(self, selectedColour, unselectedColour, size):
        super(Block, self).__init__()
        
        #setable properties
        self.number = ''
        
        self.unselected_colour = unselectedColour
        self.selected_colour = selectedColour
        self.font_colour = (0,0,0)
        self.colour = unselectedColour

        #constant properties
        self.size = size
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
    
    """
    Change the colour of the block to green if it is selected
    """
    def select(self):
        self.colour = self.selected_colour
        self.update()
    
    """
    Returns the colour to white when deselecting
    """    
    def deselect(self):
        self.colour = self.unselected_colour
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
    
    """
    @returns the number that is associated with the block
    """        
    def getNum(self):
        return self.number
    
    """
    Delete the number on a block
    """
    def removeNum(self):
        self.number = ''
        self.update()
    
    """
    Updates the image with the block's current colour and number
    """    
    def update(self):
        self.image.fill(self.colour)
        text = pygame.font.SysFont('Calibri', self.size, True, False).render(str(self.number), True, self.font_colour)
        self.image.blit(text, [self.size/2 - text.get_rect().width/2,self.size/2 - text.get_rect().height/2])   
        
        