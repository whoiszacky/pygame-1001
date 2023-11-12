import pygame
import sys
import random

# Colors
black = (0, 0, 0)                # background color 
red = (255, 0, 0)               # the object color 
white = (255, 255, 255)         # enemy obeject

# Initialize Pygame
pygame.init()

#the screen size 
screen_width = 640
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Exciting Collision Game")

class GameObject:
    def __init__(self, x, y, color=red):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.width = 50
        self.height = 50
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def update(self, screen_width, screen_height):
        self.x += self.vel_x
        self.y += self.vel_y

        # Boundary checks
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > screen_width:
            self.x = screen_width - self.width

        if self.y < 0:
            self.y = 0
        elif self.y + self.height > screen_height:
            self.y = screen_height - self.height

    def check_collision(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )

class Obstacle(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, color=white)
        self.width = 30
        self.height = 30

    def update(self, screen_width, screen_height, speed):
        # Move the obstacle horizontally
        self.x -= speed

        # Reset position if it goes off-screen
        if self.x + self.width < 0:
            self.x = screen_width
            self.y = random.randint(0, screen_height - self.height)

def display_score(score, font, surface):
    score_text = font.render(f"Score: {score}", True, white)
    surface.blit(score_text, (10, 10))

def display_message(message, font, surface, screen_width, screen_height):
    text = font.render(message, True, white)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    surface.blit(text, text_rect)

def main():
    clock = pygame.time.Clock()

    player = GameObject(100, 50)
    obstacles = [Obstacle(400, random.randint(0, screen_height - 30)) for _ in range(3)]

    font = pygame.font.Font(None, 36)
    score = 0
    speed = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for user input to move the player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.vel_y = -1
                elif event.key == pygame.K_DOWN:
                    player.vel_y = 1
                elif event.key == pygame.K_RIGHT:
                    player.vel_x = 1
                elif event.key == pygame.K_LEFT:
                    player.vel_x = -1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.vel_y = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.vel_x = 0

        screen.fill(black)

        # Update player position and draw it
        player.update(screen_width, screen_height)
        player.draw(screen)

        # Update obstacle positions and draw them
        for obstacle in obstacles:
            obstacle.update(screen_width, screen_height, speed)
            obstacle.draw(screen)

            # Check for collision with obstacles
            if player.check_collision(obstacle):
                display_message("Game Over", font, screen, screen_width, screen_height)
                pygame.display.flip()
                pygame.time.wait(2000)  # Pause for 2 seconds
                return  # Exit the game

        # Increase speed over time
        speed += 0.004

        # Check for collision and update the score
        for obstacle in obstacles:
            if player.check_collision(obstacle):
                score -= 10  # Decrease score on collision
                obstacle.color = (255, 0, 0)  # Change obstacle color on collision
            else:
                obstacle.color = white  # Reset obstacle color if no collision

        score += 1  # Increase score if no collision

        # Display the score
        display_score(score, font, screen)

        pygame.display.flip()
        clock.tick(60)  # Cap the frame rate

if __name__ == "__main__":
    main()
