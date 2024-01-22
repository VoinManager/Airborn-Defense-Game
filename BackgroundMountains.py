import pygame
from Functions import load_image


class BackgroundMountains(pygame.sprite.Sprite):
    image = load_image('background mountains.png', colorkey=-1)

    def __init__(self, window_height, *groups):
        super().__init__(*groups)
        self.image = BackgroundMountains.image
        self.rect = self.image.get_rect()
        self.rect.bottom = window_height
