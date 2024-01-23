import pygame
from Functions import load_image

class Gun(pygame.sprite.Sprite):
    image = load_image('pushka.png', colorkey=-1)
    pod = load_image('podstavka.png', colorkey=-1)

    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = Gun.image
        self.rect = self.image.get_rect(center=(x,y))
        self.rect.x = x
        self.rect.y = y
    