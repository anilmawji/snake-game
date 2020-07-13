import pygame
import food
from constants import *
from snake import Snake


def main():
    pygame.init()
    pygame.display.set_caption('Snake Game')
    pygame.mouse.set_visible(False)

    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake()
    score = 0
    high_score = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if snake.get_direction() != LEFT and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    snake.set_direction(RIGHT)
                elif snake.get_direction() != RIGHT and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    snake.set_direction(LEFT)
                elif snake.get_direction() != DOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
                    snake.set_direction(UP)
                elif snake.get_direction() != UP and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    snake.set_direction(DOWN)
        snake.tick()

        display.fill(BLACK)
        if SHOW_GRID:
            render_grid(display)
        display.blit(font.render('Score: ' + str(score), True, WHITE), (2, 2))
        display.blit(font.render('High Score: ' + str(high_score), True, WHITE), (2, 36))
        food.render(display)
        snake.render(display)

        if snake.collides_with(food.x, food.y):
            food.move()
            snake.grow()
            score += 1
            if score > high_score:
                high_score = score
        elif snake.is_dead():
            score = 0

        pygame.display.flip()
    pygame.quit()


def render_grid(display):
    for x in range(DISPLAY_WIDTH // SCALE):
        pygame.draw.line(display, GRAY, (x * SCALE, 0), (x * SCALE, DISPLAY_HEIGHT))

    for y in range(DISPLAY_HEIGHT // SCALE):
        pygame.draw.line(display, GRAY, (0, y * SCALE), (DISPLAY_WIDTH, y * SCALE))


if __name__ == '__main__':
    main()
