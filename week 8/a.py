import pygame

def init():
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((1000, 500))
    background = pygame.image.load("images/background.png")
    bullet_image = pygame.image.load("images/bullet.png")
    bullet_image = pygame.transform.scale(bullet_image, (10, 10))
    bullet_image = pygame.transform.rotate(bullet_image, 45)
    rocket = pygame.image.load("images/rocket.png")
    rocket = pygame.transform.scale(rocket, (50, 50))
    background = pygame.transform.scale(background, (1000, 500))

    screen.blit(background, (0, 0))
    return bullet_image, rocket, screen, background

def show_rocket(background, rocket, screen):
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(rocket, (x, y))

def show_bullets(bullets, bullet_image, screen, speed):
    new_arr = []
    # print(bullets)
    for bullet in bullets:
        x, y = bullet
        x -= speed
        screen.blit(bullet_image, (y, x))
        new_arr.append((x, y))

    return new_arr

def move_rocket(x, y, direction, speed):
    if direction == "left":
        x = x - speed
        x = max(0, x)
        if x == 0:
            direction = "right"
    if direction == "right":
        x = x + speed
        x = min(950, x)
        if x == 950:
            direction = "left"
    if direction == "up":
        y = y - speed
        y = max(0, y)
        if y == 0:
            direction = "down"
    if direction == "down":
        y = y + speed
        y = min(450, y)
        if y == 450:
            direction = "up"

    return x, y, direction

pygame.init()

bullet_image, rocket, screen, background = init()

bullets = []

direction = "left"

x = 475
y = 450
speed = 3
rocket_speed = 2

cnt = 0
while True:
    if cnt % 100 == 0:
        print(cnt)
    pygame.display.update()
    show_rocket(background, rocket, screen)
    bullets = show_bullets(bullets, bullet_image, screen, speed)
    events = pygame.event.get()
    x, y, direction = move_rocket(x, y, direction, rocket_speed)

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
                x, y, direction = move_rocket(x, y, direction, rocket_speed)
            if event.key == pygame.K_RIGHT:
                direction = "right"
                x, y, direction = move_rocket(x, y, direction, rocket_speed)
            if event.key == pygame.K_UP:
                direction = "up"
                x, y, direction = move_rocket(x, y, direction, rocket_speed)
            if event.key == pygame.K_DOWN:
                direction = "down"
                x, y, direction = move_rocket(x, y, direction, rocket_speed)
            if event.key == pygame.K_SPACE:
                bullets.append((y, x + 20))
            if event.key == pygame.K_ESCAPE:
                exit(0)
            

    cnt += 1