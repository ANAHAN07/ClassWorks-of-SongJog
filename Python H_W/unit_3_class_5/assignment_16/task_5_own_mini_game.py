import pygame

pygame.init()


WIDTH, HEIGHT = 600, 600    # Screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Maze")     # Title


WHITE = (255, 255, 255)     # White color
BLACK = (0, 0, 0)           # Black color
BLUE = (0, 0, 255)          # Blue color
GREEN = (0, 255, 0)         # Green color

# Player settings
player_size = 20
player_x, player_y = 50, 50
player_speed = 5

# Maze walls 
walls = [
    pygame.Rect(100, 0, 20, 500),
    pygame.Rect(200, 100, 20, 500),
    pygame.Rect(300, 0, 20, 400),
    pygame.Rect(400, 200, 20, 400),
    pygame.Rect(500, 0, 20, 500)
]


goal = pygame.Rect(550, 550, 30, 30)    # End point


running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement by key arrows 
    keys = pygame.key.get_pressed()
    new_x, new_y = player_x, player_y
    if keys[pygame.K_UP]:
        new_y -= player_speed
    if keys[pygame.K_DOWN]:
        new_y += player_speed
    if keys[pygame.K_LEFT]:
        new_x -= player_speed
    if keys[pygame.K_RIGHT]:
        new_x += player_speed
    
    # Movements
    player_rect = pygame.Rect(new_x, new_y, player_size, player_size)
    if not any(player_rect.colliderect(wall) for wall in walls):
        player_x, player_y = new_x, new_y
    
    
    if player_rect.colliderect(goal):       # Win msg will be shown in terminal
        print("You Win!")
        running = False
    
    
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)       # WALLS
    
    
    pygame.draw.rect(screen, GREEN, goal)       # GOAL POST
    

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))      # Player
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()