import pygame as Pygame
import random as Random

#HOVERING over PRIVATE INSTANCE variables should have DESCRIPTIONS (for VScode at least).
#IF the INSTANCE variables has NONE, MAYBE the new object has a new instance variable from function.

#TODO: FIGURE OUT COLLISION RETURNS 
#TODO: Work on overlay, MAX_SCORE


class Game:
    """""""""""""""""""""""""""""""""""""""""""""""""""
    This class serves as the breakout game session
     and contains the elements of the game
      such as a paddle, ball, bricks, and an overlay.
    """""""""""""""""""""""""""""""""""""""""""""""""""
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
        """Variable to reference the 'Paddle' object."""

        self.__overlay = self.sprite.Group()
        """Variable to reference the Overlay (text)."""

        self.__lives = 5
        """Holds the player's lives to determine if game has ended."""

        self.__score = 0
        """Holds the player's score."""

        self.__max_score = 0

    
    
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
                elif event.type == """Hidden keystroke""":
                    pass

            #Update the logical details of the objects in the game.
            self.__bricks.update()
            self.__ball.update(width = self.__screen_width, height = self.__screen_height)
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
                brick = Brick(brick_width, brick_height, x_pos, y_pos)
                self.__bricks.add(brick)
                self.__max_score += brick.get_health

    

    def add_paddle(self, width_coverage = .1):
        """"""""""""""""""""""""""""""""""""""""
        Method to add a paddle to the game.

        Keyword argument:
        width_coverage: A percentage of the
        screen-width that a paddle should take up
        (default .1 [10%]).

        """""""""""""""""""""""""""""""""""""""""
        width = self.__screen_width * width_coverage
        self.__paddle.add(Paddle(screen_width = self.__screen_width, screen_height = self.__screen_height, width = width))

    

    def add_ball(self):
        """""""""""""""""""""""""""""""""""""""""""""""
        Method to add the ball to the game.
        """""""""""""""""""""""""""""""""""""""""""""""
        self.__ball.add(Ball())



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



    def decrement_lives(self, amount = 1):
        """""""""""""""""""""""""""""""""""
        Decrements the lives of the player.

        Keyword argument:
        
        amount: The amount to decrement by
        (default 1).
        """""""""""""""""""""""""""""""""""
        self.__lives -= amount
    


    def increment_score(self, amount = 25):
        """""""""""""""""""""""""""""""""""""""
        Increments the score of the player.

        Keyword argument:
        amount: The amount to increment by
        (default 25).
        """""""""""""""""""""""""""""""""""""""
        self.__score += amount

    
    


#Parameter of the class is the parent.
class Ball(Pygame.sprite.Sprite):
    """""""""""""""""""""""""""""""""""""""""""""""""""
    The class serves as the ball in the Breakout game.
    """""""""""""""""""""""""""""""""""""""""""""""""""
    def __init__(self, screen_width = 800, screen_height = 600):
        """""""""""""""""""""""""""""""""""""""""""""
        Ball class constructor.
        """""""""""""""""""""""""""""""""""""""""""""
        
        #Call Constructor of the parent class
        #FIXME: If issues occur, try replacing parent call with: 'Pygame.sprite.Sprite(self)'
        super().__init__()
        
        self.__x_velocity = 1
        """Ball object's horizontal velocity."""
        
        self.__y_velocity = 1
        """Ball object's vertical velocity."""

        #Leave image and rect and public since they are inherited from pygame.
        #No pop-up however.

        #Create the visual of the ball object.
        self.image = Pygame.surface((40, 40))
        
        #Parameters for circle (image, color, XY coordinates relative bottom left of boundary, radius)?
        Pygame.draw.circle(self.image, (0, 0, 0), (20,20), 20)
        """The visual representation of the object."""

        #self.__sfx = Pygame.mixer.Sound()
        """The sound effect when the ball hits something""" 

        
        #Create the boundary (hit box) of the ball object
        self.rect = self.image.get_rect()

        #Sets the XY coordinate of the ball object relative from the bottom-left of the display?
        #Half of width
        self.rect.x = screen_width / 2

        #15% of height (10% of height (Y  Coord of [height * .1]) is where paddle is located by default)
        self.rect.y = screen_height * .15

    

    def update(self, width = 800, height = 600, coll_group_1 = None, coll_group_2 = None):
        """""""""""""""""""""""""""""""""""""""""""""""""""
        Updates position of ball based on velocity and
        velocity based on collisions. This will also play
        a sound effect if any changes to the ball's velocity
        occur (indicating a collision w/ a paddle, border, or brick)

        Returns a bool value if the ball hits the bottom of
        the window. (Assists with the decrementing of the
        player's lives)

        Keyword arguments:
        width: screen width (default 800).
        height: Screen height (default 600).
        coll_group_1: A collision group. For this module,
        it is the 'Paddle' group (default = None).
        coll_group_2: Another collision group. For this module,
        it is the 'Brick' group (default = None).
        """""""""""""""""""""""""""""""""""""""""""""""""""

        #Used to notify if Game system if life should be decremented.
        modify_life = False

        #Used to determine if sound should play based on any collisions.
        play_sound = False

        self.rect.x += self.__x_velocity
        self.rect.y += self.__y_velocity

        #Check if ball hit the boundaries of the screen.
        if self.rect.x <= 0 or self.rect.x >= width:
            self.__x_velocity = -self.__x_velocity
            play_sound = True
        
        if self.rect.y <= 0 or self.rect.y >= height:
            #Check if life should be decremented based on the ball reach to the bottom.
            if self.rect.y <= 0:
                modify_life = True
            self.rect.y = -self.__y_velocity
            play_sound = True
        
        #Get and check collisions groups
        if coll_group_1 == None:
            pass
        else:
            collisions1 = Pygame.sprite.spritecollide(self, coll_group_1, False)
            self.rect.y = -self.__y_velocity
            self.__x_velocity = -self.__x_velocity
            play_sound = True
        
        if coll_group_2 == None:
            pass
        else:
            collisions1 = Pygame.sprite.spritecollide(self, coll_group_1, False)
            self.rect.y = -self.__y_velocity
            self.__x_velocity = -self.__x_velocity
            play_sound = True

        if play_sound:
            #FIXME: REmove commment once sound effect has been added.
            #self.__sfx.play()
            pass

        return modify_life



