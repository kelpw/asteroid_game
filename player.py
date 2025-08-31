from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y, rotation=0):
        super().__init__(x, y, PLAYER_RADIUS, rotation)
    # in the player class
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]        
    
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
           self.rotation -= PLAYER_TURN_SPEED * dt #turn left
        if keys[pygame.K_d]:
           self.rotation += PLAYER_TURN_SPEED * dt #turn right
    
