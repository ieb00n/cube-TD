import pygame
import os

import ressource

class Camion:
    def __init__(self, x, y, cote):
        self.x = x - cote / 2
        self.y = y - cote / 2
        
        self.cote = cote

        self.range = 100  # Portée de la tour
        self.cooldown_max = 1
        self.cooldown = ressource.Timer(self.cooldown_max)  # Temps de recharge de la tour
        self.damages = 1  # Dégâts infligés par la tour

        self.image = pygame.image.load(os.path.join("images", "sprite", "tours", "camion de base.png"))
        self.image = pygame.transform.scale(self.image, (self.cote, self.cote)).convert_alpha()
    
    def shoot(self, liste_ennemi):
        for flame in liste_ennemi:
            if ressource.calc_distance(self.x, self.y, flame.x, flame.y) <= self.range:
                if self.cooldown.timer_ended():
                    flame.take_damage(self.damages)
                    self.cooldown.reset()

                    break

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

def create_tour(liste_tour, liste_object, x, y):
    """
    Crée une nouvelle tour à la position (x, y) et l'ajoute à la liste des tours.
    """
    new_tour = Camion(x, y, 100)
    liste_tour.append(new_tour)
    liste_object.append(new_tour)

    return liste_tour, liste_object, chrono_clique_souris

def remove_tour(liste_tour, liste_object, tour_indice):
    """
    Supprime une tour de la liste des tours et de la liste des objets.
    """
    if tour_indice > 0 or tour_indice < (len(liste_tour) and len(liste_object)):
        liste_tour.pop(tour_indice)
        liste_object.pop(tour_indice)
    return liste_tour, liste_object