import pygame

def draw_grass(CELL_NUMBER: int, CELL_SIZE: int, screen: object) -> None:
    """
    Function that draws grass background in the snake game

    :param CELL_NUMBER: number of cells in the background of python snake game
    :type CELL_NUMBER: int 
    :param CELL_SIZE: size of cell (in pixels)
    :type CELL_SIZE: int
    :param screen: a screen object in pygame to be passed
    :type screen: object
    :return: N/A
    :rtype: N/A
    :raises ValueError: N/A
    :example: N/A
    """
    dark_grass_color = (96, 237, 101)
    for row in  range(CELL_NUMBER):
        if row % 2 == 0:
            for column in range(CELL_NUMBER):
                if column % 2 == 0:
                        dark_grass_rect = pygame.Rect(column * CELL_SIZE, row * CELL_SIZE, 
                                                      CELL_SIZE,CELL_SIZE)
                        pygame.draw.rect(screen,dark_grass_color,dark_grass_rect)
        else:
            for column in range(CELL_NUMBER):
                if column % 2 != 0:
                    dark_grass_rect = pygame.Rect(column * CELL_SIZE, row * CELL_SIZE, 
                                                    CELL_SIZE,CELL_SIZE)
                    pygame.draw.rect(screen,dark_grass_color,dark_grass_rect)

def check_collision (snake: object, fruit: object) -> None:
    """
    Function to determine if the snake obtains the fruit

    :param snake: the snake sprite object
    :type snake: object
    :param fruit: the fruit sprite object
    :type fruit: object
    :return: N/A
    :rtype: N/A
    :raises ValueError: N/A
    :example: N/A
    """
    if snake.body[0] == fruit.pos:
        fruit.randomize_fruit()
        snake.grow_snake()

    for block in snake.body[1:]:
        if block == fruit.pos:
            fruit.randomize_fruit()

def check_fail (CELL_NUMBER: int, snake: object) -> None:
    """
    Function to determine the conditions where the snake gamw will fail
    (call the snake_fail method)

    :param CELL_NUMBER: number of cells in the background of python snake game
    :type CELL_NUMBER: int 
    :param snake: the snake sprite object
    :type snake: object
    :return: N/A
    :rtype: N/A
    :raises ValueError: N/A
    :example: N/A
    """
    if not 0 <= snake.body[0].x < CELL_NUMBER or not 0 <= snake.body[0].y < CELL_NUMBER:
        snake.snake_fail()
    
    for block in snake.body[1:]:
        if block == snake.body[0]:
            snake.snake_fail()

def draw_score(game_font: object, CELL_SIZE: int, screen: object,snake: object) -> None:
    """
    Function that draws the score (number of fruits eaten by snake)
    it is shown in the top right area

    :param game_font: a pygame font object
    :type game_font: object
    :param CELL_SIZE: size of cell (in pixels)
    :type CELL_SIZE: int 
    :param screen: a screen object in pygame to be passed
    :type screen: object
    :param snake: the snake sprite object
    :type snake: object
    :return: N/A
    :rtype: N/A
    :raises ValueError: N/A
    :example: N/A
    """
    score_text = str(len(snake.body) - 3)
    score_surface = game_font.render(score_text,True,(0,0,0))
    score_x_loc = int(25)
    score_y_loc = int(20)    
    score_rect = score_surface.get_rect(center = (score_x_loc,score_y_loc))
    fruit_rect = pygame.Rect(score_rect.right + 5,score_rect.top + 9,
                            CELL_SIZE - 5, CELL_SIZE - 5)
    

    screen.blit(score_surface,score_rect)
    pygame.draw.rect(screen,(255,0,0),fruit_rect)