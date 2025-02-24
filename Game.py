import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")

# Set up game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the player's properties
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height // 2 - player_height // 2
player_speed = 5

# Set up obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 3
obstacles = []

# Game clock
clock = pygame.time.Clock()

# Set up the score
score = 0
font = pygame.font.SysFont(None, 36)

# Function to display score
def display_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling (player movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Create new obstacles
    if random.randint(1, 100) <= 2:
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacles.append(pygame.Rect(obstacle_x, 0, obstacle_width, obstacle_height))

    # Move obstacles
    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.y > screen_height:
            obstacles.remove(obstacle)
            score += 1  # Player scores when an obstacle goes off-screen

        # Check for collision
        if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(obstacle):
            running = False  # End the game if there's a collision

        # Draw obstacle
        pygame.draw.rect(screen, GREEN, obstacle)

    # Draw the player (red rectangle)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Display the score
    display_score(score)

    # Update the game display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)

# Game Over Screen
game_over_font = pygame.font.SysFont(None, 72)
game_over_text = game_over_font.render("GAME OVER", True, BLACK)
screen.fill(WHITE)
screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
pygame.display.update()
pygame.time.delay(2000)  # Show "Game Over" for 2 seconds

# Quit Pygame
pygame.quit()
sys.exit()
