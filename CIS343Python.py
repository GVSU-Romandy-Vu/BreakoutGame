import pygame
import random

#WARNING: ABNORMAL DOCUMENTATION STYLE


#Parameter of the class is the parent.
class Game(pygame.sprite.Sprite):
    """""""""""""""""""""""""""""""""""""""
    This class serves as the breakout game session
     and contains the elements of the game such as a
     paddle, ball, bricks, and an overlay. 
    """""""""""""""""""""""""""""""""""""""""""""
    #Instance variables are declared in constructor (Should be.)

    def __init__(self):
        """"""""""""""""""""""""""""""""""""""""
        The constructor for the Game class.
        """""""""""""""""""""""""""""""""""""""""
        
        pygame.init()
        #To create the pygame program itself?

        self.__running = False
        """"""""""""""""""""""""""""""""""""""""
        Private variable used to determine if the game should end.
        """""""""""""""""""""""""""""""""""""""""

class Overlay(pygame.sprite.Sprite):
    """""""""""""""""""""""""""""""""""""""""""""
    
    """""""""""""""""""""""""""""""""""""""""""""



