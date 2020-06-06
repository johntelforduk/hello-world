# Hello world that exercises Pygame.

import  pygame
from random import randint

# Define the colors we will use in RGB format.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = [255, 0, 0]
GREEN = [0, 255, 0]

# Set the height and width of the viewport.
screen_size = [800, 600]
target_fps = 50

def random_delta() -> int:
    """Return a random, non-zero integer between -2 and 2."""
    options = [-2, -1, 1, 2]
    return options[randint(0, len(options) -1)]

class Ball:

    def __init__(self):
        self.x = randint(1, screen_size[0])
        self.y = randint(1, screen_size[1])

        self.dx = random_delta()
        self.dy = random_delta()

        self.colour = (randint(0, 255), randint(0, 255), randint(0, 255))

    def render(self, this_screen):
        """Draw the ball on the screen."""
        pygame.draw.circle(this_screen, self.colour, [self.x, self.y], 20, 20)

    def animate(self):
        """Move the ball one-tick."""
        # Move the ball a little bit.
        self.x += self.dx
        self.y += self.dy

        # Bounce if edge of screen hit.
        if self.x <= 0 or self.x >= screen_size[0]:
            self.dx = - self.dx
        if self.y <= 0 or self.y >= screen_size[1]:
            self.dy = - self.dy


pygame.init()  # Initialize the game engine.

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

pygame.display.set_caption('Hello Pygame')  # The game window title.

quit = False

# Create a list of bouncing balls.
balls = []
for i in range(100):
    balls.append(Ball())

while not quit:
    clock.tick(target_fps)

    screen.fill(BLACK)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            quit = True  # Flag that we are done so we exit this loop, and quit the game

    for this_ball in balls:
        this_ball.animate()
        this_ball.render(screen)

    pygame.display.flip()

pygame.quit()




# # Start the Pygame sound system.
# pygame.mixer.init()
# pygame.mixer.set_num_channels(3)  # One channel for laser gun fires, one for explosions.
#
# # Get some game sounds ready, and allocate sound channels for them.
# self.explosion_sound = pygame.mixer.Sound('assets/110115__ryansnook__small-explosion.wav')
# self.laser_sound = pygame.mixer.Sound('assets/341235__sharesynth__laser01.wav')
# self.ship_explosion_sound = pygame.mixer.Sound('assets/235968__tommccann__explosion-01.wav')
# self.explosion_channel = pygame.mixer.Channel(0)
# self.laser_channel = pygame.mixer.Channel(1)
# self.ship_explosion_channel = pygame.mixer.Channel(2)
