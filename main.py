from Landing import *
from BackgroundMountains import *
from Mountains import *
from Functions import *
from Gun import *
import scheckik

import time



with open('config.txt', mode='rt', encoding='UTF-8') as config:
    for line in config.readlines():
        name, value = line.split('=')[0].split()[0].strip(), int(line.split('=')[1].split()[0].strip())
        if name == 'FPS':
            FPS = value
        elif name == 'UPS':
            UPS = value


class StartScreenSprite(pygame.sprite.Sprite):
    image = load_image('background picture.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(StartScreenSprite.image, (533, 300))
        self.rect = self.image.get_rect()


pygame.quit()


def random_pos(w):
    x = random.randint(10, w - 20)
    return (x, 10)


def start_screen():
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    StartScreenSprite(sprites)
    sprites.draw(screen)

    pygame.font.init()
    font = pygame.font.Font(None, 50)

    string_rendered = font.render('Play', 1, pygame.Color('black'))
    font_rect = string_rendered.get_rect()
    font_rect.left = 115
    font_rect.top = 35
    screen.blit(string_rendered, font_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect((115, 35, 75, 35)).collidepoint(event.pos):
                    pygame.quit()
                    return
                
        sprites.draw(screen)
        screen.blit(string_rendered, font_rect)
        pygame.display.flip()
        clock.tick(FPS)


def end_screen_win(score: int, win=False):
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    StartScreenSprite(sprites)
    sprites.draw(screen)

    pygame.font.init()
    font = pygame.font.Font(None, 50)

    text = 'You win' if win else 'You lose'
    first_string_rendered = font.render(text, 1, pygame.Color('red'))
    first_font_rect = first_string_rendered.get_rect()
    first_font_rect.left = 80
    first_font_rect.top = 50

    second_string_rendered = font.render(f'Your score: {score}', 1, pygame.Color('red'))
    second_font_rect = second_string_rendered.get_rect()
    second_font_rect.left = 45 - (7.5 * len(str(score)))
    second_font_rect.top = 150

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                return
            
        sprites.draw(screen)
        screen.blit(first_string_rendered, first_font_rect)
        screen.blit(second_string_rendered, second_font_rect)
        pygame.display.flip()
        clock.tick(FPS)

def end_screen_Lose(score: int, win=False):
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    StartScreenSprite(sprites)
    sprites.draw(screen)

    pygame.font.init()
    font = pygame.font.Font(None, 50)

    text = 'You win' if win else 'You lose'
    first_string_rendered = font.render(text, 1, pygame.Color('red'))
    first_font_rect = first_string_rendered.get_rect()
    first_font_rect.left = 80
    first_font_rect.top = 50

    second_string_rendered = font.render(f'Your score: {score}', 1, pygame.Color('red'))
    second_font_rect = second_string_rendered.get_rect()
    second_font_rect.left = 45 - (7.5 * len(str(score)))
    second_font_rect.top = 150

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                return
            
        sprites.draw(screen)
        screen.blit(first_string_rendered, first_font_rect)
        screen.blit(second_string_rendered, second_font_rect)
        pygame.display.flip()
        clock.tick(FPS)


def main():
    pygame.font.init() 

    start_screen()

    speed_of_landing = 2  # pixels per frames

    size = width, height = 800, 500
    pygame.init()
    screen = pygame.display.set_mode(size)
    UPDATE_MOVEMENTS = pygame.USEREVENT + 1
    UPDATE_ANIMATIONS = pygame.USEREVENT + 2
    pygame.time.set_timer(UPDATE_MOVEMENTS, 1000//FPS)
    pygame.time.set_timer(UPDATE_ANIMATIONS, 1000//UPS)

    all_sprites = pygame.sprite.Group()
    landings = pygame.sprite.Group()
    background_mountain = BackgroundMountains(height, all_sprites)
    mountain = Mountain(height, all_sprites)

    gun1 = Gun(145-64, 394-64, all_sprites)
    gun2 = ""


    wait_sapwn = [0.8, 0.9, 1, 1.2, 1.3, 1.5, 1.7, 2.5, 0.7,]

    perezarydka = 5
    patron = 5
    heart = 10
    kills = 0
    kills_d = 0
    level = 1
    is_pushka2 = False
    
    pygame.font.init()
    font = pygame.font.Font(None, 50)


    timing = time.time(); 

    perez1 = time.time(); 
    perez2 = time.time(); 

    first_press = True
    secend_press = False

    first_perez = False
    secend_perez = False
    sche = scheckik.down

    poyav = False

    while True:  # whole cycle is temporary
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:  # сюда музло
                    if (first_press == True and first_perez == False) or (secend_press == True and secend_perez == False):
                        for landing in landings:
                            if landing.up_strike(event.pos) == True:
                                kills_d += 1
                                kills += 1
                        patron -= 1
            elif event.type == pygame.KEYDOWN:  #сюда музло
                if event.key == pygame.K_1:
                    if secend_press == True:
                        if first_perez == False:
                            first_press = True
                            secend_press = False
                elif event.key == pygame.K_2:
                    if first_press == True and poyav:
                        if secend_perez == False:
                            secend_press = True
                            first_press = False
            elif time.time() - timing > random.choice(wait_sapwn):
                timing = time.time()
                Landing(random_pos(width), speed_of_landing, all_sprites, landings)
            elif event.type == UPDATE_MOVEMENTS:
                landings.update(mountain, width)
            elif event.type == UPDATE_ANIMATIONS:
                for landing in landings:
                    landing.update_animation()

        if patron <= 0:
            if first_press == True:
                first_perez = True
            else:
                secend_perez = True

        if first_perez == True:
            if time.time() - perez1 > perezarydka:
                perez1 = time.time()
                first_perez = False
                patron = 10

        if secend_perez == True:
            if time.time() - perez2 > perezarydka:
                perez2 = time.time()
                secend_perez = False
                patron = 10
        

        if sche < scheckik.down:
            heart -= abs(scheckik.down - sche)
            sche = scheckik.down

        if kills == 7:
            level += 1
            patron = 10
            kills = 0
            if level == 3 and not is_pushka2:
                perezarydka = 5
                gun2 = Gun(364-64, 371-64, all_sprites)
                poyav = True
            elif level == 4:
                perezarydka = 18
            
        
        if level == 6:
            end_screen_win(kills_d, True)

        if heart <= 0:
            end_screen_Lose(kills_d, False)

                    
        screen.fill((60, 100, 150))

        string_rendered = font.render(f'level: {level}', 1, pygame.Color('black'))
        font_rect = string_rendered.get_rect()
        font_rect.left = 0
        font_rect.top = 0
        screen.blit(string_rendered, font_rect)

        string_rendered = font.render(f'kill: {kills_d}', 1, pygame.Color('black'))
        font_rect = string_rendered.get_rect()
        font_rect.left = 140
        font_rect.top = 0
        screen.blit(string_rendered, font_rect)

        string_rendered = font.render(f'patron: {patron}', 1, pygame.Color('black'))
        font_rect = string_rendered.get_rect()
        font_rect.left = 140 * 2
        font_rect.top = 0
        screen.blit(string_rendered, font_rect)

        string_rendered = font.render(f'heart: {heart}', 1, pygame.Color('black'))
        font_rect = string_rendered.get_rect()
        font_rect.left = 140 * 4
        font_rect.top = 0
        screen.blit(string_rendered, font_rect)

        if first_press == True:
            string_rendered = font.render(f'taken: first weapon', 1, pygame.Color('black'))
            font_rect = string_rendered.get_rect()
            font_rect.left = 0
            font_rect.top = 55
        else:
            string_rendered = font.render(f'taken: second weapon', 1, pygame.Color('black'))
            font_rect = string_rendered.get_rect()
            font_rect.left = 0
            font_rect.top = 55
        screen.blit(string_rendered, font_rect)

        if first_perez == False and secend_perez == False:
            string_rendered = font.render(f'recharging: ---', 1, pygame.Color('black'))
            font_rect = string_rendered.get_rect()
            font_rect.left = 450
            font_rect.top = 55

        if first_perez == True and secend_perez == True:
            string_rendered = font.render(f'recharging: all', 1, pygame.Color('black'))
            font_rect = string_rendered.get_rect()
            font_rect.left = 450
            font_rect.top = 55

        if first_perez == True and secend_perez == False:
            string_rendered = font.render(f'recharging: firts', 1, pygame.Color('black'))
            font_rect = string_rendered.get_rect()
            font_rect.left = 450
            font_rect.top = 55

        if first_perez == False and secend_perez == True:
            string_rendered = font.render(f'recharging: second', 1, pygame.Color('black'))
            font_rect = string_rendered.get_rect()
            font_rect.left = 450
            font_rect.top = 55
        screen.blit(string_rendered, font_rect)

        all_sprites.draw(screen)
        pygame.display.update()


while True:
    main()
