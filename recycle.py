import pgzrun
import random
WIDTH = 800
HEIGHT = 600
#player
bin = Actor("bin", (400, 550))
plastic = Actor("plastic_bag", (random.randint(50, 750), 0))
paper= Actor("paper_bag", (random.randint(50, 850), -200))
score = 0
lives = 3 
time = 30
game_over = False
def on_mouse_move(pos):
    bin.x = pos[0]
def countdown():
    global time, game_over
    if time > 0:
        time -= 1
    else:
        game_over = True
clock.schedule_interval(countdown, 1)
def update():
    global score, lives, game_over
    if not game_over:
        plastic.y += 5
        paper.y += 5
        if plastic.y > HEIGHT:
            plastic.y = 0
            plastic.x = random.randint(50, 750)
            lives -= 1
        if paper.y > HEIGHT:
            paper.y = -200
            paper.x = random.randint(50, 850)
            lives -= 1
        if bin.colliderect(plastic):
            score += 1
            plastic.y = 0
            plastic.x = random.randint(50, 750)
        if bin.colliderect(paper):
            score += 2
            paper.y = -200
            paper.x = random.randint(50, 850)
        if lives <= 0:
            game_over = True
def draw():
    screen.fill("darkblue")
    screen.bgcolour = "lightblue"
    if game_over:
        screen.draw.text("Game Over", (WIDTH // 2 - 50, HEIGHT // 2), fontsize=30, color="black")
    else:
        screen.fill("lightblue")
        screen.draw.text("Score: " + str(score), (10, 10), fontsize=30, color="black")
        screen.draw.text("Lives: " + str(lives), (10, 50), fontsize=30, color="black")
        screen.draw.text("Time: " + str(time), (10, 90), fontsize=30, color="black")
        bin.draw()
        plastic.draw()
        paper.draw()
pgzrun.go()














