# pygame-1001# Object Movement in Pygame

This is a simple Pygame project demonstrating how to create a game object and move it using user input. The object is represented as a rectangle that can be moved in four different directions (up, down, left, and right) using arrow keys.

## Requirements

To run this code, you need to have Python and Pygame installed on your machine. If you don't have Pygame installed, you can install it using pip:
```
pip install pygame
```

## How to Run

To run the code, simply run the 'piirtäminen.py' file using Python:
```
python piirtäminen.py
```

## How to Play

- Use the up, down, left, and right arrow keys to move the object.
- The object can move within the boundaries of the screen.
- The object is represented as a red rectangle on a black background.

## Code Overview

- The `GameObject` class represents the game object with its x and y coordinates, velocity, width, and height.
- The `draw` function is responsible for drawing the object on the screen.
- The `update` function is responsible for updating the object's position.
- In the main game loop, we handle user input and update the object's position accordingly.
- We then draw the object on the screen and update it using `pygame.display.flip()`.

## Zakaria
