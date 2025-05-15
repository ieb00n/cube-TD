import pygame
import random
import time

import road
import ressource
import ennemi

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
    
    route = road.create_road(screen_width, screen_height)

    flames = [ennemi.create_flame(1, 50, 1, screen_height)]
    vague = 0


    return running, route, flames

running, route, flames = init_game()

while running:

    # UPDATE



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Vérifie si une touche est pressée
            if event.key == pygame.K_TAB:  # Vérifie si la touche pressée est "Tab"
                running = False

    for flame in flames:
        flame.move(route)
        if flame.is_dead():
            flames.remove(flame)


    # DRAW
    


    # affiche l'ecran en vert
    screen.fill((0, 255, 0))

    for road in route:
        road.draw(screen)

    for flame in flames:
        flame.draw(screen)

    # Rafraichissement de l'écran
    pygame.display.flip()

# Quitter Pygame proprement
pygame.quit()