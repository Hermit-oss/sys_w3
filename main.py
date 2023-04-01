import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Era of Conflict")

# Load assets
# Fonts
game_title_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 140)
button_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 90)
select_title_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 100)
select_button_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 50)
# Sounds
button_hover_sound = pygame.mixer.Sound(os.path.join("assets", "snd", "hover.wav"))
title_screen_intro = pygame.mixer.music.load("assets/snd/intro.wav")
# Graphics
border = pygame.transform.scale(pygame.image.load('assets/img/border.png').convert_alpha(), (width, 80))
BG = pygame.image.load(os.path.join("assets", "img", "bgwood.jpg"))
frames = []
for i in range(1, 120):
    filename = os.path.join('assets/img/background', f'frame{i}.png')
    frame = pygame.transform.scale(pygame.image.load(filename).convert_alpha(), screen.get_size())
    frames.append(frame)

# Set up game title
game_title_text = game_title_font.render("Era of Conflict", True, (180, 150, 100))
game_title_rect = game_title_text.get_rect(center=(width // 2, height // 1.06))

# Set up main menu border rectangle
border_rect = border.get_rect(center=(width // 2, height // 7))

# Set up play button
play_button_text = button_font.render("PLAY", True, (180, 150, 100))
play_button_rect = play_button_text.get_rect(center=(width // 5, height // 16))
rendered_play_button_text = play_button_text

# Set up credits button
credits_button_text = button_font.render("CREDITS", True, (180, 150, 100))
credits_button_rect = credits_button_text.get_rect(center=(width // 2, height // 16))
rendered_credits_button_text = credits_button_text

# Set up quit button
quit_button_text = button_font.render("QUIT", True, (180, 150, 100))
quit_button_rect = quit_button_text.get_rect(center=(4*width // 5, height // 16))
rendered_quit_button_text = quit_button_text

# Set up back button
back_text = button_font.render("BACK", True, (220, 220, 160))
back_rect = quit_button_text.get_rect(center=(width // 2, height -60))

# Start playing background music
pygame.mixer.music.play(-1, 0, 4000)

# Title screen
def main_menu():
    # Set the initial frame index and FPS
    # LOW FRAME RATE SOMETIMES CAUSES BUTTON GLITCHES (TWO HIGHLIGHTED AT ONCE)
    frame_index = 0
    FPS = 12

    # Set up hover sound flag
    hover_sound_played = False

    # Set up game loop
    clock = pygame.time.Clock()
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    running = False
                if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    menu_selection()

        # Draw screen
        screen.fill((0, 0, 0))

        # Get the current frame
        frame = frames[frame_index]

        # Draw background animation
        screen.blit(frame, (0, 0))
        screen.blit(border, border_rect)

        # Update the frame index
        frame_index = (frame_index + 1) % len(frames)

        # Render red quit button text and play the hover sound
        if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
            rendered_quit_button_text = button_font.render("QUIT", True, (255, 0, 0))
            if not hover_sound_played:
                button_hover_sound.play()
                hover_sound_played = True
        # Render red play button text and play the hover sound
        elif play_button_rect.collidepoint(pygame.mouse.get_pos()):
            rendered_play_button_text = button_font.render("PLAY", True, (255, 0, 0))
            if not hover_sound_played:
                button_hover_sound.play()
                hover_sound_played = True
        # Render red credits button text and play the hover sound
        elif credits_button_rect.collidepoint(pygame.mouse.get_pos()):
            rendered_credits_button_text = button_font.render("CREDITS", True, (255, 0, 0))
            if not hover_sound_played:
                button_hover_sound.play()
                hover_sound_played = True  
        # Return to the base color of the buttons and stop playing the hover sound
        else:
            rendered_quit_button_text = quit_button_text
            rendered_play_button_text = play_button_text
            rendered_credits_button_text = credits_button_text
            hover_sound_played = False

        # Draw game title
        screen.blit(game_title_text, game_title_rect)
        # Draw buttons
        screen.blit(rendered_play_button_text, play_button_rect)
        screen.blit(rendered_credits_button_text, credits_button_rect)
        screen.blit(rendered_quit_button_text, quit_button_rect)

        # Update display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(FPS)

    # Stop the background music when the game is finished
    pygame.mixer.music.stop()

    # Quit the game
    pygame.quit()

# Menu Selection Screen
def menu_selection():
    while True:

        scaled_BG = pygame.transform.scale(BG, screen.get_size())
        screen.blit(scaled_BG, (0, 0))

        menu_text = select_title_font.render("Choose your faction:", True, (220, 220, 160))
        menu_rect = menu_text.get_rect(center=(width // 2, height // 6))
        screen.blit(menu_text, menu_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(pygame.mouse.get_pos()):
                    main_menu()
                if faction1_rect.collidepoint(pygame.mouse.get_pos()):
                    char_select(1)
                if faction2_rect.collidepoint(pygame.mouse.get_pos()):
                    char_select(2)

        faction1_text = select_button_font.render("* Faction 1", True, (220, 220, 160))
        faction1_rect = quit_button_text.get_rect(center=(width // 2.1, height // 2.25))

        faction2_text = select_button_font.render("* Faction 2", True, (220, 220, 160))
        faction2_rect = quit_button_text.get_rect(center=(width // 2.1, height // 1.75))

        # Draw faction 1 button
        if faction1_rect.collidepoint(pygame.mouse.get_pos()):
            faction1_text = select_button_font.render("* Faction 1", True, (255, 0, 0))
        else:
             faction1_text = select_button_font.render("* Faction 1", True, (220, 220, 160))
        screen.blit(faction1_text, faction1_rect)

        # Draw faction 2 button
        if faction2_rect.collidepoint(pygame.mouse.get_pos()):
            faction2_text = select_button_font.render("* Faction 2", True, (255, 0, 0))
        else:
             faction2_text = select_button_font.render("* Faction 2", True, (220, 220, 160))
        screen.blit(faction2_text, faction2_rect)

        # Draw back button
        if back_rect.collidepoint(pygame.mouse.get_pos()):
            back_text = button_font.render("BACK", True, (255, 0, 0))
        else:
             back_text = button_font.render("BACK", True, (220, 220, 160))
        screen.blit(back_text, back_rect)

        pygame.display.flip()

# Character Selection Screen
def char_select(set_n):
    while True:

        scaled_BG = pygame.transform.scale(BG, screen.get_size())
        screen.blit(scaled_BG, (0, 0))

        back2_text = select_button_font.render("CHANGE FACTION", True, (220, 220, 160))
        back2_rect = back2_text.get_rect(center=(width // 2.75, height -60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back2_rect.collidepoint(pygame.mouse.get_pos()):
                    menu_selection()

        character_text = select_title_font.render("Choose 3 characters:", True, (220, 220, 160))
        character_rect = character_text.get_rect(center=(width // 2, height // 6))
        screen.blit(character_text, character_rect)

        # Draw back button
        if back2_rect.collidepoint(pygame.mouse.get_pos()):
            back2_text = select_button_font.render("CHANGE FACTION", True, (255, 0, 0))
        else:
             back2_text = select_button_font.render("CHANGE FACTION", True, (220, 220, 160))
        screen.blit(back2_text, back2_rect)

        pygame.display.flip()

        """
        if set_n == 1:

        else:
        """
main_menu()