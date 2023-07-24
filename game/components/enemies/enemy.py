import pygame
from pygame.sprite import Sprite
import random
from game.components.bullet.bullet import Bullet
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    ENEMY_WIDHT = 50
    ENEMY_HEIGHT = 70
    Y_POS = -(ENEMY_HEIGHT + 5)
    X_POS_RANGE = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    SPEED_ON_Y = random.randint(1,2)
    SPEED_ON_X = random.randint(1,10)
    MOVES = { 0:'left', 1:'right'}
    INITIAL_SHOOTING_TIME = 1000
    FINAL_SHOOTING_TIME = 3000

    def __init__(self,image):
        self.image = image
        self.image = pygame.transform.scale(self.image,(self.ENEMY_WIDHT, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
        self.centro = self.rect.center
        self.direction = self.MOVES[random.randint(0, 1)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 50)
        self.type = 'enemy'
        current_time = pygame.time.get_ticks()
        self.shooting_time = random.randint(current_time + self.INITIAL_SHOOTING_TIME, current_time + self.FINAL_SHOOTING_TIME)


    
    def update(self, enemies, game):        
        self.rect.y += self.SPEED_ON_Y
        self.shoot(game.bulletManager)

        if self.direction == self.MOVES[0]:
            self.rect.x -= self.SPEED_ON_X     
        elif self.direction == self.MOVES[1]:
            self.rect.x += self.SPEED_ON_X

        self.handle_direction()
        if self.rect.top > SCREEN_HEIGHT:
            enemies.remove(self)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_direction(self):
        self.movement_count += 1
        if (self.movement_count >= self.moves_before_change and self.direction == self.MOVES[1]) or self.rect.right >= SCREEN_WIDTH:
            self.direction = self.MOVES[0]
            self.movement_count = 0
            self.moves_before_change = random.randint(20,50)
            
            self.SPEED_ON_X = random.randint(1,10)
            self.SPEED_ON_Y = random.randint(1,2)
                
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[0] or self.rect.left <= 0:
            self.direction = self.MOVES[1]
            self.movement_count = 0
            self.moves_before_change = random.randint(20,50)
            
            self.SPEED_ON_X = random.randint(1,10)
            self.SPEED_ON_Y = random.randint(1,2)
        
    def shoot(self, bulletManager):
        current_time = pygame.time.get_ticks()
        if (self.shooting_time <= current_time):
            bullet = Bullet(self)
            bulletManager.add_bullet(bullet)
            self.shooting_time += random.randint(self.INITIAL_SHOOTING_TIME, self. FINAL_SHOOTING_TIME)
