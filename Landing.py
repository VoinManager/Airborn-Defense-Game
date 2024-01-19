import pygame
import random
from Functions import load_image


class Landing(pygame.sprite.Sprite):
    image = load_image('landing.png', colorkey=-1)

    def __init__(self, pos, speed_of_landing, *groups):
        super().__init__(*groups)

        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.rect.x = self.x = pos[0]
        self.rect.y = self.y = pos[1]

        self.x_velocity = (random.random() - 0.5) * 2
        self.y_velocity = speed_of_landing

    def update(self, mountain_group, window_width):
        if pygame.sprite.collide_mask(self, mountain_group):
            self.dead()
        else:
            if self.rect.x <= 0 or self.rect.x + self.rect.w >= window_width:
                self.x_velocity = -self.x_velocity
            self.x += self.x_velocity
            self.rect.x = self.x
            self.y += self.y_velocity
            self.rect.y = self.y

    def dead(self):
        self.kill()
