import pygame
import random
from Functions import load_image


class Landing(pygame.sprite.Sprite):
    image = load_image('landing.png', colorkey=-1)
    death_image = load_image('dead landing.png', colorkey=-1)

    def __init__(self, pos, speed_of_landing, *groups):
        super().__init__(*groups)

        self.is_dead = False
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.rect.x = self.x = pos[0]  # self.x can be a float, but self.rect.x is not
        self.rect.y = self.y = pos[1]  # self.y can be a float, but self.rect.y is not

        self.x_velocity = (random.random() - 0.5) * 2  # random float number in the interval [-1, 1)
        self.y_velocity = speed_of_landing
        self.y_acceleration = 0
        self.x_acceleration = 0

    def update(self, mountain_group, window_width):
        if pygame.sprite.collide_mask(self, mountain_group):
            if self.is_dead:
                self.kill()
            else:
                self.landing()

        elif self.is_dead:
            self.x += self.x_velocity
            self.rect.x = self.x
            self.y += self.y_velocity
            self.rect.y = self.y

            if self.x_velocity + self.x_acceleration <= 0:
                self.x_velocity = 0
            else:
                self.x_velocity += self.x_acceleration

            if self.y_velocity + self.y_acceleration >= 5:
                self.y_velocity = 5
            else:
                self.y_velocity += self.y_acceleration

        else:
            if self.rect.x <= 0 or self.rect.x + self.rect.w >= window_width:
                self.x_velocity = -self.x_velocity
            self.x += self.x_velocity
            self.rect.x = self.x
            self.y += self.y_velocity
            self.rect.y = self.y

    def dead(self):
        if self.is_dead:
            return
        self.image = Landing.death_image
        self.rect = self.image.get_rect()
        self.x += 19  # depends on sprites
        self.rect.x = self.x
        self.y += 32  # depends on sprites
        self.rect.y = self.y
        self.x_acceleration = -0.01
        self.y_acceleration = 0.1
        self.is_dead = True

    def landing(self):
        self.kill()  # temporary
