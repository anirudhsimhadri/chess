import pygame
from BoardConstants import BoardConstants as BC

Surface = pygame.Surface

BC = BC()
WINDOW_SIZE = BC.WINDOW_SIZE
BOARD_SIZE = BC.BOARD_SIZE

def draw_result_screen(screen: Surface, did_win: bool):
    """Draws the win/lose screen after the game has ended"""
    font = pygame.font.SysFont("Arial", 96)
    text = font.render(
        "You won" if did_win else "You lost",
        True,
        (0xff, 0x00, 0x00)
    )
    text_rect = text.get_rect(
        center=(BOARD_SIZE // 2, WINDOW_SIZE // 2)
    )

    screen.blit(text, text_rect)

