import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Catch the Ball or DIE")

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)
BLUE = (0, 0, 255)

player_x, player_y = 200, 450
ball_x, ball_y = random.randint(50, 450), 0
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x>0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_y>450:
        player_y += 5


    ball_y += speed
    if ball_y > 500:
        ball_x, ball_y = random.randint(50, 450), 0


    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (player_x, player_y, 150, 10))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), 10)

    pygame.display.update()

pygame.quit()