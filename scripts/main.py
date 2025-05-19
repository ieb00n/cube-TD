import pygame
import random
import time
import os

import road as module_road
import ressource
import ennemi as module_ennemi
import tour as module_tour
import icons as module_icons

pygame.init()

# Définition de la taille de la fenêtre de jeu
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
print(screen_width, screen_height)
play_screen = screen_height -  (1/5 * screen_height)

screen = pygame.display.set_mode((screen_width, screen_height))

# Initialisation du framerate pour egaliser la vitesse de jeu sur toutes les machines
framerate = 60
clock = pygame.time.Clock()
dt = clock.tick(framerate)

def init_game():
    
    running = True
    
    route = module_road.create_road(screen_width, screen_height)

    liste_flames = [module_ennemi.create_flame(1, 50, 1, screen_height)]
    vague = 0
    ennemi_max = 10 + 2 * vague
    liste_ennemi_dead = []
    chrono_spawn_ennemi = ressource.Timer(0.8) # timer pour le spawn des ennemis

    liste_tour = []
    liste_object = liste_tour + liste_flames

    chrono_clique_souris = ressource.Timer(0.5) # eviter les clics trop rapides et le spam lors du maintien de la souris

    menu_selection = False

    liste_icone = []

    argent = 100

    return running, route, liste_flames, liste_tour, liste_object, chrono_clique_souris, ennemi_max, liste_ennemi_dead, chrono_spawn_ennemi, vague, menu_selection, liste_icone, argent

def change_vague(vague, liste_flames, liste_ennemi_dead):
    """
    Change la vague d'ennemis
    """
    vague += 1
    ennemi_max = 10 + 2 * vague
    liste_flames = []
    liste_ennemi_dead = []
    return vague, liste_flames, liste_ennemi_dead, ennemi_max

running, route, liste_flames, liste_tour, liste_object, chrono_clique_souris, ennemi_max, liste_ennemi_dead, chrono_spawn_ennemi, vague, menu_selection, liste_icone, argent = init_game()

while running:

    # UPDATE

    liste_object = liste_tour + liste_flames + liste_icone

    # spawn des ennemis
    if len(liste_flames) + len(liste_ennemi_dead) < ennemi_max:
        if chrono_spawn_ennemi.timer_ended():
            liste_flames.append(module_ennemi.create_flame(1, 50, 1, screen_height))
            chrono_spawn_ennemi.reset()
    # changement de vague
    elif len(liste_ennemi_dead) >= ennemi_max:
        if len(liste_flames) == 0:
            vague, liste_flames, liste_ennemi_dead, ennemi_max = change_vague(vague, liste_flames, liste_ennemi_dead)
            chrono_spawn_ennemi.reset()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Vérifie si une touche est pressée
            if event.key == pygame.K_TAB:  # Vérifie si la touche pressée est "Tab"
                running = False

    for i in range(len(liste_flames)-1, -1, -1):
        liste_flames[i].move(route)
        if liste_flames[i].is_dead():
            liste_ennemi_dead.append(liste_flames.pop(i))

    # affiche le panneau de sélection de la tour a niveau de la souris. la tour choisie sera poser a l'emplacement du clic
    if pygame.mouse.get_pressed()[0] and chrono_clique_souris.timer_ended():
        if not menu_selection:
            chrono_clique_souris.reset()
            position_x, position_y = pygame.mouse.get_pos()
            menu_selection = True
            liste_icone = [module_icons.Icone(position_x, position_y, os.path.join("images", "icone", "pompier icone.png") , module_tour.Camion, "Camion de base")] # TODO : pour les prochaine icones, ne pas oublier d'augmenter la valeur de x et/ou y


    # toute les icones de selection de tour
    if menu_selection:
        for icone in liste_icone:
            icone.draw(screen)
            if chrono_clique_souris.timer_ended():
                if icone.is_pressed(position_x, position_y):
                    # si l'icone est pressée, on crée la tour
                    liste_tour, liste_object = module_tour.create_tour(icone.return_tour(), liste_tour, liste_object, position_x, position_y)
                    menu_selection = False
                    
                    # TODO : ne pas oublier de supprimer l'icone
                    liste_icone = []
                    chrono_clique_souris.reset()
                    break

    for tour in liste_tour:
        tour.shoot(liste_flames)


    # DRAW
    
    # affiche l'ecran en vert
    screen.fill((0, 255, 0))

    
    for road in route:
        road.draw(screen)

    for objects in liste_object:
        objects.draw(screen)

    # Rafraichissement de l'écran
    pygame.display.flip()

# Quitter Pygame proprement
pygame.quit()