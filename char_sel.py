<<<<<<< HEAD
import pygame
import os
import sys
from character import Character

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Era of Conflict")

# Load assets
game_title_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 120)
button_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 70)
select_title_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 100)
select_button_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 50)
ch_info_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 20)
button_hover_sound = pygame.mixer.Sound(os.path.join("assets", "snd", "hover.wav"))
BG = pygame.image.load(os.path.join("assets", "img", "bgwood.jpg"))
sprite = pygame.image.load(os.path.join("assets", "img", "tmp_char.png"))
sprite_rect = sprite.get_rect()
info_pic = pygame.image.load(os.path.join("assets", "img", "metal.png"))
# Set up game title
game_title_text = game_title_font.render("Era of Conflict", True, (220, 220, 160))
game_title_rect = game_title_text.get_rect(center=(width // 2, height - 60))

# Set up quit button
button_text = button_font.render("QUIT", True, (220, 220, 160))
button_rect = button_text.get_rect(center=(width // 7, height // 8))
tilted_button_text = pygame.transform.rotate(button_text, 13)

# Set up play button
PLAY_BUTTON = button_font.render("PLAY", True, (220, 220, 160))
pbutton_rect = PLAY_BUTTON.get_rect(center=(width -200, height //8 ))

back_text = button_font.render("BACK", True, (220, 220, 160))
back_rect = button_text.get_rect(center=(width // 2, height -60))

#Name1 = Character(faction=1,name="Name1",classc="Warrior",hp=30, attack=50, defense=40, speed=20)
#Name2 = Character(faction=1,name="Name2",classc="Sorcerer",hp=35, attack=40, defense=30, speed=30)
#Name3 = Character(faction=1,name="Name3",classc="Assassin",hp=25, attack=40, defense=20, speed=40)

def main_menu():
    # Load background frames
    frames = []
    for i in range(1, 53):
        filename = os.path.join('assets/img/background', f'frame{i}.png')
        frame = pygame.image.load(filename).convert_alpha()
        frames.append(frame)

    # Set the initial frame index and FPS
    frame_index = 0
    FPS = 13

    # Set up hover sound flag
    hover_sound_played = False

    # Load background music
    pygame.mixer.music.load("assets/snd/intro.wav")

    # Start playing background music
    pygame.mixer.music.play(-1)

    # Set up game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    running = False
                if pbutton_rect.collidepoint(pygame.mouse.get_pos()):
                    menu_selection()

        # Draw screen
        screen.fill((0, 0, 0))

        # Get the current frame
        frame = frames[frame_index]

        # Stretch and draw image
        scaled_frame = pygame.transform.scale(frames[frame_index], screen.get_size())
        screen.blit(scaled_frame, (0, 0))

        # Update the frame index
        frame_index = (frame_index + 1) % len(frames)

        # Draw game title
        screen.blit(game_title_text, game_title_rect)

        # Draw tilted button text
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            tilted_button_text = pygame.transform.rotate(button_font.render("QUIT", True, (255, 0, 0)), 13)
            if not hover_sound_played:
                button_hover_sound.play()
                hover_sound_played = True
        else:
            tilted_button_text = pygame.transform.rotate(button_font.render("QUIT", True, (220, 220, 160)), 13)
            hover_sound_played = False
        screen.blit(tilted_button_text, button_rect)

            # Draw play button text
        if pbutton_rect.collidepoint(pygame.mouse.get_pos()):
            PLAY_BUTTON = button_font.render("PLAY", True, (255, 0, 0))
            if not hover_sound_played:
                button_hover_sound.play()
                hover_sound_played = True
        else:
             PLAY_BUTTON = button_font.render("PLAY", True, (220, 220, 160))
        screen.blit(PLAY_BUTTON, pbutton_rect)

        # Update display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(FPS)


    # Stop the background music when the game is finished
    pygame.mixer.music.stop()

    # Quit the game
    pygame.quit()

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
        faction1_rect = button_text.get_rect(center=(width // 2.1, height // 2.25))

        faction2_text = select_button_font.render("* Faction 2", True, (220, 220, 160))
        faction2_rect = button_text.get_rect(center=(width // 2.1, height // 1.75))

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
                if sprite_rect.collidepoint(pygame.mouse.get_pos()):
                    info_window()

        character_text = select_title_font.render("Choose 3 characters:", True, (220, 220, 160))
        character_rect = character_text.get_rect(center=(width // 2, height // 6))
        screen.blit(character_text, character_rect)

        scaled_sprite = pygame.transform.scale(sprite, (100, 100))
        screen.blit(scaled_sprite, (260, 200))
        pname = ch_info_font.render("NameEX", True, (255, 0, 0))
        pname_rect = pname.get_rect(center=(width // 5, height // 2.75))
        screen.blit(pname, pname_rect)
        cname = ch_info_font.render("Class", True, (255, 0, 0))
        cname_rect = cname.get_rect(center=(width // 5, height // 2.5))
        screen.blit(cname, cname_rect)

        # Draw back button
        if back2_rect.collidepoint(pygame.mouse.get_pos()):
            back2_text = select_button_font.render("CHANGE FACTION", True, (255, 0, 0))
        else:
             back2_text = select_button_font.render("CHANGE FACTION", True, (220, 220, 160))
        screen.blit(back2_text, back2_rect)

    
        #if set_n == 1:
          #  for person in Character:
        # else:

        pygame.display.flip()

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

        scaled_sprite = pygame.transform.scale(sprite, (200, 200))
        screen.blit(scaled_sprite, (550, 200))
        pname = ch_info_font.render("NameEX", True, (255, 0, 0))
        pname_rect = pname.get_rect(center=(width // 1.75, height // 2.75))
        screen.blit(pname, pname_rect)
        cname = ch_info_font.render("Class", True, (255, 0, 0))
        cname_rect = cname.get_rect(center=(width // 1.75, height // 2.5))
        screen.blit(cname, cname_rect)

        # Draw back button
        if X_rect.collidepoint(pygame.mouse.get_pos()):
             X = select_button_font.render("X", True, (255, 0, 0))
        else:
             X = select_button_font.render("X", True, (230, 0, 0))
        screen.blit(X, X_rect)

        pygame.display.flip()

=======
import pygame
import os
import sys
from character import Character

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Era of Conflict")

# Load assets
game_title_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 120)
button_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 70)
select_title_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 100)
select_button_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 50)
ch_info_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 20)
button_hover_sound = pygame.mixer.Sound(os.path.join("assets", "snd", "hover.wav"))
BG = pygame.image.load(os.path.join("assets", "img", "bgwood.jpg"))
sprite = pygame.image.load(os.path.join("assets", "img", "tmp_char.png"))
sprite_rect = sprite.get_rect()
info_pic = pygame.image.load(os.path.join("assets", "img", "metal.png"))
# Set up game title
game_title_text = game_title_font.render("Era of Conflict", True, (220, 220, 160))
game_title_rect = game_title_text.get_rect(center=(width // 2, height - 60))

# Set up quit button
button_text = button_font.render("QUIT", True, (220, 220, 160))
button_rect = button_text.get_rect(center=(width // 7, height // 8))
tilted_button_text = pygame.transform.rotate(button_text, 13)

# Set up play button
PLAY_BUTTON = button_font.render("PLAY", True, (220, 220, 160))
pbutton_rect = PLAY_BUTTON.get_rect(center=(width -200, height //8 ))

back_text = button_font.render("BACK", True, (220, 220, 160))
back_rect = button_text.get_rect(center=(width // 2, height -60))

#Name1 = Character(faction=1,name="Name1",classc="Warrior",hp=30, attack=50, defense=40, speed=20)
#Name2 = Character(faction=1,name="Name2",classc="Sorcerer",hp=35, attack=40, defense=30, speed=30)
#Name3 = Character(faction=1,name="Name3",classc="Assassin",hp=25, attack=40, defense=20, speed=40)

def main_menu():
    # Load background frames
    frames = []
    for i in range(1, 53):
        filename = os.path.join('assets/img/background', f'frame{i}.png')
        frame = pygame.image.load(filename).convert_alpha()
        frames.append(frame)

    # Set the initial frame index and FPS
    frame_index = 0
    FPS = 13

    # Set up hover sound flag
    hover_sound_played = False

    # Load background music
    pygame.mixer.music.load("assets/snd/intro.wav")

    # Start playing background music
    pygame.mixer.music.play(-1)

    # Set up game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    running = False
                if pbutton_rect.collidepoint(pygame.mouse.get_pos()):
                    menu_selection()

        # Draw screen
        screen.fill((0, 0, 0))

        # Get the current frame
        frame = frames[frame_index]

        # Stretch and draw image
        scaled_frame = pygame.transform.scale(frames[frame_index], screen.get_size())
        screen.blit(scaled_frame, (0, 0))

        # Update the frame index
        frame_index = (frame_index + 1) % len(frames)

        # Draw game title
        screen.blit(game_title_text, game_title_rect)

        # Draw tilted button text
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            tilted_button_text = pygame.transform.rotate(button_font.render("QUIT", True, (255, 0, 0)), 13)
            if not hover_sound_played:
                button_hover_sound.play()
                hover_sound_played = True
        else:
            tilted_button_text = pygame.transform.rotate(button_font.render("QUIT", True, (220, 220, 160)), 13)
            hover_sound_played = False
        screen.blit(tilted_button_text, button_rect)

            # Draw play button text
        if pbutton_rect.collidepoint(pygame.mouse.get_pos()):
            PLAY_BUTTON = button_font.render("PLAY", True, (255, 0, 0))
            if not hover_sound_played:
                button_hover_sound.play()
                hover_sound_played = True
        else:
             PLAY_BUTTON = button_font.render("PLAY", True, (220, 220, 160))
        screen.blit(PLAY_BUTTON, pbutton_rect)

        # Update display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(FPS)


    # Stop the background music when the game is finished
    pygame.mixer.music.stop()

    # Quit the game
    pygame.quit()

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
        faction1_rect = button_text.get_rect(center=(width // 2.1, height // 2.25))

        faction2_text = select_button_font.render("* Faction 2", True, (220, 220, 160))
        faction2_rect = button_text.get_rect(center=(width // 2.1, height // 1.75))

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
                if sprite_rect.collidepoint(pygame.mouse.get_pos()):
                    info_window()

        character_text = select_title_font.render("Choose 3 characters:", True, (220, 220, 160))
        character_rect = character_text.get_rect(center=(width // 2, height // 6))
        screen.blit(character_text, character_rect)

        scaled_sprite = pygame.transform.scale(sprite, (100, 100))
        screen.blit(scaled_sprite, (260, 200))
        pname = ch_info_font.render("NameEX", True, (255, 0, 0))
        pname_rect = pname.get_rect(center=(width // 5, height // 2.75))
        screen.blit(pname, pname_rect)
        cname = ch_info_font.render("Class", True, (255, 0, 0))
        cname_rect = cname.get_rect(center=(width // 5, height // 2.5))
        screen.blit(cname, cname_rect)

        # Draw back button
        if back2_rect.collidepoint(pygame.mouse.get_pos()):
            back2_text = select_button_font.render("CHANGE FACTION", True, (255, 0, 0))
        else:
             back2_text = select_button_font.render("CHANGE FACTION", True, (220, 220, 160))
        screen.blit(back2_text, back2_rect)

    
        #if set_n == 1:
          #  for person in Character:
        # else:

        pygame.display.flip()

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

        scaled_sprite = pygame.transform.scale(sprite, (200, 200))
        screen.blit(scaled_sprite, (550, 200))
        pname = ch_info_font.render("NameEX", True, (255, 0, 0))
        pname_rect = pname.get_rect(center=(width // 1.75, height // 2.75))
        screen.blit(pname, pname_rect)
        cname = ch_info_font.render("Class", True, (255, 0, 0))
        cname_rect = cname.get_rect(center=(width // 1.75, height // 2.5))
        screen.blit(cname, cname_rect)

        # Draw back button
        if X_rect.collidepoint(pygame.mouse.get_pos()):
             X = select_button_font.render("X", True, (255, 0, 0))
        else:
             X = select_button_font.render("X", True, (230, 0, 0))
        screen.blit(X, X_rect)

        pygame.display.flip()

>>>>>>> 71ad80bc10d6a79d69bff9761a029d20a65388eb
main_menu()