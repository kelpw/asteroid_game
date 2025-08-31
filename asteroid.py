import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

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

    def split(self):
        self.kill()  # remove the current asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # too small to split further

        # Compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocities rotated in opposite directions
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)

        # Create two new asteroids at the same position with the new radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2 * 1.2