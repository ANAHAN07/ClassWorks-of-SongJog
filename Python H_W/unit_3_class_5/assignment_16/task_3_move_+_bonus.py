import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600  # Display Size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move Object")   # Title


WHITE = (255, 255, 255)     # White color

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))         # Randomizing color


rect_x, rect_y = WIDTH // 4, HEIGHT // 2    # rectangle size
circle_x, circle_y = 3 * WIDTH // 4, HEIGHT // 2        # circle size
shape_size = 40
move_speed = 1  # Object Moving speed
rect_color = random_color()
circle_color = random_color()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    keys = pygame.key.get_pressed() # Get pressed keys
    
    # setting for rectangle by W,A,S,D
    if keys[pygame.K_a]:
        rect_x -= move_speed
        rect_color = random_color()  # Random color when moving left
    if keys[pygame.K_d]:
        rect_x += move_speed
        rect_color = random_color()  # Random color when moving right
    if keys[pygame.K_w]:
        rect_y -= move_speed
        rect_color = random_color()  # Random color when moving up
    if keys[pygame.K_s]:
        rect_y += move_speed
        rect_color = random_color()  # Random color when moving down
    
    # setting for circle by arrow keys
    if keys[pygame.K_LEFT]:
        circle_x -= move_speed
        circle_color = random_color()  # Random color when moving left
    if keys[pygame.K_RIGHT]:
        circle_x += move_speed
        circle_color = random_color()  # Random color when moving right
    if keys[pygame.K_UP]:
        circle_y -= move_speed
        circle_color = random_color()  # Random color when moving up
    if keys[pygame.K_DOWN]:
        circle_y += move_speed
        circle_color = random_color()  # Random color when moving down
    

    screen.fill(WHITE)  # BG color
    
    # Moving objects
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, shape_size, shape_size))  # Rectangle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), shape_size // 2)  # Circle
    
    pygame.display.flip()

pygame.quit()