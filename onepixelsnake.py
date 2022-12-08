import pygame
import random
import math
import time

# Initialize the pygame
pygame.init()

# Title and Icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Snake
snakeImg = pygame.image.load("snake.png")
snakeX = 370
snakeY = 480
snakeX_change = 0
snakeY_change = 0

# Food
foodImg = pygame.image.load("food.png")
foodX = random.randint(0, 750)
foodY = random.randint(0, 550)

# Score
score = 0
font = pygame.font.Font("FreeSansBold.ttf", 32)

# Game Over
over_font = pygame.font.Font("FreeSansBold.ttf", 64)


def show_score(x, y):
    score_render = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_render, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


clock = pygame.time.Clock()
tamam = True

# Game Loop
while tamam:  # The game loop will run indefinitely
    # Initialize the game screen and state
    screen = pygame.display.set_mode((800, 600))
    snakeX = 370
    snakeY = 480
    snakeX_change = 0
    snakeY_change = 0
    foodX = random.randint(0, 750)
    foodY = random.randint(0, 550)
    score = 0
    running = True

    # Main game loop
    while running:
        clock.tick(30)
        # Screen background
        screen.fill((0, 0, 0))

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tamam = False
                running = False
            elif event.type == pygame.KEYDOWN:
                # Update the movement of the snake based on the key pressed
                if event.key == pygame.K_LEFT:
                    snakeX_change = -5
                    snakeY_change = 0
                elif event.key == pygame.K_RIGHT:
                    snakeX_change = 5
                    snakeY_change = 0
                elif event.key == pygame.K_UP:
                    snakeY_change = -5
                    snakeX_change = 0
                elif event.key == pygame.K_DOWN:
                    snakeY_change = 5
                    snakeX_change = 0
                elif event.key == pygame.K_q:
                    pygame.QUIT
                    break
                    
            elif event.type == pygame.KEYUP:
                # Stop the snake's movement when a key is released
                snakeX_change = 0
                snakeY_change = 0

        # Snake movement
        snakeX += snakeX_change
        snakeY += snakeY_change

        # Boundary conditions
        if snakeX > 720 or snakeX < -50 or snakeY > 520 or snakeY < -50:
            running = False
            

        distance = math.sqrt((snakeX - foodX) ** 2 + (snakeY - foodY) ** 2)
        if distance < 10:  # If the distance is less than 10 pixels
            score += 10
            foodX = random.randint(0, 750)
            foodY = random.randint(0, 550)

        # Drawing snake and food
        screen.blit(snakeImg, (snakeX, snakeY))
        screen.blit(foodImg, (foodX, foodY))
        show_score(10, 10)
        if not running:
            game_over_text()
        

        # Update the screen
        pygame.display.update()

    # Delay for 1 second after the game ends
    time.sleep(1)

