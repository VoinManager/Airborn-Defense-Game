from Landing import *
from BackgroundMountains import *
from Mountains import *
from Functions import *


speed_of_landing = 2  # pixels per frames
FPS = 60  # frames per second
UPS = 15  # updates (animations) per second


class StartScreenSprite(pygame.sprite.Sprite):
    image = load_image('start screen.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(StartScreenSprite.image, (533, 300))
        self.rect = self.image.get_rect()


pygame.quit()


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


def end_screen(score: int, win=False):
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()

    sprites = pygame.sprite.Group()
    StartScreenSprite(sprites)
    sprites.draw(screen)

    pygame.font.init()
    font = pygame.font.Font(None, 50)

    text = 'You win' if win else 'You lose'
    first_string_rendered = font.render(text, 1, pygame.Color('black'))
    first_font_rect = first_string_rendered.get_rect()
    first_font_rect.left = 80
    first_font_rect.top = 50

    second_string_rendered = font.render(f'Your score: {score}', 1, pygame.Color('black'))
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
    start_screen()

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

    while True:  # whole cycle is temporary
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:  # Right click
                    Landing(event.pos, speed_of_landing, all_sprites, landings)
                elif pygame.mouse.get_pressed()[2]:  # Left click
                    for landing in landings:
                        landing.dead()
            elif event.type == UPDATE_MOVEMENTS:
                landings.update(mountain, width)
            elif event.type == UPDATE_ANIMATIONS:
                for landing in landings:
                    landing.update_animation()
        screen.fill((60, 100, 150))
        all_sprites.draw(screen)
        pygame.display.flip()


while True:
    main()
