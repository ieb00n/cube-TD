import pygame
import os

class Icone:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.cote = 20
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.cote, self.cote)).convert_alpha()
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))