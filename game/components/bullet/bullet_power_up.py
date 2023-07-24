import pygame
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT
class BulletPowerUp(Sprite):
    SPEED = 10
    def __init__(self, spaceship):
        self.image = self.BULLET_TYPES[spaceship.type]
        self.rect = self.image.get_rect(center = spaceship.rect.center)
        self.owner = spaceship.type
        
    def update(self, bullets):
        self.rect.y -= self.SPEED
        if(self.rect.bottom <= 0):
            bullets.remove(self)

    def draw(self, screen,nu):
        screen.blit(self.image, self.rect.x+nu)