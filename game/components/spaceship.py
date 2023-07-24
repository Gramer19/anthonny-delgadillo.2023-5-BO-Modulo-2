from game.components.bullet.bullet import Bullet
from game.utils.constants import DEFAULT_TYPE, NAVE_STAR, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, SPACESHIP, SPACESHIP_SHIELD, STAR_TYPE
import pygame
from pygame.sprite import Sprite


class Spaceship(Sprite):
    SPACESHIP_WIDTH = 50
    SPACESHIP_HEIGHT = 70
    SPACESHIP_POS_X = SCREEN_WIDTH / 2
    SPACESHIP_POS_Y = 500
    MOVE = 10

    def __init__(self): 
        self.image_spaceship = {DEFAULT_TYPE:SPACESHIP, SHIELD_TYPE:SPACESHIP_SHIELD, STAR_TYPE:NAVE_STAR}
        self.image = self.image_spaceship[DEFAULT_TYPE]
        self.image = pygame.transform.scale(self.image,(self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom =(self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
        self.type = 'player'
        self.pressed = False
        self.has_power_up = False #tiene poder?
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.points_extra = 0

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
            if self.rect.y <= self.SPACESHIP_POS_Y:
                self.rect.y += self.MOVE
        elif user_input[pygame.K_SPACE]:
            self.shoot(game)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def shoot(self, game):
        bullet = Bullet(self)
        game.bulletManager.add_bullet(bullet)
    
    def reset(self):
        self.rect = self.image.get_rect(midbottom =(self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
    
    def set_image(self,type_image = DEFAULT_TYPE):
        self.power_up_type = type_image
        self.image = self.image_spaceship[self.power_up_type]
        self.image = pygame.transform.scale(self.image,(self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
