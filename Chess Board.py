import pygame

# set up the Pygame window
pygame.init()
WINDOW_SIZE = (512, 512)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Chess Board")

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# set the size of each square on the chess board
SQUARE_SIZE = 64

# draw the chess board
for row in range(8):
    for col in range(8):
        x = col * SQUARE_SIZE
        y = row * SQUARE_SIZE
        if (row + col) % 2 == 0:
            color = WHITE
        else:
            color = GRAY
        pygame.draw.rect(screen, color, [x, y, SQUARE_SIZE, SQUARE_SIZE])

# update the display
pygame.display.update()

# run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit Pygame
pygame.quit()
