import pygame
import random
import time

# Initial parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
pygame.font.init()
font = pygame.font.Font(None, 50)

# Colors
WHITE = (255, 255, 255)
BLACK= (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255,165,0)
BLUE = (0,0,255)


# Player class
class player(pygame.sprite.Sprite):
    def __init__(self):
        # Define initial parameters
        self.color = BLUE
        self.width = 50
        self.height= 100
        self.vel = 50
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a solid color block
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Fetch the color block
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT - self.height

    def move(self):
        # Get keyboard input
        keys = pygame.key.get_pressed()

        # Move to the left if its not on the leftmost side
        if keys[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= self.vel

        # Move to the right if its not on the rightmost side
        elif keys[pygame.K_RIGHT]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.vel


#### TODO1: Write a "traffic" class that simulates oncoming traffic 

class traffic(pygame.sprite.Sprite):
    def __init__(self):
        self.color = RED
        self.width = 60
        self.height= 100
        self.vel = 20

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a solid color block
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Fetch the color block
        self.rect = self.image.get_rect()

        # Set the initial positions
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = 0 

    def move(self):
        if self.rect.y < SCREEN_HEIGHT:
            self.rect.y += self.vel
        else: self.rect.y = 0
        self.vel += 0.07       

#### TODO2: Add two traffic subclasses "car" and "truck" with different proportions and velocities

class car(traffic):
    def __init__(self):
        self.color = WHITE
        self.width = 70
        self.height= 90
        self.vel = 15

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a solid color block
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Fetch the color block
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = SCREEN_WIDTH / 4
        self.rect.y = 0 

    def move(self):
        if self.rect.y < SCREEN_HEIGHT:
            self.rect.y += self.vel
        else: self.rect.y = 0
        self.vel += 0.1

class truck(traffic):
    def __init__(self):
        self.color = ORANGE
        self.width = 80
        self.height= 110
        self.vel = 5

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a solid color block
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        # Fetch the color block
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = SCREEN_WIDTH / 8 * 5
        self.rect.y = 0 

    def move(self):
        if self.rect.y < SCREEN_HEIGHT:
            self.rect.y += self.vel
        else: self.rect.y = 0
        self.vel += 0.05

# Display 'game over' and quit the game
def game_over(win):
    win.fill((255, 0, 0))
    text_surface = font.render("Game Over", True, WHITE)
    win.blit(text_surface, (SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.5))
    pygame.display.flip()
    


def run():
    # initialize pygame
    pygame.init()

    # Set display
    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set clock
    clock = pygame.time.Clock()

    # Initialize player and traffic(s)
    player1 = player()
    traffic1 = traffic()
    traffic2 = car()
    traffic3 = truck()
    #TODO: here

    # Create sprite groups
    all_traffic = pygame.sprite.Group()
    all_traffic.add(traffic1)
    all_traffic.add(traffic2)
    all_traffic.add(traffic3)
    #TODO: add traffic(s)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)
    all_sprites.add(traffic1)
    all_sprites.add(traffic2)
    all_sprites.add(traffic3)
    #TODO: add traffic(s)

    # Run the game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
           
        # Move all objects  
        for sprite in all_sprites:
            sprite.move()

        # If player and traffic collides display game over screen
        collision = pygame.sprite.spritecollideany(player1, all_traffic)
        if collision:
            game_over(win)
            time.sleep(2)
            pygame.quit()

        else:
            win.fill((0, 0, 0))
            all_sprites.draw(win)
            all_sprites.update()

        # display changes
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    run()