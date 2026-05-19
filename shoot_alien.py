import random

WIDTH = 800
HEIGHT = 600

# Alien position
alien_x = 400
alien_y = 300

# Alien size
alien_radius = 30

# Score
score = 0

def draw():
    screen.clear()
    screen.fill("black")

    # Draw alien as green circle
    screen.draw.filled_circle(
        (alien_x, alien_y),
        alien_radius,
        "green"
    )

    # Draw score
    screen.draw.text(
        f"Score: {score}",
        topleft=(10, 10),
        fontsize=40,
        color="white"
    )

def on_mouse_down(pos):
    global alien_x, alien_y, score

    mouse_x = pos[0]
    mouse_y = pos[1]

    # Distance check
    distance = ((mouse_x - alien_x)**2 + (mouse_y - alien_y)**2)**0.5

    # If clicked on alien
    if distance < alien_radius:
        score += 1

        # Move alien randomly
        alien_x = random.randint(50, WIDTH - 50)
        alien_y = random.randint(50, HEIGHT - 50)