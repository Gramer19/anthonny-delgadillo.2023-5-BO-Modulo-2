import random
import pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp(Sprite):
    POS_ON_X = random.randint(120, SCREEN_WIDTH - 120)

    def __init__(self, image, type):
        self.image = image
        self.image = pygame.transform.scale(self.image,(47, 47))
        self.rect = self.image.get_rect(midtop = (self.POS_ON_X, -70))
        self.type = type
        self.start_time = 0

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed
        if self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    