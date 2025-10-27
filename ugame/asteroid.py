import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Always destroy the current asteroid
        self.kill()
        
        # If asteroid is too small, don't split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate random split angle
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating in opposite directions
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2
        
        # Calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids at current position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set their velocities
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2
