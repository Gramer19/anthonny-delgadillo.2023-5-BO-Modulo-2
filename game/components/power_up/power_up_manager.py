import random
import pygame
from game.components.power_up.shield import Shield
from game.components.power_up.super_start import SuperStar


class PowerUpManager:

    def __init__(self):
        print("entrreeeeeee")
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3000, 5000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()# hora de inicio
                game.player.has_power_up = True
                game.player.power_up_time_up = power_up.start_time + self.duration #si llega a este tiempo obtenido se acaba el power up
                game.player.set_image(power_up.type)
            self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def generate_power_up(self):
        rand = random.randint(0,1)
        """if rand ==0:
            power_up = Shield()
            self.power_ups.append(power_up)
        else:"""
        power_up = SuperStar()
        self.power_ups.append(power_up)
            
        self.when_appears += random.randint(5000, 10000)
        #self.power_ups.append(power_up)

    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now +5000, now + 10000)
