import pygame
import os

class Road_part:
    def __init__(self, x, y, width, height, image):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load(image), (self.width, self.height)).convert_alpha()

    def get_info(self):
        return [self.x, self.y, self.width, self.height]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

def create_road(screen_width, screen_height):
    road = []
    for i in range(1):
        road.append(Road_part(0, screen_height/2, screen_width, screen_height, os.path.join("cube-TD", "images", "sprite", "road1.png")))
        print(len(road))
    return road

create_road(800, 600)