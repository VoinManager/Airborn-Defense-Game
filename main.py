from Landing import *
from Background_mountains import *
from Mountains import *
from Functions import *
pygame.quit()


def start_screen():
    screen = pygame.display.set_mode((300, 300))

    screen.fill('white')
    pygame.font.init()
    font = pygame.font.Font(None, 50)

    string_rendered = font.render('Play', 1, pygame.Color('black'))
    font_rect = string_rendered.get_rect()
    font_rect.left = 115
    font_rect.top = 115
    screen.blit(string_rendered, font_rect)

    # string_rendered = font.render('Settings', 1, pygame.Color('black'))
    # font_rect = string_rendered.get_rect()
    # font_rect.top = 260
    # screen.blit(string_rendered, font_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect((115, 115, 75, 35)).collidepoint(event.pos):
                    pygame.quit()
                    return
        pygame.display.flip()


def end_screen(score: int, win=False):
    screen = pygame.display.set_mode((300, 300))

    screen.fill('white')
    pygame.font.init()
    font = pygame.font.Font(None, 50)

    text = 'You win' if win else 'You lose'
    string_rendered = font.render(text, 1, pygame.Color('black'))
    font_rect = string_rendered.get_rect()
    font_rect.left = 80
    font_rect.top = 50
    screen.blit(string_rendered, font_rect)

    string_rendered = font.render(f'Your score: {score}', 1, pygame.Color('black'))
    font_rect = string_rendered.get_rect()
    font_rect.left = 45 - (7.5 * len(str(score)))
    font_rect.top = 150
    screen.blit(string_rendered, font_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                return
        pygame.display.flip()


def main():
    start_screen()

    size = width, height = 800, 500
    speed_of_landing = 2  # pixels per frames
    FPS = 60  # frames per second
    UPS = 15  # updates (animations) per second
    clock = pygame.time.Clock()
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
