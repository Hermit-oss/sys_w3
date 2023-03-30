import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Era of Conflict")

# Load assets
game_title_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 120)
button_font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 70)
button_hover_sound = pygame.mixer.Sound(os.path.join("assets", "snd", "hover.wav"))

# Set up game title
game_title_text = game_title_font.render("Era of Conflict", True, (220, 220, 160))
game_title_rect = game_title_text.get_rect(center=(width // 2, height - 60))

# Set up quit button
button_text = button_font.render("QUIT", True, (220, 220, 160))
button_rect = button_text.get_rect(center=(width // 7, height // 8))
tilted_button_text = pygame.transform.rotate(button_text, 13)

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

    # Update display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Stop the background music when the game is finished
pygame.mixer.music.stop()

# Quit the game
pygame.quit()
