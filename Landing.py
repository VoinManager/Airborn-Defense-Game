import pygame
import random
from Functions import load_image
import scheckik


class Landing(pygame.sprite.Sprite):
    image = load_image('landing.png', colorkey=-1)
    # death_image = load_image('dead landing.png', colorkey=-1)
    sheet = load_image('animated death landing.png', colorkey=-1)

    def __init__(self, pos, speed_of_landing, *groups):
        super().__init__(*groups)

        self.is_dead = False
        self.frames = []
        self.cut_sheet(Landing.sheet, 3, 1)
        self.current_frame = 0
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.rect.x = self.x = pos[0]  # self.x can be a float, but self.rect.x is not
        self.rect.y = self.y = pos[1]  # self.y can be a float, but self.rect.y is not

        self.x_velocity = (random.random() - 0.5) * 2  # random float number in the interval [-1, 1)
        self.y_velocity = speed_of_landing
        self.y_acceleration = 0
        self.x_acceleration = 0
        self.upale = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self, mountain_group, window_width):
        if pygame.sprite.collide_mask(self, mountain_group):
            if self.is_dead:
                self.kill()
            else:
                self.landing()
                scheckik.down += 1

        elif self.is_dead:
            self.x += self.x_velocity
            self.rect.x = self.x
            self.y += self.y_velocity
            self.rect.y = self.y

            if self.x_velocity >= 0:
                if self.x_velocity + self.x_acceleration <= 0:
                    self.x_velocity = 0
                else:
                    self.x_velocity += self.x_acceleration
            else:
                if self.x_velocity + self.x_acceleration > 0:
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

    def update_animation(self):
        if self.is_dead:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

    def dead(self):
        if self.is_dead:
            return
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.x += 19  # depends on sprites
        self.rect.x = self.x
        self.y += 32  # depends on sprites
        self.rect.y = self.y
        self.x_acceleration = -0.01 if self.x_velocity >= 0 else 0.01
        self.y_acceleration = 0.1
        self.is_dead = True

    def landing(self):
        self.kill()  # temporary



    def get_x_y(self):
        return (self.x, self.y)
    
    def up_strike(self, c_pos):
        if self.rect.collidepoint(c_pos):
            self.dead()
            return True
        return False