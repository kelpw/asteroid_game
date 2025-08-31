import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),  # white
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt
    
    def collision(self, other):
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)
