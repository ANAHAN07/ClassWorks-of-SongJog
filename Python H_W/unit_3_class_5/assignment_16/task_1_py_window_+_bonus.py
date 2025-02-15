import pygame
import random   # For bonus task


pygame.init()

WIDTH, HEIGHT = 500, 400    # Screen setting
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MY First PY Project")   # Title

bg_color = (0, 128, 255)  # Blue

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                
                # Bonus --
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))     # random colors will apper after pressing space bar.
    
    screen.fill(bg_color)
    pygame.display.flip()

pygame.quit()