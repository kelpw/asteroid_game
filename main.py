import pygame
from constants import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    def fill(self,color):
        self.color = color
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False        
        screen.fill((0, 0, 0))  # Fill screen black
        pygame.display.flip()   # Update the screen

    pygame.quit()

if __name__ == "__main__":
    main()

