import pygame
import random

pygame.init()

# setting up the screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
snake_block = 10
clock = pygame.time.Clock()

# starting position,food
x, y = width // 2, height // 2
x_change, y_change = 0, 0
snake = [[x, y]]
food_x = random.randint(0, (width - snake_block) // 10) * 10
food_y = random.randint(0, (height - snake_block) // 10) * 10
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change, y_change = -snake_block, 0
            elif event.key == pygame.K_RIGHT:
                x_change, y_change = snake_block, 0
            elif event.key == pygame.K_UP:
                x_change, y_change = 0, -snake_block
            elif event.key == pygame.K_DOWN:
                x_change, y_change = 0, snake_block

    # move snake
    x += x_change
    y += y_change
    snake.append([x, y])

    # checking food
    if x == food_x and y == food_y:
        score += 1
        food_x = random.randint(0, (width - snake_block) // 10) * 10
        food_y = random.randint(0, (height - snake_block) // 10) * 10
    else:
        snake.pop(0)  # Move forward by removing tail unless food is eaten

    # game over
    if x < 0 or x >= width or y < 0 or y >= height or [x, y] in snake[:-1]:
        running = False

    # drawing
    screen.fill(black)
    for segment in snake:
        pygame.draw.rect(screen, white, [segment[0], segment[1], snake_block, snake_block])
    pygame.draw.rect(screen, green, [food_x, food_y, snake_block, snake_block])
    pygame.display.set_caption("Snake Game | Score: " + str(score))
    pygame.display.update()

    clock.tick(15)

pygame.quit()
