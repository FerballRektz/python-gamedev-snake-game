import sys
import random
import pygame
import pygame.math as pygmath
import snake_functions 
import sprites


#GLOBAL DEFINITIONS
pygame.init()
CELL_SIZE: int = 20
CELL_NUMBER: int = 23

pygame.display.set_caption("Basic Python Snake Game")
screen = pygame.display.set_mode(( CELL_SIZE * CELL_NUMBER ,
                                    CELL_SIZE * CELL_NUMBER))
clock =  pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,140)


game_font = pygame.font.Font(None, 50)

#sprites 
fruits: object = sprites.Snake_fruits(cell_num= CELL_NUMBER, cell_size= CELL_SIZE,screen= screen)
snake: object = sprites.Snake_sprite(cell_num= CELL_NUMBER, cell_size= CELL_SIZE,screen= screen)

# main function 
def main() -> None:
    run: bool = True
    while run:
        screen.fill((114, 255, 119)) #background screen color
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                run = False
            if event.type == SCREEN_UPDATE:
                snake.move_snake()
                snake_functions.check_collision(snake,fruits)
                snake_functions.check_fail(CELL_NUMBER= CELL_NUMBER, snake= snake)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.snake_direction.y != 1:
                        snake.snake_direction = pygmath.Vector2(0,-1)
                elif event.key == pygame.K_DOWN:
                    if snake.snake_direction.y != -1:
                        snake.snake_direction = pygmath.Vector2(0,1)
                elif event.key == pygame.K_LEFT:
                    if snake.snake_direction.x != 1:
                        snake.snake_direction = pygmath.Vector2(-1,0)
                elif event.key == pygame.K_RIGHT:
                    if snake.snake_direction.x != -1:
                        snake.snake_direction = pygmath.Vector2(1,0)        
        snake_functions.draw_grass(CELL_NUMBER= CELL_NUMBER,CELL_SIZE= CELL_SIZE,
                                screen = screen)
        fruits.draw_fruit() # fruits
        snake.draw_snake() # snake
        snake_functions.draw_score(game_font= game_font, CELL_SIZE= CELL_SIZE, 
                                   screen = screen, snake = snake)
        pygame.display.update()
        clock.tick(60) # 60 fps

    pygame.quit()
    sys.exit()



if __name__  == "__main__":
    main()