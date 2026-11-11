import pygame
import pyzrun

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Space Invaders")
font = pygame.font.SysFont("arial", 50)
big_font = pygame.font.SysFont("arial", 30) 

#player's spaceship

player = pygame.Rect((375,500,50,50))

clock = pygame.time.clock()
running = True

score = 0
lives = 5

while running:
    screen.fill("black")

