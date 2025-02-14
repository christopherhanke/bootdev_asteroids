import pygame
import random
import circleshape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_one_velocity = self.velocity.rotate(random_angle)
        new_two_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_one.velocity = new_one_velocity * 1.2
        new_two.velocity = new_two_velocity * 1.2
        