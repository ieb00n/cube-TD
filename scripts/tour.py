import pygame
import os

import ressource

class Tour:
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

        self.selected = False
    
    def shoot(self, liste_ennemi):
        flames_in_range = []
        for flame in liste_ennemi:
            if ressource.calc_distance(self.x, self.y, flame.x, flame.y) <= self.range:
                flames_in_range.append(flame)
        
        # On tire sur l'ennemi le plus avancé sur la route (pas forcement le premier de la liste car ca changera avec la vitesse)
        if len(flames_in_range) > 0:
            
            target_place = flames_in_range[0].get_info()[4]
            target = flames_in_range[0]
            
            for flame in flames_in_range:
                if flame.get_info()[4] > target_place:
                    target_place = flame.get_info()[4]
                    target = flame
            
            if self.cooldown.timer_ended():
                target.take_damage(self.damages)
                self.cooldown.reset()
    
    def is_selected(self):
        # si la souris clique sur la tour alors "self.selected" = True et ca return False
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.x < mouse_x < self.x + self.cote and self.y < mouse_y < self.y + self.cote:
            if not self.selected:
                self.selected = True
                return True
    
    def unselect(self):
        self.selected = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        # dessine un cercle de rayon la portée de la tour, le cercle est presque transparent
        if self.selected:
            pygame.draw.circle(screen, (255, 0, 0, 50), (int(self.x + self.cote / 2), int(self.y + self.cote / 2)), self.range, 1)

class Camion(Tour):
    def __init__(self, x, y, cote):
        super().__init__(x, y, cote)

# TODO : ne pas oublier de faire les icones de ces tours

def create_tour(type_de_tour, liste_tour, liste_object, x, y):
    """
    Crée une nouvelle tour à la position (x, y) et l'ajoute à la liste des tours.
    """
    new_tour = type_de_tour(x, y, 100)
    liste_tour.append(new_tour)
    liste_object.append(new_tour)

    return liste_tour, liste_object

def remove_tour(liste_tour, liste_object, tour_indice):
    """
    Supprime une tour de la liste des tours et de la liste des objets.
    """
    if tour_indice > 0 or tour_indice < (len(liste_tour) and len(liste_object)):
        liste_tour.pop(tour_indice)
        liste_object.pop(tour_indice)
    return liste_tour, liste_object