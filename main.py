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
#ch_info_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 30)
# Sounds
button_hover_sound = pygame.mixer.Sound(os.path.join("assets", "snd", "hover.wav"))
title_screen_intro = pygame.mixer.music.load("assets/snd/intro.wav")
# Graphics
border = pygame.transform.scale(pygame.image.load('assets/img/border.png').convert_alpha(), (width, 80))
BG = pygame.image.load(os.path.join("assets", "img", "bgwood.jpg"))
sprite = pygame.image.load(os.path.join("assets", "img", "tmp_char.png"))
info_pic = pygame.image.load(os.path.join("assets", "img", "metal.png"))
frames = []
for i in range(1, 120):
    filename = os.path.join('assets/img/background', f'frame{i}.png')
    frame = pygame.transform.scale(pygame.image.load(filename).convert_alpha(), screen.get_size())
    frames.append(frame)

# Set up game title
game_title_text = game_title_font.render("Era of Conflict", True, (180, 150, 100))
game_title_rect = game_title_text.get_rect(center=(width // 2, height // 1.08))

# Set up main menu border rectangle
border_rect = border.get_rect(center=(width // 2, height // 6.5))

# Set up play button
play_button_text = button_font.render("PLAY", True, (180, 150, 100))
play_button_rect = play_button_text.get_rect(center=(width // 5, height // 14))
rendered_play_button_text = play_button_text

# Set up credits button
credits_button_text = button_font.render("CREDITS", True, (180, 150, 100))
credits_button_rect = credits_button_text.get_rect(center=(width // 2, height // 14))
rendered_credits_button_text = credits_button_text

# Set up quit button
quit_button_text = button_font.render("QUIT", True, (180, 150, 100))
quit_button_rect = quit_button_text.get_rect(center=(4*width // 5, height // 14))
rendered_quit_button_text = quit_button_text

# Set up back button
back_text = button_font.render("BACK", True, (220, 220, 160))
back_rect = quit_button_text.get_rect(center=(width // 2, height -60))
back_text_hovered = back_text

# Start playing background music
pygame.mixer.music.play(-1, 0, 4000)


# Set up hover sound flag
hover_sound_played = False

# Title screen
def main_menu():
    # Set the initial frame index and FPS
    # LOW FRAME RATE SOMETIMES CAUSES BUTTON GLITCHES (TWO HIGHLIGHTED AT ONCE)
    frame_index = 0
    FPS = 12

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
        faction1_text_hovered = faction1_text

        faction2_text = select_button_font.render("* Faction 2", True, (220, 220, 160))
        faction2_rect = quit_button_text.get_rect(center=(width // 2.1, height // 1.75))
        faction2_text_hovered = faction2_text

        # Draw faction 1 button
        if faction1_rect.collidepoint(pygame.mouse.get_pos()):
            faction1_text_hovered = select_button_font.render("* Faction 1", True, (255, 0, 0))
        # Draw faction 2 button
        elif faction2_rect.collidepoint(pygame.mouse.get_pos()):
            faction2_text_hovered = select_button_font.render("* Faction 2", True, (255, 0, 0))
        # Draw back button
        elif back_rect.collidepoint(pygame.mouse.get_pos()):
            back_text_hovered = button_font.render("BACK", True, (255, 0, 0))
        else:
            faction1_text_hovered = faction1_text
            faction2_text_hovered = faction2_text
            back_text_hovered = back_text
            # hover_sound_played = False

        screen.blit(faction1_text_hovered, faction1_rect)
        screen.blit(faction2_text_hovered, faction2_rect)
        screen.blit(back_text_hovered, back_rect)

        pygame.display.flip()

# Character Selection Screen
def char_select(set_n):
    while True:

        scaled_BG = pygame.transform.scale(BG, screen.get_size())
        screen.blit(scaled_BG, (0, 0))
        sprite_rect = sprite.get_rect()

        back2_text = select_button_font.render("CHANGE FACTION", True, (220, 220, 160))
        back2_rect = back2_text.get_rect(center=(width // 2.75, height -60))
        back2_text_hovered = back2_text

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back2_rect.collidepoint(pygame.mouse.get_pos()):
                    menu_selection()
                if ch_box.collidepoint(pygame.mouse.get_pos()):
                    info_window()

        character_text = select_title_font.render("Choose 3 characters:", True, (220, 220, 160))
        character_rect = character_text.get_rect(center=(width // 2, height // 6))
        screen.blit(character_text, character_rect)

        scaled_sprite = pygame.transform.scale(sprite, (100, 100))
        screen.blit(scaled_sprite, (width // 6, height // 2.6))
        pname = ch_info_font.render("NameEX", True, (220, 220, 160))
        pname_rect = pname.get_rect(center=(width // 5, height // 1.9))

        cname = ch_info_font.render("Class", True, (220, 220, 160))
        cname_rect = cname.get_rect(center=(width // 5, height // 1.75))

        ch_box = pygame.draw.rect(screen, (220, 220, 160), (width // 6.6,height // 2.7,150,200),2)
        ch_box_hovered = ch_box

        select_character = ch_info_font.render("Select", True, (220, 220, 160))
        select_character_rect = pname.get_rect(center=(width // 4.7, height // 1.55))

        screen.blit(pname, pname_rect)
        screen.blit(cname, cname_rect)
        screen.blit(select_character, select_character_rect)

        # Draw back button
        if back2_rect.collidepoint(pygame.mouse.get_pos()):
            back2_text_hovered = select_button_font.render("CHANGE FACTION", True, (255, 0, 0))
        elif ch_box.collidepoint(pygame.mouse.get_pos()):
            ch_box_hovered = pygame.draw.rect(screen, (255, 0, 0), (width // 6.6,height // 2.7,150,200),2)
        else:
            back2_text_hovered = back2_text
            ch_box_hovered = ch_box

        screen.blit(back2_text_hovered, back2_rect)

        pygame.display.flip()

        """
        for instance in Character.instances:
	        if instance.faction == set_n :
        """  

def info_window():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if X_rect.collidepoint(pygame.mouse.get_pos()):
                    scaled_BG = pygame.transform.scale(BG, screen.get_size())
                    screen.blit(scaled_BG, (0, 0))
                    return

        scaled_box = pygame.transform.scale(info_pic, (700, 825))
        screen.blit(scaled_box, (425, 25))

        X = select_button_font.render("X", True, (230, 0, 0))
        X_rect = X.get_rect(center=(width // 1.4, height // 10))   
        X_hovered = X       

        scaled_sprite = pygame.transform.scale(sprite, (200, 200))
        screen.blit(scaled_sprite, (width // 2.75,  height // 8))
        pname = ch_info_font.render("NameEX", True, (65, 32, 96))
        pname_rect = pname.get_rect(center=(width // 1.85, height // 6))
        screen.blit(pname, pname_rect)
        cname = ch_info_font.render("Class", True, (65, 32, 96))
        cname_rect = cname.get_rect(center=(width // 1.9, height // 4.75))
        screen.blit(cname, cname_rect)

        # Draw back button
        if X_rect.collidepoint(pygame.mouse.get_pos()):
             X_hovered = select_button_font.render("X", True, (255, 77, 77))
        else:
             X_hovered = X
        screen.blit(X_hovered, X_rect)

        pygame.display.flip()

main_menu()