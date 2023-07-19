
from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_HEIGHT


class EnemyManager:
    NUMBER_OF_ENEMY = 1
    INCREASE_ENEMY = 1
    def __init__(self):
        self.enemies = []
        self.index = 0

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if enemy.rect.y >= SCREEN_HEIGHT:
                #self.enemies.remove(enemy)
                self.enemies.clear()
                self.INCREASE_ENEMY <= self.NUMBER_OF_ENEMY

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy = Enemy()
            self.enemies.append(enemy)