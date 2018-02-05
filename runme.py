#!/usr/bin/env python
from gamecontroller import GameController

"""
Initializes and passes control to the game controller
"""
def main():
    game = GameController() #initialize the puzzle surface
    game.play()
     
if __name__ == "__main__":
    main()