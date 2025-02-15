import pygame

pygame.init()

screen = pygame.display.set_mode((720, 360))
pygame.display.set_caption("PLAY OR DIE")


WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)
BLUE = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_w:
                print("W key pressed")
            elif event.key == pygame.K_s:
                print("S key pressed")
            elif event.key == pygame.K_a:
                print("A key pressed")
            elif event.key == pygame.K_d:
                print("D key pressed")
                
    screen.fill(RED)
    pygame.draw.circle(screen, GREEN, (120, 90), 30)
    pygame.draw.rect(screen, LIGHT_GREEN, (150, 150, 50, 50))

    point_1 = (300, 100)
    point_2 = (250, 200)  
    point_3 = (350, 200)  
    pygame.draw.polygon(screen, BLUE, [point_1, point_2, point_3])

    pygame.display.update()

pygame.quit()