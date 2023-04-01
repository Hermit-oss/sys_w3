import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Era of Conflict")

# Load assets
game_title_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 140)
button_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 90)
button_hover_sound = pygame.mixer.Sound(os.path.join("assets", "snd", "hover.wav"))
border = pygame.image.load('assets/img/border.png').convert_alpha()

# Set up game title
game_title_text = game_title_font.render("Era of Conflict", True, (180, 150, 100))
game_title_rect = game_title_text.get_rect(center=(width // 2, height // 1.05))

border_rect = border.get_rect(center=(width // 2, height // 7))

# Set up quit button
quit_button_text = button_font.render("QUIT", True, (180, 150, 100))
quit_button_rect = quit_button_text.get_rect(center=(2*width // 3, height // 16))
tilted_quit_button_text = pygame.transform.rotate(quit_button_text, 0)

# Set up play button
play_button_text = button_font.render("PLAY", True, (180, 150, 100))
play_button_rect = play_button_text.get_rect(center=(width // 3, height // 16))
tilted_play_button_text = pygame.transform.rotate(play_button_text, 0)

# Load background frames
frames = []
for i in range(1, 120):
    filename = os.path.join('assets/img/background', f'frame{i}.png')
    frame = pygame.image.load(filename).convert_alpha()
    frames.append(frame)

# Set the initial frame index and FPS
frame_index = 0
FPS = 12

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
            # If quit button is pressed
            if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                running = False

    # Draw screen
    screen.fill((0, 0, 0))

    # Get the current frame
    frame = frames[frame_index]

    # Stretch and draw image
    scaled_frame = pygame.transform.scale(frames[frame_index], screen.get_size())
    screen.blit(scaled_frame, (0, 0))
    screen.blit(border, border_rect)

    # Update the frame index
    frame_index = (frame_index + 1) % len(frames)

    # Draw tilted quit button text
    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
        tilted_quit_button_text = pygame.transform.rotate(button_font.render("QUIT", True, (255, 0, 0)), 0)
        if not hover_sound_played:
            button_hover_sound.play()
            hover_sound_played = True
    # Draw tilted play button text
    elif play_button_rect.collidepoint(pygame.mouse.get_pos()):
        tilted_play_button_text = pygame.transform.rotate(button_font.render("PLAY", True, (255, 0, 0)), 0)
        if not hover_sound_played:
            button_hover_sound.play()
            hover_sound_played = True
    # Return to the base color of the buttons
    else:
        tilted_quit_button_text = quit_button_text
        tilted_play_button_text = play_button_text
        hover_sound_played = False

    # Draw game title
    screen.blit(game_title_text, game_title_rect)
    # Draw buttons
    screen.blit(tilted_quit_button_text, quit_button_rect)
    screen.blit(tilted_play_button_text, play_button_rect)

    # Update display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Stop the background music when the game is finished
pygame.mixer.music.stop()

# Quit the game
pygame.quit()
