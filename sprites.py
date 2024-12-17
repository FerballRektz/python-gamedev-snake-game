import random
import pygame
import pygame.math as pygmath


class Snake_fruits:
    def __init__(self: object, screen: object, 
                 cell_num: int, cell_size: int) -> object:
        """
        Constructor for fruit sprite

        :param self: object self call 
        :type self: object 
        :param screen: a screen object in pygame to be passed
        :type screen: object
        :param cell_num: number of cells in the background of python snake game
        :type cell_num: int 
        :param cell_size: size of cell (in pixels)
        :type cell_size: int
        :return: an snake fruit object
        :rtype: object
        :raises ValueError: N/A
        :example: N/A
        """
        self.CELL_SIZE = cell_size
        self.CELL_NUMBER = cell_num
        self.screen = screen
        self.randomize_fruit()
    
    def draw_fruit(self: object) -> None:
        """
        Snake fruit object method for drawing the fruit

        :param self: object self call 
        :type self: object 
        :return: N/A
        :rtype: N/A
        :raises ValueError: N/A
        :example: N/A

        """
        fruit_rect = pygame.Rect(int(self.x * self.CELL_SIZE),int(self.y * self.CELL_SIZE),
                                 self.CELL_SIZE, self.CELL_SIZE)
        pygame.draw.rect(self.screen, (255,0,0),fruit_rect)
    
    def randomize_fruit(self: object) -> None:
        """
        Snake fruit object method for making fruit locations random

        :param self: object self call 
        :type self: object 
        :return: N/A
        :rtype: N/A
        :raises ValueError: N/A
        :example: N/A
        """
        self.x  = random.randint(0,self.CELL_NUMBER - 1)
        self.y = random.randint(0,self.CELL_NUMBER - 1)
        self.pos = pygmath.Vector2(self.x,self.y)

class Snake_sprite:

    def __init__(self: object, screen: object, 
                 cell_num: int, cell_size: int) -> object:
        """
        Constructor for snake sprite

        :param self: object self call 
        :type self: object 
        :param screen: a screen object in pygame to be passed
        :type screen: object
        :param cell_num: number of cells in the background of python snake game
        :type cell_num: int 
        :param cell_size: size of cell (in pixels)
        :type cell_size: int
        :return: an snake fruit object
        :rtype: object
        :raises ValueError: N/A
        :example: N/A
        """
        self.CELL_SIZE = cell_size
        self.CELL_NUMBER = cell_num
        self.screen = screen
        self.body = [pygmath.Vector2(10,11),
                     pygmath.Vector2(11,11),pygmath.Vector2(12,11)]
        self.snake_direction = pygmath.Vector2(1,0)
        self.add_length = False
    
    def draw_snake(self: object)-> None:
        """
        Snake sprite object method drawing snake

        :param self: object self call 
        :type self: object 
        :return: N/A
        :rtype: N/A
        :raises ValueError: N/A
        :example: N/A
        """
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x * self.CELL_SIZE),int(block.y * self.CELL_SIZE),
                                    self.CELL_SIZE, self.CELL_SIZE)
            pygame.draw.rect(self.screen,(210, 19, 240),snake_rect)
    
    def move_snake(self: object) -> None:
        """
        Snake sprite object method for making the snake move

        :param self: object self call 
        :type self: object 
        :return: N/A
        :rtype: N/A
        :raises ValueError: N/A
        :example: N/A
        """
        if self.add_length:
            body_copy = self.body[:]
            body_copy.insert(0,  body_copy[0] + self.snake_direction)
            self.body = body_copy[:]
            self.add_length = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,  body_copy[0] + self.snake_direction)
            self.body = body_copy[:]

    def grow_snake(self: object) -> None:
        """
        Snake sprite object method to allow the growth of snake 
        (in conjuction with move_snake method)

        :param self: object self call 
        :type self: object 
        :return: N/A
        :rtype: N/A
        :raises ValueError: N/A
        :example: N/A
        """
        self.add_length = True
    
    def snake_fail (self: object) -> None:
        """
        Snake sprite object method to restart the snake into its
        original size upon failure
        :param self: object self call 
        :type self: object 
        :return: N/A
        :rtype: N/A
        :raises ValueError: N/A
        :example: N/A
        """
        self.body = [pygmath.Vector2(10,11),
                pygmath.Vector2(11,11),pygmath.Vector2(12,11)]
        self.snake_direction = pygmath.Vector2(0,0)