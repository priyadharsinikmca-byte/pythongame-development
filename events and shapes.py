import pygame
pygame.init()
screen = pygame.display.set_mode((800,900))
pygame.display.set_caption("shapes and events")
class Circle:
    def __init__(self):
        self.radius = 30

    def draw(self):
        pygame.draw.circle(screen,"blue",(300,250),self.radius)

obj = Circle()
running = True 
while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            obj.radius += 100
        if event.type == pygame.MOUSEBUTTONUP:
            obj.radius = 30
    obj.draw()
    pygame.display.update()

pygame.quit()
    









