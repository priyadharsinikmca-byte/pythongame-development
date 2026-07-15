import pgzrun
import pgzero.screen

WIDTH = 800
HEIGHT = 600

bee1 = Actor("bee",(280,345))
flower1 = Actor("flower",(534,412))


def draw():
    screen.clear()
    screen.fill("darkgreen")
    bee1.draw()
    flower1.draw()
    screen.draw.text("use arrow keys to move bee",(10,10),color="black")

def update():
    if keyboard.left:
        bee1.x -= 5
    if keyboard.right:
        bee1.x += 5
    if keyboard.up:
        bee1.y -= 5
    if keyboard.down:
        bee1.y += 5
    if bee1.colliderect(flower1):
        print("bee is on flower")


pgzrun.go()













