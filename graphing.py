import pygame
import random
import math
import turtle 

turtle.forward(10)

pygame.init()

display = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()
FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)

def game():
    
    while True:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
            
            display.fill(white)   
                        
            pygame.display.update()

            clock.tick(FPS)
        
game()


    