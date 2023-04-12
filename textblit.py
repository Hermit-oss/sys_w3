import pygame
import os
import sys
from button import Button, ToggleButton

import pygame

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((500, 500))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define fonts
font = pygame.font.SysFont(None, 50)

# Create the toggle button
button_image = pygame.Surface((200, 50))
button_image.fill(GREEN)
button_pos = (150, 200)
button_pos2 = (150, 300)
button_pos3 = (150, 400)
button_text = "Toggle Me!"
button_font = font
button_base_color = WHITE
button_hovering_color = RED
toggle_button = ToggleButton(button_image, button_pos, button_text, button_font, button_base_color, button_hovering_color)
toggle_button2 = ToggleButton(button_image, button_pos2, button_text, button_font, button_base_color, button_hovering_color)
toggle_button3 = ToggleButton(button_image, button_pos3, button_text, button_font, button_base_color, button_hovering_color)
# Game loop
running = True
while running:

        # Update screen
    screen.fill(BLACK)
    toggle_button.changeColor(pygame.mouse.get_pos())
    toggle_button.update(screen)
    toggle_button2.changeColor(pygame.mouse.get_pos())
    toggle_button2.update(screen)    
    toggle_button3.changeColor(pygame.mouse.get_pos())
    toggle_button3.update(screen)
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the toggle button was clicked
            mouse_pos = pygame.mouse.get_pos()
            toggle_button.checkForInput(mouse_pos)
            toggle_button2.checkForInput(mouse_pos)
            toggle_button3.checkForInput(mouse_pos)

    pygame.display.flip()

# Quit pygame
pygame.quit()
