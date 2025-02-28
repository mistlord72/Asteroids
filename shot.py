import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS



class Shot(CircleShape):  
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        
        self.color = (255, 255, 255)  # White color
        self.velocity = pygame.Vector2(0, 0)
    
    def update(self, dt):
        movement = self.velocity * dt
        self.position += movement
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    
