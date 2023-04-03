import pygame
import sys
import os
from button import Button

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = SCREEN.get_size()

# Main menu background animation
MENU_FRAMES = []
for i in range(1, 120):
    filename = os.path.join('assets/img/background', f'frame{i}.png')
    frame = pygame.transform.scale(pygame.image.load(filename).convert_alpha(), SCREEN.get_size())
    MENU_FRAMES.append(frame)

# Colors
MENU_BASE_COLOR = (180, 150, 100)

# Sounds
BUTTON_HOVER_SOUND = pygame.mixer.Sound(os.path.join("assets", "snd", "hover.wav"))
TITLE_SCREEN_INTRO = pygame.mixer.music.load("assets/snd/intro.wav")
# Start playing background music
pygame.mixer.music.play(-1, 0, 4000)
pygame.mixer.music.set_volume(0.5)
# Set up hover sound flag
hover_sound_played = False

def getFont(size): # Returns Bitmgothic in the specified size
    font_path = "assets/font/Bitmgothic.ttf"
    return pygame.font.Font(font_path, size)

def main_menu(): # Main menu method
    # Set the window caption
    pygame.display.set_caption("Era of Conflict")

    # Set the initial frame index and FPS
    # LOW FRAME RATE SOMETIMES CAUSES BUTTON GLITCHES (SLOW COLOR CHANGE)
    frame_index = 0
    FPS = 24

    # Set up game loop
    clock = pygame.time.Clock()

    while True:
        # Get main menu mouse position
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Draw the screen
        SCREEN.fill((0, 0, 0))

        # Get the current frame, update the index, blit the current frame
        frame = MENU_FRAMES[frame_index]
        frame_index = (frame_index + 1) % len(MENU_FRAMES)
        SCREEN.blit(frame, (0, 0))

        # Set up main menu border
        MENU_BORDER = pygame.transform.scale(pygame.image.load('assets/img/border.png').convert_alpha(), (WIDTH, 80))
        MENU_BORDER_RECT = MENU_BORDER.get_rect(center=(WIDTH // 2, HEIGHT // 7))
        SCREEN.blit(MENU_BORDER, MENU_BORDER_RECT)

        # Set up main menu text
        MENU_TEXT = getFont(140).render("Era of Conflict", True, MENU_BASE_COLOR)
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 1.06))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Set up main menu PLAY button
        MENU_PLAY = Button(image=None, pos=(WIDTH // 5, HEIGHT // 16),
                            text_input="PLAY", font=getFont(90), base_color=MENU_BASE_COLOR, hovering_color="red")

        # Set up main menu CREDITS button
        MENU_CREDITS = Button(image=None, pos=(WIDTH // 2, HEIGHT // 16),
                            text_input="CREDITS", font=getFont(90), base_color=MENU_BASE_COLOR, hovering_color="red")

        # Set up main menu QUIT button
        MENU_QUIT = Button(image=None, pos=(4*WIDTH // 5, HEIGHT // 16),
                            text_input="QUIT", font=getFont(90), base_color=MENU_BASE_COLOR, hovering_color="red")

        # Set state and blit the buttons, play the hovering sound
        for button in [MENU_PLAY, MENU_CREDITS, MENU_QUIT]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_QUIT.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if MENU_PLAY.checkForInput(MENU_MOUSE_POS):
                    menu_selection()
                if MENU_CREDITS.checkForInput(MENU_MOUSE_POS):
                    menu_credits()

        # Limit the frame rate
        clock.tick(FPS)

        # Update display
        pygame.display.update()

def menu_credits():
    # Set the window caption
    pygame.display.set_caption("Credits")
    while True:
        # Get credits mouse position
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        # Draw the screen
        SCREEN.fill((0, 0, 0))

        # Set up credits background
        CREDITS_BG = pygame.transform.scale(pygame.image.load("assets/img/bgwood.jpg"), SCREEN.get_size())
        SCREEN.blit(CREDITS_BG, (0, 0))

        # Set up credits text
        CREDITS_TEXT = getFont(140).render("We're thankful to", True, MENU_BASE_COLOR)
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 6))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)

        # Set up credits text
        CREDITS_TEXT1 = getFont(100).render("Creators: JJEntertainment", True, MENU_BASE_COLOR)
        CREDITS_RECT1 = CREDITS_TEXT1.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        SCREEN.blit(CREDITS_TEXT1, CREDITS_RECT1)

        # Set up credits text
        CREDITS_TEXT2 = getFont(100).render("BG Anima: Camille Unknown", True, MENU_BASE_COLOR)
        CREDITS_RECT2 = CREDITS_TEXT2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)

        # Set up credits text
        CREDITS_TEXT3 = getFont(100).render("BG Music: TBD...", True, MENU_BASE_COLOR)
        CREDITS_RECT3 = CREDITS_TEXT3.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
        SCREEN.blit(CREDITS_TEXT3, CREDITS_RECT3)

        # Set up credits BACK button
        CREDITS_BACK = Button(image=None, pos=(WIDTH // 4, HEIGHT // 1.06),
                            text_input="BACK", font=getFont(90), base_color=MENU_BASE_COLOR, hovering_color="red")
        CREDITS_BACK.changeColor(CREDITS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def menu_selection(): # Menu selection method
    # Set the window caption
    pygame.display.set_caption("Menu Selection")

    while True:
        # Get menu selection mouse position
        MENU_SELECTION_MOUSE_POS = pygame.mouse.get_pos()

        # Draw the screen
        SCREEN.fill((0, 0, 0))

        # Set up menu selection background
        MENU_SELECTION_BG = pygame.transform.scale(pygame.image.load("assets/img/bgwood.jpg"), SCREEN.get_size())
        SCREEN.blit(MENU_SELECTION_BG, (0, 0))

        # Set up menu selection text
        MENU_SELECTION_TEXT = getFont(140).render("Pledge your allegiance", True, MENU_BASE_COLOR)
        MENU_SELECTION_RECT = MENU_SELECTION_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 6))
        SCREEN.blit(MENU_SELECTION_TEXT, MENU_SELECTION_RECT)

        # Set up menu selection FACTION1 button
        MENU_SELECTION_FACTION1 = Button(image=None, pos=(WIDTH // 2, HEIGHT // 2.25),
                            text_input="The Crimson Legion", font=getFont(90), base_color=MENU_BASE_COLOR, hovering_color="red")
        MENU_SELECTION_FACTION1.changeColor(MENU_SELECTION_MOUSE_POS)
        MENU_SELECTION_FACTION1.update(SCREEN)

        # Set up menu selection FACTION2 button
        MENU_SELECTION_FACTION2 = Button(image=None, pos=(WIDTH // 2, HEIGHT // 1.75),
                            text_input="The Mystic Conclave", font=getFont(90), base_color=MENU_BASE_COLOR, hovering_color="red")
        MENU_SELECTION_FACTION2.changeColor(MENU_SELECTION_MOUSE_POS)
        MENU_SELECTION_FACTION2.update(SCREEN)

        # Set up menu selection BACK button
        MENU_SELECTION_BACK = Button(image=None, pos=(WIDTH // 4, HEIGHT // 1.06),
                            text_input="BACK", font=getFont(90), base_color=MENU_BASE_COLOR, hovering_color="red")

        # Set state and blit the buttons, play the hovering sound
        for button in [MENU_SELECTION_FACTION1, MENU_SELECTION_FACTION2, MENU_SELECTION_BACK]:
            button.changeColor(MENU_SELECTION_MOUSE_POS)
            button.update(SCREEN)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_SELECTION_BACK.checkForInput(MENU_SELECTION_MOUSE_POS):
                    main_menu()
                if MENU_SELECTION_FACTION1.checkForInput(MENU_SELECTION_MOUSE_POS):
                    char_select(1)
                if MENU_SELECTION_FACTION2.checkForInput(MENU_SELECTION_MOUSE_POS):
                    char_select(2)

        pygame.display.update()

def char_select(set_n): # Character selection method
    # Set the window caption
    pygame.display.set_caption("Character Selection")

    while True:
        # Get character selection mouse position
        CHARACTER_SELECTION_MOUSE_POS = pygame.mouse.get_pos()

        # Draw the screen
        SCREEN.fill((0, 0, 0))

        # Set up character selection background
        CHARACTER_SELECTION_BG = pygame.transform.scale(pygame.image.load("assets/img/bgwood.jpg"), SCREEN.get_size())
        SCREEN.blit(CHARACTER_SELECTION_BG, (0, 0))

        # Set up character selection text
        CHARACTER_TEXT = getFont(140).render("Pick three companions", True, MENU_BASE_COLOR)
        CHARACTER_RECT = CHARACTER_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 6))
        SCREEN.blit(CHARACTER_TEXT, CHARACTER_RECT)

        CHARACTER_SPRITE = pygame.transform.scale(pygame.image.load("assets/img/tmp_char.png"), (100, 100))
        CHARACTER_SPRITE_RECT = CHARACTER_SPRITE.get_rect(center=(WIDTH // 6, HEIGHT // 2.6))
        SCREEN.blit(CHARACTER_SPRITE, CHARACTER_SPRITE_RECT)

        # Set up character selection BACK button
        CHARACTER_SELECTION_BACK = Button(image=None, pos=(WIDTH // 4, HEIGHT // 1.06),
                            text_input="BACK", font=getFont(90), base_color=MENU_BASE_COLOR, hovering_color="red")
        CHARACTER_SELECTION_BACK.changeColor(CHARACTER_SELECTION_MOUSE_POS)
        CHARACTER_SELECTION_BACK.update(SCREEN)

        PNAME = getFont(30).render("NameEX", True, MENU_BASE_COLOR)
        PNAME_RECT = PNAME.get_rect(center=(WIDTH // 5, HEIGHT // 1.9))
        SCREEN.blit(PNAME, PNAME_RECT)

        CNAME = getFont(30).render("Class", True, MENU_BASE_COLOR)
        CNAME_RECT = CNAME.get_rect(center=(WIDTH // 5, HEIGHT // 1.75))
        SCREEN.blit(CNAME, CNAME_RECT)

        SELECT_CHARACTER = getFont(30).render("Select", True, MENU_BASE_COLOR)
        SELECT_CHARACTER_RECT = PNAME.get_rect(center=(WIDTH // 4.7, HEIGHT // 1.55))
        SCREEN.blit(SELECT_CHARACTER, SELECT_CHARACTER_RECT)

        CH_BOX = pygame.draw.rect(SCREEN, MENU_BASE_COLOR, (WIDTH // 6.6, HEIGHT // 2.7, 150, 200), 2)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHARACTER_SELECTION_BACK.checkForInput(CHARACTER_SELECTION_MOUSE_POS):
                    menu_selection()

        pygame.display.update()

main_menu()