import pygame
from game.components.bullet.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.spaceship import Spaceship

from game.utils.constants import BG_2, FONT_STYLE, GL, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship ()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu('!READY¡ ! PRESS NOW!⤐', self.screen)
        self.death_count = 0 
        self.score = 0
        self.highest_score = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.score = 0
        self.enemy_manager.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG_2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    
    def show_menu(self):
        self.menu.resset_screen_color(self.screen)
        half_screen_heigth = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            self.menu.update_message('!!HO NO YOUR SHIP EXPLODED¡¡' )
            self.menu.draw(self.screen)
            self.menu.update_message(f'YOUR SCORE: ' + str(self.score)) 
            self.menu.draw(self.screen)
            self.menu.update_message('HIGHEST SCORE: ' + str(self.highest_score))
            self.menu.draw(self.screen)
            self.menu.update_message('TOTAL DEATH: ' + str(self.death_count))
            self.menu.draw(self.screen)

        icon = self.image = pygame.transform.scale(ICON, (150,190))
        self.screen.blit(icon,( half_screen_width - 50, half_screen_heigth - 220))

        self.menu.update(self)
    
    def update_score(self):
        self.score += 1
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, ( 255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)