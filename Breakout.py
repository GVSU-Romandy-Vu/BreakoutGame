import pygame as Pygame
from pygame import mixer
import random as Random

class Game:
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The class that creates the Breakout Game session.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    lives = 5
    """The lives of the player, decrements when a ball reaches
    the bottom of the screen. If lives are 0, the player will lose. A
    static public variable so other classes can access it."""
    score = 0
    """The score of the player, increments when a ball hits a brick.
    A static public variable so other classes can access it."""
    def __init__(self):
        """Constructor of the Game class."""


        #Initalize sound to play sound effect and background music.
        mixer.init()
        self.__running = False
        """Determines if the game should continue or not."""
        self.__screen = Pygame.display.set_mode((800, 600))
        """The size of the game window"""
        self.__clock = Pygame.time.Clock()
        """The time before a new frame is updated to the game window"""
        self.__bricks = Pygame.sprite.Group()
        """A container to hold the bricks class."""
        self.__balls = Pygame.sprite.Group()
        """A container to hold the balls"""
        self.__paddle_group = Pygame.sprite.Group()
        """A container to hold a paddle since updating it needs it in a group."""
        self.__paddle = Paddle()
        """The paddle that the player controls."""
        self.__max_score = 0
        """The max score a player can get. If score == max_score, the game quits."""

        #The background music
        Pygame.mixer.music.load('alex-productions-epic-cinematic-gaming-cyberpunk-reset.mp3')
        #Music source: Epic Cinematic Gaming Cyberpunk | RESET by Alex-Productions | https://www.youtube.com/channel/UCx0_M61F81Nfb-BRXE-SeVA
        #Music promoted by https://www.chosic.com/free-music/all/
        #Creative Commons CC BY 3.0
        #https://creativecommons.org/licenses/by/3.0/

    
    def run(self):
        """""""""""""""""""""""""""""""""""""""
        The procedures to run the breakout game.
        """""""""""""""""""""""""""""""""""""""
        #Start the background music and continuously play it until the program terminates.
        Pygame.mixer.music.play(-1)
        
        #Add the elements of the breakout game to the game.
        self.add_paddle()
        self.add_ball()
        self.add_bricks()

        #Used to update the frame to the display.
        while self.__running:
            events = Pygame.event.get()
            
            #Condition that causes the program to terminate by itself.
            if Game.lives == 0 or Game.score == self.__max_score:
                self.__running = False
                Pygame.mixer.music.stop()
                Pygame.quit()
                exit()

            #Checks for user input.
            for event in events:
                #Condition that causes the program to terminate by the player.
                if event.type == Pygame.QUIT:
                    self.__running = False
                    Pygame.mixer.music.stop()
                    Pygame.quit()
                    exit()
                #Input from the user that causes the paddle to move or a ball to be added.
                if event.type == Pygame.KEYDOWN:
                    if event.key == Pygame.K_SPACE:
                        self.add_ball()
                    if event.key == Pygame.K_RIGHT:
                        self.__paddle.move_right()
                    if event.key == Pygame.K_LEFT:
                        self.__paddle.move_left()
            
            #Update the group information (position, velocity, health)
            self.__balls.update()
            self.__bricks.update()

            #Get a new frame to draw the updated groups.
            self.__screen.fill((255, 255, 255))
            #Draw to groups to the frame.
            self.__paddle_group.draw(self.__screen)
            self.__balls.draw(self.__screen)
            self.__bricks.draw(self.__screen)
            self.show_info()
            #Change frame
            Pygame.display.flip()
            #Creates a buffer so user can react.
            self.__clock.tick(60)

    def set_running(self, value):
        """""""""""""""""""""""""""""""""""""""""
        A setter method to determine if the game
        should run or not.

        Keyword argument:
        value: Value to determine if the game 
        should run or not (bool).
        """""""""""""""""""""""""""""""""""""""""
        self.__running = value

    def add_paddle(self):
        """""""""""""""""""""""""""""""""""""""""
        Adds a paddle to the game.
        """""""""""""""""""""""""""""""""""""""""
        self.__paddle_group.add( self.__paddle )

    def add_ball(self):
        """""""""""""""""""""""""""""""""""""""""
        Adds 1 additional ball to the game session.
        """""""""""""""""""""""""""""""""""""""""
        self.__balls.add(Ball())

    def add_bricks(self):
        """""""""""""""""""""""""""""""""""""""""""""""
        Adds bricks to the game (currently 30)
        """""""""""""""""""""""""""""""""""""""""""""""
        for x in range(0, 10):
            for y in range(0,3):
                brick = Brick(x = x, y= y)
                self.__bricks.add(brick)
                #Get brick health info to determine max_score
                self.__max_score += brick.get_health()


    def get_bricks(self):
        """"""""""""""""""""""""""""""""""""""""""""""
        Returns the game's Brick group. Used to
        help other classes determine collisions.
        """""""""""""""""""""""""""""""""""""""""""""""
        return self.__bricks

    def get_paddle(self):
        """"""""""""""""""""""""""""""""""""""""""""""
        Returns the game's Paddle group. Used to
        help other classes determine collisions.
        """""""""""""""""""""""""""""""""""""""""""""""
        return self.__paddle_group

    def get_balls(self):
        """"""""""""""""""""""""""""""""""""""""""""""
        Returns the game's Ball group. Used to
        help other classes determine collisions.
        """""""""""""""""""""""""""""""""""""""""""""""
        return self.__balls

    def show_info(self):
        """"""""""""""""""""""""""""""""""""""""""""""
        Displays the player's lives and score to the
        screen on the upper left corner.
        """""""""""""""""""""""""""""""""""""""""""""
        #Initalize font.
        Pygame.font.init()
        #Set font details
        font = Pygame.font.SysFont('arial.ttf', 26)
        #Set text information
        text = font.render('Lives: '+str(Game.lives)+'    Score: '+ str(Game.score), True, (0, 0, 0))
        #Set position of text.
        position = text.get_rect()
        position.x = 0
        position.y = 0
        #Add text to display.
        self.__screen.blit(text, position)





