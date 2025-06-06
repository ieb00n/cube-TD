import pygame
import math
import random

class Timer:
    def __init__(self, duree_secondes):
        """
        Constructeur de timer
        Prend en argument la durée
        """
        self.duree_secondes = duree_secondes
        self.temps_initial = pygame.time.get_ticks() / 1000  # Convertir en secondes

    def elapse(self):
        """ Actualise le temps actuel """
        self.temps_actuel = pygame.time.get_ticks() / 1000  # Convertir en secondes

    def timer_ended(self):
        """ Revoie True si la bénédiction en utilisation peut toujours être utilisée, sinon False """
        self.elapse()
        if self.temps_actuel - self.temps_initial >= self.duree_secondes:
            return True
        else:
            return False
        
    def reset(self):
        """ Réinitialise le timer """
        self.temps_initial = pygame.time.get_ticks() / 1000  # Convertir en secondes
        self.temps_actuel = pygame.time.get_ticks() / 1000  # Convertir en secondes

def calc_distance(x1, y1, x2, y2):
    """ Calcule la distance entre deux points """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)