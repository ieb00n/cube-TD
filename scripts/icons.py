import pygame
import os

import tour as module_tour

class Icone:
    def __init__(self, x, y, image_path, class_tour, desciption):
        
        self.cote = 40
        self.x = x - self.cote / 2 # l'icone est centré sur la souris
        self.y = y - self.cote / 2 # l'icone est centré sur la souris
        
        image = image_path # l'image de base et celle de la première icone
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.cote, self.cote)).convert_alpha()

        # description de la tour. cadence, portée, dégâts ... 
        self.description = desciption

        self.class_tour = class_tour
    
    def return_tour(self):
        """
        renvoie la tour a créer
        """
        return self.class_tour
    
    def is_pressed(self):
        """
        Vérifie si l'icone est pressée
        """
        if self.x <= pygame.mouse.get_pos()[0] <= self.x + self.cote and self.y <= pygame.mouse.get_pos()[1] <= self.y + self.cote and pygame.mouse.get_pressed()[0]:
            return True
    
    def draw(self, screen):
        # dessine un carre orange plein avec les bord arondis derrière l'icone
        pygame.draw.rect(screen, (255, 165, 0), (self.x, self.y, self.cote, self.cote), border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.cote, self.cote), 2, border_radius=10)
        screen.blit(self.image, (self.x, self.y))