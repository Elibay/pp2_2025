import pygame

def init():
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

pygame.init()
init()

screen = pygame.display.set_mode((1000, 500))
background = pygame.image.load("images/background.png")
rocket = pygame.image.load("images/rocket.png")
rocket = pygame.transform.scale(rocket, (50, 50))
background = pygame.transform.scale(background, (1000, 500))

screen.blit(background, (0, 0))

x = 475
y = 450


cnt = 0
while True:
    if cnt % 100 == 0:
        print(cnt)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(rocket, (y, x))
    pygame.display.update()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                y -= 10
            if event.key == pygame.K_RIGHT:
                y += 10
            if event.key == pygame.K_UP:
                x -= 10
                x = max(0, x)
            if event.key == pygame.K_DOWN:
                x += 10
                x = min(500, x)
            if event.key == pygame.K_ESCAPE:
                exit(0)
            

    cnt += 1