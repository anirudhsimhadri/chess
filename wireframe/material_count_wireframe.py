import pygame
import sys

WIDTH, HEIGHT = 900, 900
BORDER = 0, 0, WIDTH, HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

WHITE = 255, 255, 255
BLACK = 0, 0, 0

def draw_window():

    WIN.fill(WHITE)
    pygame.draw.rect(WIN, WHITE, BORDER)
    full_border()
    material_tracking_border()
    pygame.display.update()

def full_border():

    pygame.draw.rect(WIN, BLACK, (0, 0, WIDTH, 5))  # Top border
    pygame.draw.rect(WIN, BLACK, (0, 0, 5, HEIGHT))  # Left border
    pygame.draw.rect(WIN, BLACK, (0, HEIGHT - 5, WIDTH, 5))  # Bottom border
    pygame.draw.rect(WIN, BLACK, (WIDTH - 5, 0, 5, HEIGHT)) # Right border

def material_tracking_border():
    pygame.draw.rect(WIN, BLACK, (0, 0, 338, 100), 4, border_radius=1)
    pygame.draw.rect(WIN, BLACK, (0, HEIGHT-100, 338, 100), 4, border_radius=1)

def main():
    # clock = pygame.time.Clock()
    run = True
    while run:
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
    
    pygame.quit()

if __name__ == "__main__":
    main()
