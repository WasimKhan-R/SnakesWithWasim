import pygame
import random

pygame.init()

screen_width = 600
screen_height = 450

gameWindow = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("SnakesWithWasim")
pygame.display.update()

font = pygame.font.SysFont(None, 55)
white = (255, 255, 255)
red = (255 , 0, 0)
black = (0 , 0 , 0)


def plot_snake(gameWindow, color, snk_list, snakes_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow , color, [x , y, snakes_size, snakes_size])
    # pygame.draw.rect(gameWindow , black, [snakes_x , snakes_y, snakes_size, snakes_size])

def text_screen(text,color,x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def gameLoop():
    # Game specific Variable
    exit_game = False
    game_over = False
    snakes_x = 45
    snakes_y = 55
    snakes_size = 10
    fps = 60

    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(20, screen_width/2)
    food_y =  random.randint(20, screen_height/2)

    clock = pygame.time.Clock()

    score = 0

    init_velocity = 5

    snk_list = []
    snk_length = 1

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over!",red,180,180)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # snakes_x = snakes_x + 5
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snakes_x = snakes_x + velocity_x
            snakes_y = snakes_y + velocity_y

            if abs(snakes_x - food_x) < 10 and abs(snakes_y - food_y) < 10:
                score+=1
                food_x = random.randint(20, screen_width/2)
                food_y =  random.randint(20, screen_height/2)
                snk_length +=5

                
            gameWindow.fill(white)
            text_screen("Score :"+str(score *10), red, 5,5)
            pygame.draw.rect(gameWindow , red, [food_x , food_y, snakes_size, snakes_size])

            head = []
            head.append(snakes_x)
            head.append(snakes_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
            # pygame.draw.rect(gameWindow , black, [snakes_x , snakes_y, snakes_size, snakes_size])
            if snakes_x < 0 or snakes_x > screen_width or snakes_y < 0 or snakes_y > screen_width:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snakes_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameLoop();