import pygame

# Initialize Pygame
pygame.init()

# Get the dimensions of the screen
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Set the screen to full screen mode
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Set the title of the screen
pygame.display.set_caption("Era of Conflict")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Define some fonts
title_font = pygame.font.SysFont(None, 100)
button_font = pygame.font.SysFont(None, 50)

# Create Title
title_text = title_font.render("Era of Conflict", True, (255, 255, 255))
title_text_rect = title_text.get_rect(center=(screen_width/2, screen_height/4))

# Create the Play button
play_button = pygame.Rect(screen_width//2-100, screen_height//2-50, 200, 50)
play_text = button_font.render("Play", True, WHITE)
play_text_rect = play_text.get_rect(center=play_button.center)

# Create the Credits button
credits_button = pygame.Rect(screen_width//2-100, screen_height//2+25, 200, 50)
credits_text = button_font.render("Credits", True, WHITE)
credits_text_rect = credits_text.get_rect(center=credits_button.center)

# Create the Quit button
quit_button = pygame.Rect(screen_width//2-100, screen_height//2+100, 200, 50)
quit_text = button_font.render("Quit", True, WHITE)
quit_text_rect = quit_text.get_rect(center=quit_button.center)

# Loop to keep the screen open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                # Start the game
                print("Starting the game...")
            elif credits_button.collidepoint(mouse_pos):
                # Show the credits
                print("Credits:")
                print("- Created by JJEntertainment")
            elif quit_button.collidepoint(mouse_pos):
                # Quit the game
                running = False

    # Draw the background and the buttons
    screen.fill(GRAY)
    screen.blit(title_text, title_text_rect)
    pygame.draw.rect(screen, BLACK, play_button)
    screen.blit(play_text, play_text_rect)
    pygame.draw.rect(screen, BLACK, credits_button)
    screen.blit(credits_text, credits_text_rect)
    pygame.draw.rect(screen, BLACK, quit_button)
    screen.blit(quit_text, quit_text_rect)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
