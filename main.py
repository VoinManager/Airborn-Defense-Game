import os
import sys
import random

import pygame
from Landing import *
from Background_mountains import *
from Mountains import *
from Functions import *
pygame.quit()


size = width, height = 800, 500
SPEED_OF_LANDING = 2  # pixels per frames
FPS = 60  # frames per second
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(size)
UPDATE_MOVEMENTS = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE_MOVEMENTS, 1000//FPS)


all_sprites = pygame.sprite.Group()
landings = pygame.sprite.Group()
background_mountain = BackgroundMountains(height, all_sprites)
mountain = Mountain(height, all_sprites)

while True:  # whole cycle is temporary
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:  # Right click
                Landing(event.pos, SPEED_OF_LANDING, all_sprites, landings)
            elif pygame.mouse.get_pressed()[2]:  # Left click
                for landing in landings:
                    landing.dead()
        elif event.type == UPDATE_MOVEMENTS:
            landings.update(mountain, width)
    screen.fill((60, 100, 150))
    all_sprites.draw(screen)
    pygame.display.flip()
