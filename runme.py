#!/usr/bin/env python
import pygame
from consts import *
from board import Board


SIZE = (SCREEN_SIZE, SCREEN_SIZE) #screen size in pixels
 
pygame.init()
 
screen = pygame.display.set_mode(SIZE)
 
pygame.display.set_caption("Sudoku Solver")
 
clock = pygame.time.Clock()

def main():
    done = False   
    
    board = Board()
    
    computing = False
    
    while not done:
    # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP and not computing:
                board.click(pygame.mouse.get_pos())
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True               
                elif not computing:
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
                    
                    elif event.key == pygame.K_BACKSPACE:
                        board.deleteSelected()
                        
                    elif event.key == pygame.K_RETURN:
                        computing = True

        if computing:
            solved = board.checkSolved()
            
            computing = False if solved else board.solve()
                
        screen.fill(BLACK)
        
        board.spriteList.draw(screen)

        pygame.display.flip()
        
    clock.tick(FRAME_RATE)
 
    pygame.quit()
    
if __name__ == "__main__":
    main()
