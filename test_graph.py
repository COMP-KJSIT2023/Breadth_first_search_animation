import pygame
import sys
import math
from collections import deque


def start_transversal(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node]) 
    Transversed = 330
    last_node = '0'

    while queue:
        
        # Draw nodes
        for n, (x, y) in node_positions.items():
            if n == node: 
                node_color = BLUE
            else: 
                node_color = RED
            pygame.draw.circle(screen, node_color, (x, y), NODE_RADIUS)
            text = font.render(n, True, WHITE)
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)
        
        if node not in visited:
            display_text3 = node
            visited.add(node)

            # Enqueue neighbors of the current node that have not been visited
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    
        # Draw the queue elements
        for i, element in enumerate(queue):
            x = 175 + i * (NODE_WIDTH + 10)
            y = 100
            pygame.draw.rect(screen, RED, (x, y, NODE_WIDTH, NODE_HEIGHT))
            text = font.render(element, True, WHITE)
            text_rect = text.get_rect(center=(x + NODE_WIDTH // 2, y + NODE_HEIGHT // 2))
            screen.blit(text, text_rect)
            
            text = font.render(display_text2, True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = (200,750)
            # Draw the text onto the screen
            screen.blit(text, text_rect)
            
            if last_node != node:
               text = font.render(display_text3, True, BLACK)
               text_rect = text.get_rect()
               text_rect.center = (Transversed,750)
               Transversed = Transversed+20
               # Draw the text onto the screen
               screen.blit(text, text_rect)
            
            last_node = node
            node = queue.popleft()  # Dequeue the front node
            pygame.display.flip()
            pygame.time.delay(500)

# Initialization
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
NODE_RADIUS = 20
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
EDGE_WIDTH = 2
NODE_WIDTH, NODE_HEIGHT = 40, 40
QUEUE_CAPACITY = 8
font = pygame.font.Font(None, 36)

graph = {
    '1': ['2', '4', '6', '7'],
    '2': ['1', '5', '8'],
    '3': ['5', '7'],
    '4': ['1', '6', '8'],
    '5': ['2', '3', '8'],
    '6': ['1', '4', '7'],
    '7': ['1', '3', '6'],
    '8': ['2', '4', '5']
    }
 
# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Graph")

display_text = "Press the key for ROOT NODE!!"
display_text2 = "Transveral order is : "

# Position nodes in a circular layout
num_nodes = len(graph)
node_positions = {
    '1': (325, 375),
    '2': (500, 450),
    '3': (600, 200),
    '4': (175, 575),
    '5': (650, 600),
    '6': (150, 200),
    '7': (450, 225),
    '8': (250, 700)
}



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:  
            display_text = "Let's Start!!"
            key_name = pygame.key.name(event.key)
            if key_name in graph:
                start_transversal(graph, key_name) 
            

    # Clear the screen
    screen.fill(WHITE)


    # Draw edges
    for node, neighbors in graph.items():
        node_x, node_y = node_positions[node]
        for neighbor in neighbors:
            neighbor_x, neighbor_y = node_positions[neighbor]
            pygame.draw.line(screen, RED, (node_x, node_y), (neighbor_x, neighbor_y), EDGE_WIDTH)

    # Draw nodes
    for node, (x, y) in node_positions.items():
        pygame.draw.circle(screen, RED, (x, y), NODE_RADIUS)
        text = font.render(node, True, WHITE)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
    
     # Render the text
    text = font.render(display_text, True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (400,50)
    # Draw the text onto the screen
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
