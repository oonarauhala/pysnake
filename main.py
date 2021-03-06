import pygame
from random import randint

class Player:
    def __init__(self):
        # Init player starting status
        self.speed = 1
        self.length = 10
        self.increment = 5
        self.direction = "right"
        self.score = 0
        self.player_colour = (255, 255, 255)
        self.p_x, self.p_y = 100, 250
        self.p_width, self.p_height = 10, 10
        self.coordinates = []
    
    # Stores last known coordinates in self.coordinates according to self.length
    def update_coordinates(self, coordinates: tuple):
        if len(self.coordinates) < self.length:
            self.coordinates.append(coordinates)
        else:
            self.coordinates.append(coordinates)
            self.coordinates = self.coordinates[-self.length:-1]

class Treat:
    def __init__(self):
        self.treat_colour = (255, 0, 0)
        self.t_width, self.t_height = 5, 5
        self.t_x = self.throw_treat()
        self.t_y = self.throw_treat()

    def throw_treat(self):
        self.t_x = randint(0, 495)
        self.t_y = randint(0, 495)
    
class Snake:
    # Init game
    def __init__(self):
        pygame.init()
        self.game_end = False

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

        # Game over
        self.end()

    def main_loop(self):
        clock = pygame.time.Clock()
        while not self.game_end:
            self.event()
            self.move()
            self.draw()
            self.collision(self.player_rect, self.treat_rect)
            self.check_boundaries()
            self.player.update_coordinates((self.player.p_x, self.player.p_y))
            clock.tick(60)
        
    def end(self):
        flash = True
        clock = pygame.time.Clock()

        # Init game over -text
        self.font = pygame.font.SysFont("Arial", 50)
        game_over_text_red = self.font.render("GAME OVER!", True, (255, 0, 0))
        game_over_text_white = self.font.render("GAME OVER!", True, (255, 255, 255))
        game_over_position = (80, 50)

        # Init end score -text
        self.scorefont = pygame.font.SysFont("Arial", 28)
        score_position = (210, 250)

        # Init quit -text
        self.quit_newgame_font = pygame.font.SysFont("Arial", 15)
        quit_text = self.quit_newgame_font.render("Press ESC to quit", True, (255, 255, 255))
        quit_text_position = (50, 400)

        # Init new game -text
        newgame_text = self.quit_newgame_font.render("Press SPACE to try again", True, (255, 255, 255))
        newgame_text_position = (300, 400)

        while True:
            # Look for events
            self.event()
            self.screen.fill(self.screen_colour)
            if flash:
                self.screen.blit(game_over_text_white, game_over_position)
                self.screen.blit(self.score_text, score_position)
                self.screen.blit(quit_text, quit_text_position)
                self.screen.blit(newgame_text, newgame_text_position)
                pygame.display.flip()
                flash = False
                clock.tick(10)
            else:
                self.screen.blit(game_over_text_red, game_over_position)
                self.screen.blit(self.score_text, score_position)
                self.screen.blit(quit_text, quit_text_position)
                self.screen.blit(newgame_text, newgame_text_position)
                pygame.display.flip()
                flash = True
                clock.tick(10)


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
    
    # End game if player touches the boundaries
    def check_boundaries(self):
        if self.player.p_x >= self.screen_max_width:
            self.game_end = True
        elif self.player.p_x <= 0:
            self.game_end = True
        elif self.player.p_y <= 0:
            self.game_end = True
        elif self.player.p_y >= self.screen_max_height:
            self.game_end = True

    # Draw screen
    def draw(self):
        self.screen.fill(self.screen_colour)
        # Player
        self.player_rect = pygame.draw.rect(self.screen, self.player.player_colour, pygame.Rect(self.player.p_x, self.player.p_y, self.player.p_width, self.player.p_height))
        self.draw_tail()
        # Treat
        self.treat_rect = pygame.draw.rect(self.screen, self.treat.treat_colour, pygame.Rect(pygame.Rect(self.treat.t_x, self.treat.t_y, self.treat.t_width, self.treat.t_height)))
        # Score
        self.font = pygame.font.SysFont("Arial", 15)
        score_colour = (255, 255, 255)
        score_position = (5, 5)
        self.score_text = self.font.render(" Score: "+ str(self.player.score), True, score_colour)
        self.screen.blit(self.score_text, score_position)
        pygame.display.flip()

    # Draw player tail
    def draw_tail(self):
        for i in range(len(self.player.coordinates)):
            pygame.draw.rect(self.screen, self.player.player_colour, pygame.Rect(self.player.coordinates[i][0], self.player.coordinates[i][1], self.player.p_width, self.player.p_height))

    # Check & react to collision with treat
    def collision(self, player, treat):
        if self.player_rect.colliderect(treat) == 1:
            self.treat.throw_treat()
            self.player.score += 1
            # Increase player length
            self.player.length += self.player.increment
            # Increase speed
            self.player.speed += 0.25

            
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
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_SPACE:
                        Snake()


Snake()