class Paddle(Pygame.sprite.Sprite):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    The class is the Paddle that the player controls to reflect the ball.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def __init__(self, screen_width = 800, screen_height = 600, width = 60):
        """""""""""""""""""""""""""
        The constructor for the Paddle class.
        
        Keyword arguments:
        width: The width of the paddle.
        """""""""""""""""""""""""""
        Pygame.sprite.Sprite(self)
        self.__velocity = 3
        """The velocity of the Paddle used to calculate it's next position"""

        self.image = Pygame.Surface((width, 10))
        self.image.fill(0, 0, 0)

        self.__screen_width = screen_width
        """Used to prevent the paddle from moving off-screen."""
        
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height * .1



    def update(self, shift_amt = 0):
        """""""""""""""""""""""""""""""""""""""
        Updates the position of the paddle.

        Keyword argument:
        
        shift_amt: How many times to move in a
        certain direction. A positve indicates
        a shift to the right while the negative
        indicates a shift to the left (if
        applicable).
        """""""""""""""""""""""""""""""""""""""
        #FIXME: If it doesn't stop at the left-right boundary
        if self.rect.x <= 0 or self.rect.x >= 800:
            pass
        else:
            self.rect.x += self.__velocity * shift_amt




class Brick(Pygame.sprite.Sprite):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    The class serves as the bricks in the Breakout game where the player
    can get points everytime they collide the ball with a brick.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def __init__(self, width, height, x_position, y_position):
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Constructor to create the brick.

        Keyword arguments:
        width: the width of the brick.
        height: The height of the brick.
        x_position: the horizontal coordinates for the center of the brick.
        y_position: the vertical coordinates for the center of the brick.
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        Pygame.sprite.Sprite.__init__(self)
        #FIXME: Create image and rectangle
        random = Random.randint
        red = random(0, 255)
        green = random(0, 255)
        blue = random(0, 255)
    
        self.__health = 766 - red - green - blue
        """The health of the brick."""

        self.image = Pygame.Surface(width, height)
        self.image.fill ((red, green, blue))
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position


    
    def decrement_health(self, amount = 25):
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Decrements the brick's health based on the given amount.
        It will also move the brick out of the display if the brick's
        health is less than 0. (To be used as a private/helper method.)

        Keyword arguments:
        amount: The amount to decrement the health by (default 25).
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.__health -= amount
        if self.__health <= 0:
            #Removes object by moving it out of the boundary and decrease size
            self.rect.x = -500
            self.rect.y = -500
            self.image = Pygame.Surface((0,0))
            self.rect.image.get_rect()

    #FIXME: Finish method
    def update(self, coll_group_1 = None):
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Detects any collision with the group stated in the parameters
        and updates the brick's health if a collision occurs. If no
        group is specified, the method does nothing.

        Returns a bool value if a collision with the specified group
        occurs.

        Keyword arguments:
        coll_group_1: The group to that is being check if a collision occurs
        (default None).
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        #Return value.
        ball_collision = False


        if coll_group_1 == None:
            pass
        else:
            collisions = Pygame.sprite.spritecollide(self, coll_group_1, False)
            if collisions:
                self.decrement_health()
                ball_collision = True
        
        return ball_collision

    def get_health(self):
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Returns the health of the given brick.
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        #FIXME:
        return self.__health
    


#FIXME: Figure if score and health is needed (might be in Game class)
class Overlay(Pygame.sprite.Sprite):
    
    def __init__(self):
        Pygame.sprite.Sprite.__init__(self)
        #FIXME: Create text and store into image (rectangle also)

    
    
    def update():
        #FIXME: Finish method
        pass




