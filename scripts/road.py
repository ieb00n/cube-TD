import pygame
import os
import random

import ressource

class Road_part:
    def __init__(self, x, y, cote, image, number):
        self.cote = cote
        self.x = x
        self.y = y
        self.number = number
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (self.cote, self.cote)).convert_alpha()
        self.afficher_number = pygame.font.Font(None, 36).render((str(number)), True, (255, 0, 0))


    def get_info(self):
        return [self.x, self.y, self.width, self.height]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.afficher_number, (self.x + self.cote/2, self.y + self.cote/2))
    


def create_road(screen_width, screen_height):
    route = []

    number = 0
    cote = screen_width / 20

    direction = 0  # 0 pour la droite, 1 pour le haut, 2 pour le bas
    sens_precedente_route = 0  # 0 pour droite, 1 pour haut, 2 pour bas

    position_x = 0
    position_y = screen_height / 2
    longueur_x_route = 0

    # Ajout des deux premières routes horizontales
    for i in range(2):
        route.append(Road_part(position_x, position_y, cote, os.path.join("images", "sprite", "road1.png"), number))
        number += 1
        longueur_x_route += 1
        position_x = cote

    while longueur_x_route < 20:
        # Choix de la direction de la route
        if sens_precedente_route == 0:  # Si la route précédente allait à droite
            direction = random.randint(0, 2)
        elif sens_precedente_route == 1:  # Si la route précédente montait
            direction = random.choice([0, 1])  # Ne peut pas redescendre
        elif sens_precedente_route == 2:  # Si la route précédente descendait
            direction = random.choice([0, 2])  # Ne peut pas remonter

        # Empêcher la route de descendre trop bas
        if position_y >= screen_height - 2 * cote and direction == 2:
            direction = random.choice([0, 1])  # Forcer à aller à droite ou monter

        # Empêcher la route de monter trop haut
        if position_y <= cote and direction == 1:
            direction = random.choice([0, 2])  # Forcer à aller à droite ou descendre

        # Création de la route en fonction de la direction choisie
        if direction == 0:  # Droite
            sens_precedente_route = 0
            position_x += cote
            longueur_x_route += 1
        elif direction == 1:  # Haut
            sens_precedente_route = 1
            position_y -= cote
        elif direction == 2:  # Bas
            sens_precedente_route = 2
            position_y += cote

        # Ajouter la nouvelle partie de route
        if longueur_x_route == 20:
            route.append(Road_part(position_x, position_y, cote, os.path.join("images", "sprite", "last_road.png"), number))
        else:
            route.append(Road_part(position_x, position_y, cote, os.path.join("images", "sprite", "road1.png"), number))
        number += 1

    return route