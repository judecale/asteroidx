import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            for _ in range(2):
                asteroid = Asteroid(self.position.x, self.position.y, self.radius / 2)
                position = self.position
                angle = random.uniform(20, 50)
                speed = random.randint(50, 150)
                asteroid.velocity = pygame.Vector2(1, 0).rotate(angle) * speed * 1.2
                asteroid.add(self.groups())
            self.kill()