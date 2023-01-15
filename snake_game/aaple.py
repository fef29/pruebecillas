from constants import *
import pygame
import random


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("snake_game/resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 25) * SIZE
        self.y = random.randint(0, 15) * SIZE
