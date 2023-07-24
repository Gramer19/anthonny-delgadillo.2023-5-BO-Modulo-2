import pygame
from pygame.sprite import Sprite
from game.utils.constants import EXPLOSION_LIST

class Explosion(Sprite):
    def __init__(self, spaceship):
        super().__init__()
        self.image_expl = EXPLOSION_LIST[0]
        self.image_expl = pygame.transform.scale(self.image_expl, (100, 100))
        self.rect = self.image_expl.get_rect(center = spaceship.rect.center)
        self.index = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_speed = 30  # Milliseconds per frame

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.animation_speed:
            self.last_update = now
            self.index += 1
            if self.index >= len(EXPLOSION_LIST):
               self.kill()
            else:
                self.image_expl = EXPLOSION_LIST[self.index]



    def draw(self, screen):
        screen.blit(self.image_expl, self.rect)