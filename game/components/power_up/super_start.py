import pygame
from pygame.sprite import Sprite

from game.components.power_up.power_up import PowerUp
from game.utils.constants import STAR, STAR_TYPE

class SuperStar(PowerUp):

    def __init__(self):
        super().__init__(STAR,STAR_TYPE)
        self.ponts_extra = 0
    
    def points(self):
        self.ponts_extra +=5

