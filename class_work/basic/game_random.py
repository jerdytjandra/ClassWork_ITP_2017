import pygame
def subok():
    a = 500
    b = 400
    pygame.init()
    screen = pygame.display.set_mode((a, b))
    done = False
    is_blue = True
    x = 30
    y = 30

    clock = pygame.time.Clock()

    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         done = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                         is_blue = not is_blue

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]    and y>0  : y -= 15
            if pressed[pygame.K_DOWN]  and y<320 : y += 15
            if pressed[pygame.K_LEFT]  and x>0  : x -= 15
            if pressed[pygame.K_RIGHT] and x<410 : x += 15

            screen.fill((0, 0, 0))
            if is_blue: color = (0, 128, 255)
            else: color = (255, 0, 0)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 80, 80))

            pygame.display.flip()
            clock.tick(60)
subok()
