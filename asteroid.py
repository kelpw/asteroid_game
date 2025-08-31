import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),  # white
            (int(self.position.x), int(self.position.y)),  # convert Vector2 -> tuple
            self.radius,
            2  # line width
        )

    def update(self, dt):
        # Move in a straight line at constant speed
        self.position += self.velocity * dt