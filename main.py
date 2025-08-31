import pygame
from constants import *
from circleshape import *  # Make sure this imports your Player subclass
from asteroid import Asteroid
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()


    running = True
    while running:
        dt = clock.tick(60) / 1000  # Calculate delta time at the start of the loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update player (rotation)
        for obj in updatable:
            obj.update(dt)

        # Clear screen
        screen.fill((0, 0, 0))

        # Draw player
        for obj in drawable:
            obj.draw(screen)

        # Update display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

