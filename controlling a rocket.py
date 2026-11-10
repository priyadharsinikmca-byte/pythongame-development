import pygame
from  pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Rockets In Space")

rocket = pygame.image.load("spaceship.png")
rocket = pygame.transform.scale(rocket,(50,70))
x = 375
y = 500
speed = 5
running = True
while running:
    screen.fill("black")
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == K_DOWN:
                 y += speed
            if event.type == K_UP:
                 y -= speed
            if event.type == K_LEFT:
                 x -= speed
            if event.type == K_RIGHT:
                 x += speed
    screen.blit(rocket, (x, y))

    pygame.display.update()

pygame.quit()
    
