import pygame
from pygame.sprite import Sprite
from game.components.bullet.bullet import Bullet


######{}  [] ''
from game.utils.constants import DEFAULT_TYPE, SPACESHIP_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Spaceship(Sprite):
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH//2) - SPACESHIP_WIDTH//2
    Y_POS = 500
    MOVE = 10
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP_2,(self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
        
    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= self.MOVE
            else:
                self.rect.left = SCREEN_WIDTH - self.SPACESHIP_WIDTH
        elif user_input[pygame.K_RIGHT]:
            if self.rect.right < SCREEN_WIDTH:
                self.rect.x += self.MOVE
            else:
                self.rect.right = self.SPACESHIP_WIDTH
        elif user_input[pygame.K_UP]:
            if self.rect.top > SCREEN_HEIGHT//2:
                self.rect.y -= self.MOVE
        elif user_input[pygame.K_DOWN]:
            if self.rect.y <= self.Y_POS:
                self.rect.y += self.MOVE
        elif user_input[pygame.K_SPACE]:
            self.shoot(game)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet)

    def set_image(self, size = (SCREEN_WIDTH, SCREEN_HEIGHT), image = (SPACESHIP_2)):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

        
