###############################################################################################
#   VPython Single Player Pong                                                                #
#   File: pong.py                                                                             #
#   Author: Michael Morgan Wise                                                               #
#   Description: A single player, simplified version of a classic game.                       #
###############################################################################################

from visual import *
import random

# Set necessary variables
maxScore = 10
animationRate = 1500
score = 0
deltaT = 0.001

# Create and customize windows
w = window(title = 'Single Player Pong', width = 700, height = 700)
scene = display(window = w, width = 700, height = 700, center = (0,0,0), range = (75,75,100))
#scene.stereo = 'redcyan' # For 3D Glasses

# Create room
rightWall = box(size=(1,101,25),pos=(50,0,0), material = materials.wood, color=(1,0.7,0.2))
bottomWall = box(size=(100,1,25),pos=(0,-50,0), material = materials.wood, color=(1,0.7,0.2))
topWall = box(size=(100,1,25),pos=(0,50,0), material = materials.wood, color=(1,0.7,0.2))
floor = box(size=(100,100,1),pos=(0,0,-12.5), material = materials.wood, color=(1,0.7,0.2))

# Create a score box
scoreLabel = label(text = 'Score: %d'%score, font='serif', pos=(0,65,0), border = 6)

# Create a pad
pad = cylinder(pos=(-50,0,0), radius = 10, material = materials.wood)

# Create a ball
ball = sphere(radius=2, material = materials.rough)

# Set the velocity vector for the ball
ball.velocity = vector(random.randint(15,45),random.randint(15,45),0)

# Generic Animation Loop
while score < maxScore and score >= 0:
    # Edit animation rate to allow for smooth generation
    rate(animationRate)

    # Ball bouncing logic
    if ball.pos.x > 48:
        ball.velocity.x = -ball.velocity.x
    # Scoring logic
    elif ball.pos.x < -48 and ball.pos.x > -49 and ball.pos.y < pad.pos.y+pad.radius and ball.pos.y > pad.pos.y-pad.radius:
        ball.velocity.x = -ball.velocity.x
        score = score + 1
        scoreLabel.text = 'Score: %d'%score

    # Ball bouncing logic
    if ball.pos.y > 48 and ball.pos.x < 48 and ball.pos.x > -48:
        ball.velocity.y = -ball.velocity.y
    elif ball.pos.y < -48 and ball.pos.x < 48 and ball.pos.x > -48:
        ball.velocity.y = -ball.velocity.y

    # Moves the paddle
    if scene.mouse.pos.y < 45 and scene.mouse.pos.y > -45:
        pad.pos.y = scene.mouse.pos.y

    # Actually moves the ball       
    ball.pos = ball.pos + ball.velocity*deltaT

    # If the ball is out of the box, show the game over screen and exit loop
    if ball.pos.x > 60 or ball.pos.x < -60 or ball.pos.y < -60 or ball.pos.y > 60:
        label(text = '      GAME OVER:\nYou dropped the ball.', font='serif')
        scoreLabel.visible = False
        score = -1;

# Give congratulations if they are in order
if score >= 0:
    label(text = 'CONGRATULATIONS!\n            You won!', font='serif')
