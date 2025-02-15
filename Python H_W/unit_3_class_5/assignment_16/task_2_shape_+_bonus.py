import pygame


pygame.init()

WIDTH, HEIGHT = 500, 400    # Screen Setting
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shapes")        # Title


WHITE = (255, 255, 255)     # White color
RED = (255, 0, 0)           # Red color
BLUE = (0, 0, 255)          # Blue color
GREEN = (0, 255, 0)         # Green color
BROWN = (139, 69, 19)       # Brown color
YELLOW = (255, 255, 0)      # Yellow color


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill(WHITE)  # BG Color
    
    
    pygame.draw.rect(screen, RED, (10, 10, 100, 60))  # Red Rectangle (On top-left corner)
    pygame.draw.circle(screen, BLUE, (WIDTH - 50, 50), 40)  # Blue Circle (On top-right corner)
    pygame.draw.line(screen, GREEN, (WIDTH // 4, HEIGHT - 50), (3 * WIDTH // 4, HEIGHT - 50), 5)  # Green line (On Middle-bottom)
    
    # Bonus
    pygame.draw.rect(screen, BROWN, (200, 220, 100, 100))  # House base
    pygame.draw.polygon(screen, YELLOW, [(200, 220), (250, 170), (300, 220)])  # Roof
    pygame.draw.rect(screen, BLUE, (230, 270, 30, 50))  # Door
    
    pygame.display.flip()

pygame.quit()
