import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
width, height = 600, 400

# Set up display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snek Game')

# Clock object to control game speed
clock = pygame.time.Clock()

# Snake block size
snake_block = 10

# Snake speed
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Display score count
def display_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])

# Draw snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(display, green, [block[0], block[1], snake_block, snake_block])

# Display message
def display_message(msg, color):
    mssg = font_style.render(msg, True, color)
    display.blit(mssg, [width / 6, height / 3])

# Game loop
def game_loop():

    time.sleep(5)

    # Initial snake position
    snake_x = width / 2
    snake_y = height / 2

    # Initial snake movement
    snake_x_change = 0
    snake_y_change = 0

    # Initial snake body
    snake_list = []
    snake_length = 1

    # Initial food position
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Main game loop
    game_over = False
    close_game = False

    while not game_over:

        while close_game:
            display.fill(blue)
            display_message("Game Over! Press Q to Quit or P to Play Again!", red)
            display_score(snake_length - 1)
            pygame.display.update()

            # Handle restart / quit event
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        close_game = False
                    if event.key == pygame.K_p:
                        game_loop()

        # Handle player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                if event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block
                    snake_y_change = 0
                if event.key == pygame.K_UP:
                    snake_x_change = 0
                    snake_y_change = -snake_block
                if event.key == pygame.K_DOWN:
                    snake_x_change = 0
                    snake_y_change = snake_block

        # Boundary check
        if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
            close_game = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        display.fill(black)
        pygame.draw.rect(display, blue, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                close_game = True
        
        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Check if snake has eaten food
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    input("Press Enter to exit...")

# Run game
try:
    game_loop()
except Exception as e:
    print(f"An error occured: {e}")
    pygame.quit()
    input("Press Enter to exit...")