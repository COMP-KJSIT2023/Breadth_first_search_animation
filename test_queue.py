import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
NODE_WIDTH, NODE_HEIGHT = 40, 40
QUEUE_CAPACITY = 5

# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Queue Visualization")

# Queue data structure
queue = []

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input (enqueue and dequeue)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and len(queue) < QUEUE_CAPACITY:
        queue.append("Element")

    if keys[pygame.K_BACKSPACE] and len(queue) > 0:
        queue.pop(0)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the queue elements
    for i, element in enumerate(queue):
        x = 50 + i * (NODE_WIDTH + 10)
        y = SCREEN_HEIGHT // 2
        pygame.draw.rect(screen, RED, (x, y, NODE_WIDTH, NODE_HEIGHT))
        font = pygame.font.Font(None, 36)
        text = font.render(element, True, WHITE)
        text_rect = text.get_rect(center=(x + NODE_WIDTH // 2, y + NODE_HEIGHT // 2))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
