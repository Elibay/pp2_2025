import pygame


def init():
    screen = pygame.display.set_mode((500, 800))
    background = pygame.image.load("images/background.png")
    avatar = pygame.image.load("images/avatar.png")
    avatar = pygame.transform.scale(avatar, (80, 80))
    background = pygame.transform.scale(background, (500, 800))
    island = pygame.image.load("images/island.png")
    island = pygame.transform.scale(island, (150, 100))

    screen.blit(background, (0, 0))
    return avatar, screen, background, island


def show_avatar(background, avatar, screen, x, y):
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(avatar, (x, y))

def show_island(island, screen, x, y):
    screen.blit(island, (x, y))


def move_avatar(speed, x, y, moves, total_moves):
    print(x, y)
    if moves < 0:
        return x, y, moves
    if moves == 0:
        x += speed
        return x, y, moves
    if moves > total_moves / 2:
        x -= speed
    else:
        x += speed
    moves -= 1
    return x, y, moves

def move_direction(direction, x, y, speed):
    if direction == "left":
        y -= 1
    if direction == "right":
        y += 1
    return x, y


def interception(x, y, moves, islands):
    for i_x, i_y in islands:
        if i_x - 20 <= x <= i_x and i_y <= y + 40 and y <= i_y + 120:
            return True
    return False

pygame.init()

avatar, screen, background, island = init()

bullets = []

direction = ""

islands = [(550, 350), (400, 30), (200, 120)]

x = 620
y = 40

speed = 8
total_moves = 30
moves = 0

cnt = 0
while True:
    if cnt % 100 == 0:
        print(cnt)
    if cnt % 5 == 0:
        x, y, moves = move_avatar(speed, x, y, moves, total_moves)
    show_avatar(background, avatar, screen, y, x)
    for i_x, i_y in islands:
        show_island(island, screen, i_y, i_x)
    pygame.display.update()
    events = pygame.event.get()
    if not interception(x, y, moves, islands):
        x, y = move_direction(direction, x, y, speed)
    else:
        moves = -1
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                moves = total_moves
                x, y, moves = move_avatar(speed, x, y, moves, total_moves)
            if event.key == pygame.K_LEFT:
                direction = "left"
            if event.key == pygame.K_RIGHT:
                direction = "right"
            if event.key == pygame.K_ESCAPE:
                exit(0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                direction = ""
    cnt += 1