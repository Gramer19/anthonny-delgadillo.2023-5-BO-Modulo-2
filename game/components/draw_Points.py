import pygame
from game.utils.constants import FONT_STYLE
class DrawPoints():   
    def __init__(self, screen):
        self.screen = screen   
        
    def draw_message_points(self,message,pos_X,pos_Y):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(message, False, 'Lime')
        text_rect = text.get_rect(center = (pos_X, pos_Y))
        self.screen.blit(text, text_rect)