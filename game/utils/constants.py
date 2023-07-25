import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Icon/icon.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Tack_3.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
STAR_TYPE = 'star'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_2.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))

NAVE_STAR  = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_star.png")) 

BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))

ENEMY_LIST = [pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png")),
           pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png")),
           pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png")),
           pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png")),
           pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_5.png"))
           ]
EXPLOSION_LIST= [pygame.image.load(os.path.join(IMG_DIR, "Bullet/ex1.png")),
             pygame.image.load(os.path.join(IMG_DIR, "Bullet/ex2.png")),
             pygame.image.load(os.path.join(IMG_DIR, "Bullet/ex3.png")),
             pygame.image.load(os.path.join(IMG_DIR, "Bullet/ex4.png")),
             pygame.image.load(os.path.join(IMG_DIR, "Bullet/ex5.png")),
             pygame.image.load(os.path.join(IMG_DIR, "Bullet/ex6.png")),
             pygame.image.load(os.path.join(IMG_DIR, "Bullet/ex7.png"))
             ]


BUTTON_PLAY = pygame.image.load(os.path.join(IMG_DIR, 'Icon/Play.png'))
BUTTON_RESTART = pygame.image.load(os.path.join(IMG_DIR, 'Icon/Restar.png'))

HEART  = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart_2.png'))
STAR  = pygame.image.load(os.path.join(IMG_DIR, 'Other/Estrella.png'))

FONDO_INICIO = pygame.image.load(os.path.join(IMG_DIR, 'Other/Tack_4.png'))


ALIEN = pygame.image.load(os.path.join(IMG_DIR, "Enemy/alien.png"))

FONT_STYLE = 'freesansbold.ttf'
