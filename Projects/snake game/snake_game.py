import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


# Define a class for the cube which will represent the snake and the snack
class cube(object):
    rows = 20  # Number of rows in the grid
    w = 500  # Width of the window

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start  # Position of the cube
        self.dirnx = dirnx  # Direction on the x-axis
        self.dirny = dirny  # Direction on the y-axis
        self.color = color  # Color of the cube

    # Move the cube in the direction of dirnx and dirny
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    # Draw the cube on the surface
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows  # Distance between lines in the grid
        i = self.pos[0]  # Row position
        j = self.pos[1]  # Column position

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if eyes:  # Draw eyes if it's the head of the snake
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


# Define a class for the snake
class snake(object):
    body = []  # List to store the body of the snake
    turns = {}  # Dictionary to store the turns

    def __init__(self, color, pos):
        self.color = color  # Color of the snake
        self.head = cube(pos)  # The head of the snake is a cube
        self.body.append(self.head)  # Add the head to the body
        self.dirnx = 0  # Direction on the x-axis
        self.dirny = 1  # Direction on the y-axis

    # Function to handle the movement of the snake
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()  # Get the keys that are pressed

            for key in keys:
                if keys[pygame.K_LEFT]:  # Move left
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:  # Move right
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:  # Move up
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:  # Move down
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:  # If the position is in turns, move accordingly
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:  # Handle the edge of the screen
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1: c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows - 1)
                else: c.move(c.dirnx, c.dirny)

    # Reset the snake to the starting position
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    # Add a cube to the snake's body
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    # Draw the snake on the surface
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)  # Draw the head with eyes
            else:
                c.draw(surface)


# Function to draw the grid
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows  # Distance between lines

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


# Function to redraw the window
def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0, 0, 0))  # Fill the surface with black
    s.draw(surface)  # Draw the snake
    snack.draw(surface)  # Draw the snack
    drawGrid(width, rows, surface)  # Draw the grid
    pygame.display.update()  # Update the display


# Function to get a random position for the snack
def randomSnack(rows, item):
    positions = item.body  # Get the positions of the snake's body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


# Function to show a message box
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


# Main function
def main():
    global width, rows, s, snack
    width = 500  # Width of the window
    rows = 20  # Number of rows
    win = pygame.display.set_mode((width, width))  # Set the window size
    s = snake((255, 0, 0), (10, 10))  # Create a snake
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))  # Create a snack
    flag = True  # Variable to keep the game running

    clock = pygame.time.Clock()  # Create a clock object

    while flag:
        pygame.time.delay(50)  # Delay the game
        clock.tick(10)  # Set the frame rate
        s.move()  # Move the snake
        if s.body[0].pos == snack.pos:  # Check if the snake eats the snack
            s.addCube()  # Add a cube to the snake
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))  # Create a new snack

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):  # Check if the snake hits itself
                print('Score: ', len(s.body))
                message_box('You Lost! Play again...', f"Score: {len(s.body)}")
                s.reset((10, 10))  # Reset the snake
                break

        redrawWindow(win)  # Redraw the window

    pass


main()  # Start the game