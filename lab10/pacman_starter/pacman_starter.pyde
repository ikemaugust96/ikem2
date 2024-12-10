WIDTH = 500
HEIGHT = 500
PACMAN_HEIGHT = 100
PACMAN_WIDTH = 100
SPEED = 3
x = WIDTH/2
y = HEIGHT/2
x_add = 0
y_add = 0
mouth_angle = 45  # Angle to control mouth opening
mouth_direction = 1  # Direction for the mouth opening/closing (1 for open, -1 for closed)
start_angle = radians(45)  # Initial mouth start angle
end_angle = radians(315)  # Initial mouth end angle

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    fill(1.0, 1.0, 0.0)
    noStroke()

def draw():
    global x, y,  start_angle, end_angle, x_add, y_add
    # Must be declared as global
    background(0)

    x = x + x_add
    y = y + y_add
    
    
    # The following cases deal with when PacMan
    # is near the edge of the screen
    
    # If PacMan moves completely behond the right edge 
    if (x > WIDTH + (PACMAN_WIDTH/2)): 
        # Reset the x value to the left side
        x = PACMAN_WIDTH/2
    # If PacMan is overlapping the right edge
    elif (x > WIDTH - (PACMAN_WIDTH/2)):
        # draw a second PacMan on the left side, also
        # overlapping
        pacman(x - WIDTH, y)
    
    # If PacMan moves past the bottom edge, 
    # redraw at the top
    if (y > HEIGHT + (PACMAN_HEIGHT/2)):
        y = PACMAN_HEIGHT/2
    elif (y > HEIGHT - (PACMAN_HEIGHT/2)):
        pacman(x, y - HEIGHT)
        
    # If PacMan moves past the left edge, 
    # redraw at the right   
    if (x < -(PACMAN_WIDTH/2)): 
        x = WIDTH - (PACMAN_WIDTH/2)
    elif (x < PACMAN_WIDTH/2):
        pacman(x + WIDTH, y)
    
    # If PacMan moves past the top, redraw at bottom
    if (y < -(PACMAN_HEIGHT/2)):
        y = HEIGHT - (PACMAN_HEIGHT/2)
    elif (y < PACMAN_HEIGHT/2):
        pacman(x, y + HEIGHT)
    
    # Always draw PacMan at his real current location.
    pacman(x, y)

def pacman(x, y):
    """Draw PacMan to the screen"""

    global start_angle, end_angle, mouth_angle, mouth_direction # Ensure global usage if required for angles
    
    mouth_angle += 2 * mouth_direction
    if mouth_angle >= 45:
        mouth_angle = 45
        mouth_direction = -1
    elif mouth_angle <= 0:
        mouth_angle = 0
        mouth_direction = 1

    # Set consistent angle order for each direction
    if x_add > 0:  # Moving right
        start_angle = radians(45-mouth_angle)
        end_angle = radians(315+mouth_angle)
    elif x_add < 0:  # Moving left
        start_angle = radians(225-mouth_angle)
        end_angle = radians(495+mouth_angle)
    elif y_add > 0:  # Moving down
        start_angle = radians(135-mouth_angle)
        end_angle = radians(405+mouth_angle)
    elif y_add < 0:  # Moving up
        start_angle = radians(315-mouth_angle)
        end_angle = radians(585+mouth_angle)  # Use 405 degrees to cross 0 smoothly
    else:  # Default to facing right if stationary
        start_angle = radians(45)
        end_angle = radians(315)

    # Draw Pac-Man with the calculated start and end angles
    arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT, start_angle, end_angle)
    
def keyPressed():
    global x_add, y_add  # Must be declared as global
    if (key == CODED):
        if (keyCode == DOWN):
            x_add = 0
            y_add = SPEED
        elif (keyCode == UP):
            x_add = 0
            y_add = -(SPEED)
        elif (keyCode == LEFT):
            x_add = -(SPEED)
            y_add = 0
        elif (keyCode == RIGHT):
            x_add = SPEED
            y_add = 0
