import pygame
import sys
from collections import deque

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
NODE_RADIUS = 20
EDGE_WIDTH = 2

# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breadth-First Traversal Visualization")

# Define the graph structure (nodes and edges)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# Breadth-First Traversal
def breadth_first_traversal(start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)

            # Draw the visited node (in RED)
            x, y = node_positions[current_node]
            pygame.draw.circle(screen, RED, (x, y), NODE_RADIUS)

            for neighbor in graph[current_node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

# Position nodes in a circular layout
num_nodes = len(graph)
node_positions = {
    'A': (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)),
    'B': (int(SCREEN_WIDTH / 2 - 100), int(SCREEN_HEIGHT / 2 - 100)),
    'C': (int(SCREEN_WIDTH / 2 + 100), int(SCREEN_HEIGHT / 2 - 100)),
    'D': (int(SCREEN_WIDTH / 2 - 150), int(SCREEN_HEIGHT / 2 - 200)),
    'E': (int(SCREEN_WIDTH / 2 - 50), int(SCREEN_HEIGHT / 2 - 200)),
    'F': (int(SCREEN_WIDTH / 2 + 50), int(SCREEN_HEIGHT / 2 - 200)),
    'G': (int(SCREEN_WIDTH / 2 + 150), int(SCREEN_HEIGHT / 2 - 200))
}

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Perform breadth-first traversal from node 'A'
    breadth_first_traversal('A')

    # Draw edges
    for node, neighbors in graph.items():
        node_x, node_y = node_positions[node]
        for neighbor in neighbors:
            neighbor_x, neighbor_y = node_positions[neighbor]
            pygame.draw.line(screen, RED, (node_x, node_y), (neighbor_x, neighbor_y), EDGE_WIDTH)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
