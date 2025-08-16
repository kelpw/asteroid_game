import pygame
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, rotation=0):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.rotation = rotation
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]        

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(
            screen,
            (255, 255, 255),    # white
            self.triangle(),    # list of 3 points
            2                   # line width
        )

    def update(self, dt):
        # sub-classes must override

        pass


from constants import PLAYER_RADIUS

class Player(CircleShape):
    
    def __init__(self, x, y, rotation=0):
        super().__init__(x, y, PLAYER_RADIUS, rotation)
        


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    
    

    def move(self, dt, forward=True):
        # Create a vector pointing "forward" from the ship
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        if not forward:  # If moving backward
            direction *= -1
        self.position += direction * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
           self.rotation -= PLAYER_TURN_SPEED * dt #turn left
        if keys[pygame.K_d]:
           self.rotation += PLAYER_TURN_SPEED * dt #turn right
        if keys[pygame.K_w]:
            self.move(dt, forward=True)
        if keys[pygame.K_s]:
            self.move(dt, forward=False)
    


