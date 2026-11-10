import pygame
import time 

pygame.init()
screen = pygame.display.set_mode((600,700))
pygame.display.set_caption("Merry Christmas")
font = pygame.font.SysFont("arial", 50)
small_font = pygame.font.SysFont("arial", 30) 
start_time = time.time()
page = 1
running = True
while running:
    screen.fill("red")
    current_time = time.time() - start_time
    if current_time >3:
        page = 2
    if page == 1:
        text = font.render("Merry Christmas",True,"black")
        screen.blit(text,(180,175))
        message = small_font.render("Have a happy new year",True,"black")
        screen.blit(message,(200,150))
    else:
        text = font.render("Merry Christmas!", True, "blue")
        screen.blit(text, (200, 150))

        message = small_font.render("Wishing you and your family lots of happiness!", True, "white")
        screen.blit(message, (180, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()

 
