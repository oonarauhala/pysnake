import pygame
from random import randint

class Player:
    def __init__(self):
        # Init player starting status
        self.speed = 1
        self.direction = "right"
        self.score = 0
        self.player_colour = (255, 255, 255)
        self.p_x, self.p_y = 100, 250
        self.p_width, self.p_height = 10, 10

class Treat:
    def __init__(self):
        self.treat_colour = (255, 0, 0)
        self.t_width, self.t_height = 5, 5
        self.t_x = self.throw_treat()
        self.t_y = self.throw_treat()

    def throw_treat(self):
        self.t_x = randint(0,500)
        self.t_y = randint(0,500)
    
class Snake:
    # Init game
    def __init__(self):
        pygame.init()

        # Init player
        self.player = Player()

        # Init first treat
        self.treat = Treat()
        self.treat.throw_treat()

        # Init screen size and colour
        self.screen = pygame.display.set_mode((500, 500))
        self.screen_colour = (0, 0, 0)
        pygame.display.set_caption("PySnake")
        self.screen_max_width = self.screen.get_width() - self.player.p_width
        self.screen_max_height = self.screen.get_height() - self.player.p_height

        # Start main loop
        self.main_loop()

    def main_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.event()
            self.move()
            self.draw()
            clock.tick(60)
            
    # Change player coordinates
    def move(self):
        if self.player.direction == "right" and self.player.p_x <= self.screen_max_width:
            self.player.p_x += self.player.speed
        if self.player.direction == "left" and self.player.p_x >= 0:
            self.player.p_x -= self.player.speed
        if self.player.direction == "up" and self.player.p_y >= 0:
            self.player.p_y -= self.player.speed
        if self.player.direction == "down" and self.player.p_y <= self.screen_max_height:
            self.player.p_y += self.player.speed

    # Draw screen
    def draw(self):
        self.screen.fill(self.screen_colour)
        # Player
        pygame.draw.rect(self.screen, self.player.player_colour, pygame.Rect(self.player.p_x, self.player.p_y, self.player.p_width, self.player.p_height))
        # Treat
        pygame.draw.rect(self.screen, self.treat.treat_colour, pygame.Rect(pygame.Rect(self.treat.t_x, self.treat.t_y, self.treat.t_width, self.treat.t_height)))
        pygame.display.flip()
            
    # Check for events & react
    def event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.direction = "up"
                    if event.key == pygame.K_RIGHT:
                        self.player.direction = "right"
                    if event.key == pygame.K_LEFT:
                        self.player.direction = "left"
                    if event.key == pygame.K_DOWN:
                        self.player.direction = "down"


Snake()



