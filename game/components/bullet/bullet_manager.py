import pygame
from game.components.bullet.explosion import Explosion

from game.components.power_up.heart import Heart

from game.utils.constants import ENEMY_LIST, SHIELD_TYPE, STAR_TYPE

class BulletManager:
    CANT = len(ENEMY_LIST)

    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
        self.explo_list = []
        self.heart = Heart()
        #self.explosion = Explosion()

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player) and bullet.owner =='enemy':
                self.enemy_bullets.remove(bullet)
                if  game.player.power_up_type != SHIELD_TYPE:#game.player.power_up_type != SHIELD_TYPE:
                    game.heart.cant -=1
                    if game.heart.cant ==0:
                        game.death_counter +=1
                        game.playing = False
                        pygame.time.delay(500)
                break
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            
            for enemy in game.enemyManager.enemies:
                if bullet.owner =='player' and bullet.rect.colliderect(enemy):
                    
                    if game.player.power_up_type == STAR_TYPE:
                       game.player.points_extra += 5


                    self.add_explo(enemy)
                    for inma in self.explo_list:
                        inma.update()
                    game.enemyManager.enemies.remove(enemy)
                    game.score +=1
            


    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.player_bullets:
            bullet.draw(screen)
        #if len(self.explo_list)<:
        for inma in self.explo_list:
            inma.draw(screen)

    def add_bullet(self, bullet):
        if(bullet.owner == 'enemy' and len(self.enemy_bullets) < self.CANT):
            self.enemy_bullets.append(bullet)
        elif(bullet.owner == 'player' and len(self.player_bullets) < 20):
            self.player_bullets.append(bullet)
    
    def add_explo(self, enemy):
        explo = Explosion(enemy)
        self.explo_list.append(explo)
    
    def reset(self):
        self.player_bullets = []
        self.enemy_bullets = []
        self.explo_list = []
    