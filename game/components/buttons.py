import pygame
from pygame.sprite import Sprite

from game.utils.constants import BUTTON_PLAY, BUTTON_RESTART, SCREEN_HEIGHT, SCREEN_WIDTH

class Button(Sprite):
    BOTTON_WIDHT = 200
    BOTTON_HEIGHT = 60
    def __init__(self,screen):
        self.screen = screen
        self.image_Button_Play = BUTTON_PLAY
        self.image_Button_Restart = BUTTON_RESTART
        self.image_Button_Play = pygame.transform.scale(self.image_Button_Play,(self.BOTTON_WIDHT, self.BOTTON_HEIGHT))
        self.image_Button_Restart = pygame.transform.scale(self.image_Button_Restart,(self.BOTTON_WIDHT, self.BOTTON_HEIGHT))
        self.rect_Play = self.image_Button_Play.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.rect_Restart = self.image_Button_Restart.get_rect(center = (SCREEN_WIDTH / 2, 230))

    def draw_Button_Play(self):
        self.screen.blit(self.image_Button_Play, self.rect_Play)
    
    def button_Play(self):
        run = False
        pos_mouse = pygame.mouse.get_pos() 
        if self.rect_Play.collidepoint(pos_mouse): 
            if pygame.mouse.get_pressed()[0] : 
                print("start")
                run = True
        return run

    def draw_Button_Restart(self):
        self.screen.blit(self.image_Button_Restart, self.rect_Restart)

    def button_Restart(self):
        run = False
        pos_mouse = pygame.mouse.get_pos() 
        if self.rect_Restart.collidepoint(pos_mouse): 
            if pygame.mouse.get_pressed()[0]: 
                print("reset")
                run = True
        return run

