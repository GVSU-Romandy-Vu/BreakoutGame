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

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite(self)
        self.__x_velocity = 0
        self.__y_velocity = 0
        #FIXME: Create image and rect
    
    def update():
        #FIXME: Update needs to check collisions, move ball and direction
        pass



class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite(self)
        #FIXME: Set rect and image
        self.__velocity = 0
        #FIXME:
        self.__width = 50

    #FIXME: Finish method
    def update():
        pass

class Brick(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #FIXME: Create image and rectangle
        red = 5
        green = 5
        blue = 5
        self.__health = red + blue + green
    
    def decrement_health(self, amount = 25):
        self.__health -= amount
        if self.__health <= 0:
            #FIXME: Find way to destroy object
            pass

    def set_health(self, health):
        self.__health = health

    #FIXME: Finish method
    def update():
        pass
    


#FIXME: Figure if score and health is needed (might be in Game class)
class Overlay(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #FIXME: Create text and store into image (rectangle also)

        self.__lives = 5
        self.__score = 0

    def set_lives(self, lives = 5):
        self.__lives = lives

    def decrement_lives(self):
        self.__lives -= 1
    
    def set_score(self, score = 0):
        self.__score = score

    def increment_score(self, score = 25):
        self.__score += score
    
    def update():
        #FIXME: Finish method
        pass




