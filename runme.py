#!/usr/bin/env python
import pygame
from consts import SCREEN_SIZE, FRAME_RATE, BLACK
from board import Board


SIZE = (SCREEN_SIZE, SCREEN_SIZE) #screen size in pixels
 
pygame.init() #initialize the pygame library
 
screen = pygame.display.set_mode(SIZE) #initialize a window
 
pygame.display.set_caption("Sudoku Solver") #set window title
 
clock = pygame.time.Clock()

"""
Creates a blank Sudoku puzzle and lets the user set up initial values
Solves the puzzle after the Enter key is pressed
"""
def main():
    done = False
    
    board = Board() #initialize the puzzle surface
    
    computing = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #exit if the window is closed
                done = True
            elif event.type == pygame.MOUSEBUTTONUP and not computing:
                board.click(pygame.mouse.get_pos()) #select a block on click
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #the user can also quit with the escape key
                    done = True               
                elif not computing:
                    #set the initial puzzle numbers
                    if event.key == pygame.K_1:
                        board.enterNum(1)
                        
                    elif event.key == pygame.K_2:
                        board.enterNum(2)
                        
                    elif event.key == pygame.K_3:
                        board.enterNum(3)
                        
                    elif event.key == pygame.K_4:
                        board.enterNum(4)
                        
                    elif event.key == pygame.K_5:
                        board.enterNum(5)
                        
                    elif event.key == pygame.K_6:
                        board.enterNum(6)
                        
                    elif event.key == pygame.K_7: 
                        board.enterNum(7)
                        
                    elif event.key == pygame.K_8:
                        board.enterNum(8)
                        
                    elif event.key == pygame.K_9:
                        board.enterNum(9)
                    
                    #clear the selected block
                    elif event.key == pygame.K_BACKSPACE:
                        board.deleteSelected()
                    
                    #solve the puzzle 
                    elif event.key == pygame.K_RETURN:
                        computing = True

        if computing:
            solved = board.checkSolved() #check if the board has been solved
            
            computing = False if solved else board.solve() #stop solving if the board is solved otherwise solve another block
                
        screen.fill(BLACK)
        
        board.spriteList.draw(screen) #draw the board to the screen

        pygame.display.flip()
        
    clock.tick(FRAME_RATE)
 
    pygame.quit()
    
if __name__ == "__main__":
    main()