#Augment represents the parent class.
class Paddle(Pygame.sprite.Sprite):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    The class is the Paddle that the player controls to reflect the ball.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def __init__(self):
        """"""""""""""""""""""""""""""""""""""""
        Constructor of the Paddle class.
        """""""""""""""""""""""""""""""""""""""""
        #Call parent class constructor
        super().__init__()

        self.__speed = 50
        """The speed that the paddle moves."""

        #"Public" fields because they are inherited from parent.
        #Set dimensions of Paddle and fill in color (black).
        self.image = Pygame.Surface((100, 10))
        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 600 *.85

    def move_left(self):
        """""""""""""""""""""""""""""""""""""""""
        Moves the Paddle to the left if applicable.
        """""""""""""""""""""""""""""""""""""""""
        #Boundary check before changing the position so it doesn't go offscreen.
        if self.rect.x <= 800 and self.rect.x >= 0:
            self.rect.x -= self.__speed
        #Keeps it at horizontal position 0 if at the left edge.
        if self.rect.x < 0:
            self.rect.x = 0
            

    def move_right(self):
        """""""""""""""""""""""""""""""""""""""""
        Moves Paddle to the right if applicable.
        """""""""""""""""""""""""""""""""""""""""
        #Boundary check before changing position (right boundary is determined by screen width - Paddle width)
        #as it checks the Paddle position according to it's left edge.
        if self.rect.x <= 700 and self.rect.x >= 0:
            self.rect.x += self.__speed
        #Keep at horizontal position 700 if at the right edge of screen.
        if self.rect.x > 700:
            self.rect.x = 700

