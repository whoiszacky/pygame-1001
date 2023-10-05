import pygame

# background väärin
black = (0, 0, 0)

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.width = 50
        self.height = 50

    def draw(self, surface):
        #objektin vääri
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def update(self, screen_width, screen_height):
        # update position based on x and y
        self.x += self.vel_x
        self.y += self.vel_y

        # 
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > screen_width:
            self.x = screen_width - self.width

        if self.y < 0:
            self.y = 0
        elif self.y + self.height > screen_height:
            self.y = screen_height - self.height

pygame.init()

# set up screen
screen_width = 640
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Piirtäminen")

# create our object
object = GameObject(100, 50)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # check for user input to move object
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    object.vel_y = -1
                elif event.key == pygame.K_DOWN:
                    object.vel_y = 1
                elif event.key == pygame.K_RIGHT:
                    object.vel_x = 1
                elif event.key == pygame.K_LEFT:
                    object.vel_x = -1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    object.vel_y = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    object.vel_x = 0

        screen.fill(black)

        # update object position and draw it
        object.update(screen_width, screen_height)
        object.draw(screen)

        pygame.display.flip()

main()
