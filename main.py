import pygame
class Player:
    def __init__(self):
        # Init player starting position, size, colour and speed
        self.speed = 1
        self.direction = "right"
        self.player_colour = (255, 255, 255)
        self.p_x, self.p_y = 100, 250
        self.p_width, self.p_height = 10, 10

class Snake:
    # Init game
    def __init__(self):
        pygame.init()

        # Init screen size and colour
        self.screen = pygame.display.set_mode((500, 500))
        self.screen_colour = (0, 0, 0)

        # Init player
        self.player = Player()

        # Start main loop
        self.main_loop()

    def main_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.event()
            self.move()
            self.draw()
            clock.tick(60)
            
    def move(self):
        if self.player.direction == "right":
            self.player.p_x += self.player.speed
        if self.player.direction == "left":
            self.player.p_x -= self.player.speed
        if self.player.direction == "up":
            self.player.p_y -= self.player.speed
        if self.player.direction == "down":
            self.player.p_y += self.player.speed

    # Draw screen
    def draw(self):
        self.screen.fill(self.screen_colour)
        pygame.draw.rect(self.screen, self.player.player_colour, pygame.Rect(self.player.p_x, self.player.p_y, self.player.p_width, self.player.p_height))
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



