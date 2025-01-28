import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius , 2)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        self.spawn(self.radius, self.position, self.velocity)

    def spawn(self, radius, position, velocity):
        angle = random.uniform(20, 50)

        a = velocity.rotate(angle)
        b = velocity.rotate(-angle)

        radius -= ASTEROID_MIN_RADIUS
    
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = b * 1.2
        
    def update(self, dt):
        self.position += self.velocity * dt 