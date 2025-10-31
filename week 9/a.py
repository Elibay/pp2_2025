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
    if moves == 0:
        return x, y, moves
    if moves > total_moves / 2:
        x -= speed
    else:
        x += speed
    moves -= 1
    return x, y, moves

pygame.init()

avatar, screen, background, island = init()

bullets = []

direction = "left"

x = 620
y = 40

island_x = 550
island_y = 350

speed = 5
total_moves = 50
moves = 0

cnt = 0
while True:
    if cnt % 100 == 0:
        print(cnt)
    if cnt % 5 == 0:
        x, y, moves = move_avatar(speed, x, y, moves, total_moves)
    show_avatar(background, avatar, screen, y, x)
    show_island(island, screen, island_y, island_x)
    pygame.display.update()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                moves = total_moves
                x, y, moves = move_avatar(speed, x, y, moves, total_moves)
    #         if event.key == pygame.K_RIGHT:
    #             direction = "right"
    #             x, y, direction = move_rocket(x, y, direction, rocket_speed)
    #         if event.key == pygame.K_UP:
    #             direction = "up"
    #             x, y, direction = move_rocket(x, y, direction, rocket_speed)
    #         if event.key == pygame.K_DOWN:
    #             direction = "down"
    #             x, y, direction = move_rocket(x, y, direction, rocket_speed)
    #         if event.key == pygame.K_SPACE:
    #             bullets.append((y, x + 20))
    #         if event.key == pygame.K_ESCAPE:
    #             exit(0)

    cnt += 1