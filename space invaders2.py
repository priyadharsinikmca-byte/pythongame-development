import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

player_img = pygame.image.load("spaceship.png")
player_img = pygame.transform.scale(player_img, (60, 60))

enemy_img = pygame.image.load("enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (60, 60))

player = pygame.Rect(370, 500, 60, 60)
enemy = pygame.Rect(370, 50, 60, 60)

bullets = []
score = 0
running = True

while running:
    clock.tick(60)
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx, player.top, 5, 15))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5

    if keys[pygame.K_RIGHT] and player.right < 800:
        player.x += 5

    enemy.x += 3

    if enemy.right > 800 or enemy.left < 0:
        enemy_speed = 3
        if enemy.right > 800:
            enemy.x = 740
        else:
            enemy.x = 0
        enemy_speed = -enemy_speed

    for bullet in bullets[:]:
        bullet.y -= 7

        if bullet.colliderect(enemy):
            bullets.remove(bullet)
            score += 1
            enemy.x = random.randint(0, 740)

        elif bullet.bottom < 0:
            bullets.remove(bullet)

    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)

    for bullet in bullets:
        pygame.draw.rect(screen, "yellow", bullet)

    text = font.render("Score: " + str(score), True, "white")
    screen.blit(text, (20, 20))

    pygame.display.update()

pygame.quit()
   

