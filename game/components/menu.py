import pygame
from game.components.buttons import Button
from game.utils.constants import FONDO_INICIO, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    SCREEN_HALF_HEIGHT = SCREEN_HEIGHT / 2
    SCREEN_HALF_WIDHT = SCREEN_WIDTH / 2
    
    def __init__(self, screen):
        self.screen = screen
        self.image_Fondo = FONDO_INICIO
        self.image_Fondo = pygame.transform.scale(self.image_Fondo,(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image_Fondo.get_rect(topleft = (0,0))
        self.button = Button(screen)
        
        self.icon = ICON
        self.icon = pygame.transform.scale((ICON), (200, 250))
        self.rectIcon = self.icon.get_rect(center = (SCREEN_WIDTH /2, (SCREEN_HEIGHT / 2) - 180))

    def update(self, game):
        pygame.display.update()
        self.handle_events(game)
    
    def draw_Game_Over(self,message):
        font = pygame.font.Font(FONT_STYLE, 70)
        text = font.render(message, False, 'Red')
        text_rect = text.get_rect(center = ((SCREEN_WIDTH /2), (SCREEN_HEIGHT / 2)+10))
        self.screen.blit(text, text_rect)



    def update_Icon(self):
        self.rectIcon.x +=1    
        if(self.rectIcon.left > (SCREEN_WIDTH /2) + 100 ) :
            self.rectIcon.x -=1
        if self.rectIcon.left < 100 :
            self.rectIcon.x +=1

    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            if (self.button.button_Play() and game.death_counter ==0) or (self.button.button_Restart() and game.death_counter >0):
                game.run()

    def draw_Image_Fondo(self):
        self.screen.blit(self.image_Fondo, self.rect)

    def update_message(self, message):
        self.text = self.font.render(message, False, 'Black')
        self.text.get_rect(center = (self.SCREEN_HALF_WIDHT, self.SCREEN_HALF_HEIGHT))

    def draw_Icono(self):
        self.screen.blit(self.icon,self.rectIcon)