class Brick(Pygame.sprite.Sprite):
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    The class serves as the bricks in the Breakout game where the player
    can get points everytime they collide the ball with a brick.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    balls = None
    """A public global variable to help detect collisions with the ball group."""

    def __init__(self, x, y):
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Constructor for Brick class, which places at
        a location based on it's dimensions.

        Keyword argument:
        x: the column # to place the brick at (0 = left most)
        y: the row # to place the brick at (0 = up most)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        random = Random.randint
        
        super().__init__()
        
        #XY dimension of the Brick
        self.image = Pygame.Surface((80 , 50))
        
        red = random(0, 255)
        green = random(0, 255)
        blue = random(0, 255)

        self.image.fill((red, green, blue))
        self.rect = self.image.get_rect()

        self.rect.x = x * 80
        self.rect.y = y * 50
        
        self.__health = 766 - red - green - blue
        """Health of the brick, if 0, the brick is removed from the screen."""
    
    def get_health(self):
        """""""""""""""""""""""""""
        Getter method to return health of brick.
        """""""""""""""""""""""""""
        return self.__health
    
    def decrement_health(self):
        """""""""""""""""""""""""""""""""""
        Decrements health of the brick by 
        25 (based on score when ball
        collides with a brick). If the brick's
        health is 0, it is removed from the
        screen.
        """""""""""""""""""""""""""""""""""
        self.__health -= 25
        if self.__health <= 0:
            self.rect.x = -800
            self.rect.y = -600

    def update(self):
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Method to apply changes to each brick if there is a collision.
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        collisions = Pygame.sprite.spritecollide(self, Brick.balls, False)
        if collisions:
            #Determines how points to increment based on damage done to brick.
            if self.get_health() >= 25:
                Game.score += 25
            else:
                Game.score += self.get_health()
            
            self.decrement_health()


class Ball(Pygame.sprite.Sprite):
    """""""""""""""""""""""""""""""""""""""""""""""""""
    The class serves as the ball in the Breakout game.
    """""""""""""""""""""""""""""""""""""""""""""""""""

    bricks = None
    """A public static variable to help get brick group"""
    paddle = None
    """A public static variable to help get the paddle group"""

    def __init__(self):
        random = Random.randint
        super().__init__()
        #First element indicates horizontal velocity, 2nd indicates vertical
        self.__velocity = [3, -3]
        #Get the sprite of ball and fill it to the background color.
        self.image = Pygame.Surface((10,10))
        self.image.fill((255, 255, 255))
        #Fill the sprite with a black circle
        Pygame.draw.circle(self.image, (0, 0, 0), (5, 5), 5)
        self.__sfx = Pygame.mixer.Sound("mixkit-arcade-mechanical-bling-210.wav")
        """Sound effect when the ball collides with a paddle, screen edge, or brick."""

        self.rect = self.image.get_rect()
        self.rect.x = random(20, 780)
        self.rect.y = 600 *.8
    
    def update(self):
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Method to update the ball's velocity and position based
        on collision.
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.rect.x += self.__velocity[0]
        self.rect.y += self.__velocity[1]

        #Right boundary is calculated from screen width - ball radius
        if self.rect.x <= 0 or self.rect.x >= 795:
            self.__velocity[0] = -self.__velocity[0]
            self.__sfx.play()
        
        #bottom boundary is calculated from screen height - ball radius
        if self.rect.y <= 0 or self.rect.y >= 595:
            self.__velocity[1] = -self.__velocity[1]
            if self.rect.y >= 595:
                Game.lives -= 1
            self.__sfx.play()

        #Collisions with the ball group
        collisions = Pygame.sprite.spritecollide(self, Ball.bricks, False)
        if collisions:
            self.__velocity[1] = -self.__velocity[1]
            self.__velocity[0] = self.__velocity[0]
            self.__sfx.play()
        
        #Collisions with the paddle group.
        collisions = Pygame.sprite.spritecollide(self, Ball.paddle, False)
        if collisions:
            self.__velocity[1] = -self.__velocity[1]
            self.__velocity[0] = self.__velocity[0]
            self.__sfx.play()
        

#The main method to start the game.
def main():
    game = Game()
    #print(Game.lives)
    game.set_running(True)
    Ball.bricks = game.get_bricks()
    Ball.paddle = game.get_paddle()
    Brick.balls = game.get_balls()
    game.run()

if __name__ == '__main__':
    main()