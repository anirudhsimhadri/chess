import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Login Page")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load the font
font = pygame.font.Font(None, 30)

# Function to display text on the screen
def display_text(text, x, y):
    rendered_text = font.render(text, True, BLACK)
    screen.blit(rendered_text, (x, y))


# Main game loop
def login_page():
    loop = True

    username = ""
    password = ""
    port = ""
    ip = ""

    active_input = "username"

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if active_input == "username":
                        active_input = "password"
                    elif active_input == "password":
                        active_input = "port"
                    elif active_input == "port":
                        active_input = "ip"
                    elif active_input == "ip":
                        loop = False

                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace
                    if active_input == "username":
                        username = username[:-1]
                    elif active_input == "password":
                        password = password[:-1]
                    elif active_input == "port":
                        port = port[:-1]
                    elif active_input == "ip":
                        ip = ip[:-1]

                else:
                    # Handles other keypresses:
                    if active_input == "username":
                        username += event.unicode
                    elif active_input == "password":
                        password += event.unicode
                    elif active_input == "port":
                        port += event.unicode
                    elif active_input == "ip":
                        ip += event.unicode

        screen.fill(WHITE)

        # Display text input labels
        display_text("Username:", 100, 100)
        display_text("Password:", 100, 200)
        display_text("Port:", 100, 300)
        display_text("IP:", 100, 400)

        # Display input text
        display_text(username, 250, 100)
        display_text("*" * len(password), 250, 200)  # Display asterisks for password
        display_text(port, 250, 300)
        display_text(ip, 250, 400)

        # Highlight active input field
        if active_input == "username":
            pygame.draw.rect(screen, BLACK, (240, 95, 250, 40), 2)  # Username
        if active_input == "password":
            pygame.draw.rect(screen, BLACK, (240, 195, 250, 40), 2)  # Password
        if active_input == "port":
            pygame.draw.rect(screen, BLACK, (240, 295, 250, 40), 2)  # Port
        if active_input == "ip":
            pygame.draw.rect(screen, BLACK, (240, 395, 250, 40), 2)  # IP

        pygame.display.update()
    
    "connect to server"

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    login_page()
