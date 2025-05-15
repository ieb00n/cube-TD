import pygame
import random
import math
import os

class Flame:
    def __init__(self, cote, speed, screen_height):
        self.x = 0
        self.y = screen_height / 2
        self.cote = cote
        self.vie_max = 1
        self.vie = self.vie_max
        self.speed = speed
        self.mort = False
        self.route = 0
        self.route_suivante = self.route + 1
    
    def calc_position(self, route):
        # Vérifie si la flamme a atteint la fin de la route
        if self.route_suivante >= len(route):
            self.mort = True
            return

        # Récupère les informations sur la route actuelle et la suivante
        current_route = route[self.route]
        next_route = route[self.route_suivante]

        # Vérifie si la flamme a atteint la prochaine route
        if current_route.get_info()[3] == 0:  # Direction droite
            if self.x >= next_route.get_info()[0]:
                self.route += 1
                self.route_suivante += 1
        elif current_route.get_info()[3] == 1:  # Direction haut
            if self.y <= next_route.get_info()[1]:
                self.route += 1
                self.route_suivante += 1
        elif current_route.get_info()[3] == 2:  # Direction bas
            if self.y >= next_route.get_info()[1]:
                self.route += 1
                self.route_suivante += 1

    def move(self, route):
        if self.mort:
            return

        # Vérifie si la flamme a atteint la fin de la route
        if self.route_suivante >= len(route):
            self.mort = True
            return

        if route[self.route_suivante].get_info()[3] == 0:
            if self.x < route[self.route_suivante].get_info()[0]:
                self.x += self.speed
            else:
                self.route += 1
                self.route_suivante += 1
        elif route[self.route_suivante].get_info()[3] == 1:
            if self.y > route[self.route_suivante].get_info()[1]:
                self.y -= self.speed
            else:
                self.route += 1
                self.route_suivante += 1
        elif route[self.route_suivante].get_info()[3] == 2:
            if self.y < route[self.route_suivante].get_info()[1]:
                self.y += self.speed
            else:
                self.route += 1
                self.route_suivante += 1

        # Mise à jour de la position sur la route
        #self.calc_position(route)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_dead(self):
        return self.mort
    
class Basic_flame(Flame):
    def __init__(self, cote, speed, screen_height):
        super().__init__(cote, speed, screen_height)
        image = os.path.join("images", "sprite", "ennemi", "flame_1.png")
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (self.cote, self.cote)).convert_alpha()
    
def create_flame(level, cote, speed, screen_height):
    if level == 1:
        return Basic_flame(cote, speed, screen_height)
