import pygame
from Functions import load_image


class Mountain(pygame.sprite.Sprite):
    image = load_image('mountains.png', colorkey=-1)

    def __init__(self, window_height, *groups):
        super().__init__(*groups)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = window_height
