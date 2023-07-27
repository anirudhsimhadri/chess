import pygame
import sys

WIDTH, HEIGHT = 900, 900
BORDER = 0, 0, WIDTH, HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = 255, 255, 255
BLACK = 0, 0, 0

def draw_window():
    WIN.fill(WHITE)
    # pygame.draw.rect(WIN, WHITE, BORDER)
    full_border()
    credentials_borders()
    pygame.display.update()

def full_border():

    pygame.draw.rect(WIN, BLACK, (0, 0, WIDTH, 5))  # Top border
    pygame.draw.rect(WIN, BLACK, (0, 0, 5, HEIGHT))  # Left border
    pygame.draw.rect(WIN, BLACK, (0, HEIGHT - 5, WIDTH, 5))  # Bottom border
    pygame.draw.rect(WIN, BLACK, (WIDTH - 5, 0, 5, HEIGHT)) # Right border

def credentials_borders():
    pygame.draw.rect(WIN, BLACK, (((WIDTH/2) - (338/2)), HEIGHT - 550, 200, 35), 4, border_radius=1)
    pygame.draw.rect(WIN, BLACK, (((WIDTH/2) - (338/2)), HEIGHT - 500, 200, 35), 4, border_radius=1)
    pygame.draw.rect(WIN, BLACK, (((WIDTH/2) - (338/2)), HEIGHT - 450, 200, 35), 4, border_radius=1)

def main():
    run = True
    while run:
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LCTRL and event.key == pygame.K_w:
            #         run = False
        pygame.display.update()

if __name__ == "__main__":
    main()