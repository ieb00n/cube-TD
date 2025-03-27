import pygame
import random

import road
import ressource

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
    return running

running = init_game()

route = road.create_road(screen_width, screen_height)

while running:

    # UPDATE



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Vérifie si une touche est pressée
            if event.key == pygame.K_TAB:  # Vérifie si la touche pressée est "Tab"
                running = False



    # DRAW
    
    # affiche l'ecran en vert
    screen.fill((0, 255, 0))

    for road in route:
        road.draw(screen)

    # Rafraichissement de l'écran
    pygame.display.flip()

# Quitter Pygame proprement
pygame.quit()