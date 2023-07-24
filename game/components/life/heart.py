from game.utils.constants import HEART


class Heart:
    def __init__(self):
        self.image = HEART
        self.cant = 3
    
    def decrementar_heart(self):
        self.cant -= 1

    def draw(self, screen):
        heart_x = 20
        heart_y = 20
        for index in range(self.cant):
            screen.blit(self.image, (heart_x,heart_y))
            heart_x += 50