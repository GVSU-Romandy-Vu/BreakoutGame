#Refer to modules as titled, what could go wrong?
import pygame as Pygame
import random as Random

#HOVERING over the INSTANCE variables should have DESCRIPTIONS (for VScode at least).
#IF the INSTANCE variables has NONE, MAYBE the new object has a new instance variable from function.

#TODO: FIGURE OUT COLLISION RETURNS 

#Parameter of the class is the parent.
class Game(Pygame.sprite.Sprite):
    """""""""""""""""""""""""""""""""""""""
    This class serves as the breakout game session
     and contains the elements of the game such as a
     paddle, ball, bricks, and an overlay. 
    """""""""""""""""""""""""""""""""""""""""""""
    #Instance variables are declared in constructor (Should be.)

    def __init__(self, screen_width = 800, screen_height = 600):
        """""""""""""""""""""""""""""""""""""""
        The constructor for the Game class.

        Keyword argument:
        screen_width: The screen width.
        screen_height: The screen height.
        """""""""""""""""""""""""""""""""""""""
        
        Pygame.init()

        self.__screen_width = screen_width
        """Holds the width of the screen"""

        self.__screen_height = screen_height
        
        self.__running = False
        """Used to determine if the game should end."""

        self.__screen = Pygame.display.set_mode((screen_width,screen_height))
        """Determines size of game window."""

        self.__clock = Pygame.time.Clock()
        """Serves as a buffer for the next frame."""

        self.__bricks = self.Pygame.sprite.Group()
        """Container to hold 'Brick' objects."""

        self.__ball = self.Pygame.sprite.Group()
        """Variable to reference a 'Ball' object."""

        self.__paddle = self.Pygame.sprite.Group()
        """Variable to reference the 'Paddle" object."""

        self.__overlay = self.sprite.Group()
        """Variable to reference the Overlay (text)."""

    
    def run(self):
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        The procedures of how the game should operate.
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        while self.__running:

            #Gets a list of the user input.
            events = Pygame.event.get()

            #Read through event list and act accordingly.
            for event in events:
                if event.type == Pygame.QUIT:
                    self.__running = False
                    Pygame.quit()
                    exit()
                #FIXME: COmplete
                elif event.type == """Move left""":

                    pass

                elif event.type == """Move right""":
                    pass

                elif event.type == """Launch ball""":
                    if self.__start == True:
                        #FIXME
                        pass
                    else:
                        pass

            #Update the logical details of the objects in the game.
            self.__bricks.update()
            self.__ball.update()
            self.__paddle.update()
            self.__overlay.update()
            
            #Get a empty frame to draw the new state of the objects in the game.
            self.__screen.fill( (255, 255, 255) )
            self.__ball.draw(self.__screen)
            self.__paddle.draw(self.__screen)
            self.__bricks.draw(self.__screen)
            self.__overlay.update()

            #Load the drawn frame to the screen?
            Pygame.display.flip()

            #Give the player time to react before loading a new frame.
            self.__clock.tick(60)
    
    def set_running(self, is_running = True):
        """""""""""""""""""""""""""""""""""""""""""""
        Setter method to set if the game is running.

        Keyword arguments:

        is_running: If the game should be running.
        'True' for yes, 'False' for no, else
        errors occurs? (default: True) 
        """""""""""""""""""""""""""""""""""""""""""""
        self.__running = is_running

    def add_bricks(self, amount_per_row = 5, num_rows = 3, height_coverage = .25):
        """""""""""""""""""""""""""""""""""""""""""""
        Method to add bricks to the game. Automatically
        sets the size and position of the bricks

        Keyword arguments:
        amount_per_row: Number of bricks per row (default 10).
        num_rows: Number of brick rows (default 3).
        height_coverage: Percentage in decimal of the height to be
        cover (default .25).

        """""""""""""""""""""""""""""""""""""""""""""

        #Determine dimension of brick objects
        brick_width = self.__screen_width / amount_per_row
        brick_height = (self.__screen_height * height_coverage) / num_rows

        #Helps determine position of bricks
        x_offset = brick_width / 2
        y_offset = brick_height / 2

        for row in range(0, num_rows):
            #FIXME: Issue might occur here.
            y_pos = self.__screen_height - ((row * brick_height) + y_offset)

            for amount in amount_per_row:
                x_pos = self.__screen_width + (amount * brick_width + x_offset)
                self.__bricks.add(Brick(brick_width, brick_height, x_pos, y_pos))

    def add_paddle(self, width_coverage = .1, y_loc = .1):
        """"""""""""""""""""""""""""""""""""""""
        Method to add a paddle to the game.

        Keyword argument:
        width_coverage: A percentage of the
        screen-width that a paddle should take up
        (default .1 [10%]).

        y_loc: A percentage to determine how high
        the paddle is based on the screen height.
        For example a screen height of 600 with
        y_loc will place the paddle at y position
        60 (screen height * y_loc = 600 * .1).

        """""""""""""""""""""""""""""""""""""""""
        width = self.__screen_width * width_coverage
        self.__ball.add(Ball(width))
    



class Ball(Pygame.sprite.Sprite):
    """""""""""""""""""""""""""""""""""""""""""""""""""
    The class serves as the ball in the Breakout game.
    """""""""""""""""""""""""""""""""""""""""""""""""""
    def __init__(self, width = 80):
        """""""""""""""""""""""""""""""""""""""""""""
        Ball class constructor.
        """""""""""""""""""""""""""""""""""""""""""""
        Pygame.sprite.Sprite(self)

        self.__x_velocity = 0
        """Ball object's horizontal velocity."""
        
        self.__y_velocity = 0
        """Ball object's vertical velocity."""



        #FIXME: Create image and rect (need to be private) and add sound effect
    
    def update():
        #FIXME: Update needs to check collisions, move ball and direction
        pass



class Paddle(Pygame.sprite.Sprite):
    def __init__(self):
        Pygame.sprite.Sprite(self)
        #FIXME: Set rect and image
        self.__velocity = 0
        #FIXME:
        self.__width = 50

    #FIXME: Finish method
    def update():
        pass

class Brick(Pygame.sprite.Sprite):

    def __init__(self, width, height, x_position, y_position):
        Pygame.sprite.Sprite.__init__(self)
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
class Overlay(Pygame.sprite.Sprite):
    
    def __init__(self):
        Pygame.sprite.Sprite.__init__(self)
        #FIXME: Create text and store into image (rectangle also)

        self.__lives = 5
        self.__score = 0
    
    def get_lives(self):
        """""""""""""""""""""""""""""""""""""""
        Getter method for the player's lives.
        """""""""""""""""""""""""""""""""""""""
        return self.__lives

    def get_score(self):
        """""""""""""""""""""""""""""""""""""""
        Getter method for the player's score.
        """""""""""""""""""""""""""""""""""""""
        return self.__score

    def decrement_lives(self, amount = -1):
        self.__lives -= amount
    

    def increment_score(self, amount = 25):
        self.__score += amount

    
    
    def update():
        #FIXME: Finish method
        pass




