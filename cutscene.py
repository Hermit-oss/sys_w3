import pygame
import json

def getFont(size): # Returns Bitmgothic in the specified size
    font_path = "assets/font/Bitmgothic.ttf"
    return pygame.font.Font(font_path, size)

def draw_text(screen, text, size, color, x, y):
    font = getFont(size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

class Cutscene():
    def __init__(self, screen):
        self.cutscenes_complete = []
        self.cutscene = None
        self.cutscene_running = False

        # Drawing variables
        self.screen = screen
        self.window_size = 0

    def start_cutscene(self, cutscene):
        if cutscene.name not in self.cutscenes_complete:
            self.cutscenes_complete.append(cutscene.name)
            self.cutscene = cutscene
            self.cutscene_running = True

    def end_cutscene(self):
        self.cutscene = None
        self.cutscene_running = False

    def update(self):
        if self.cutscene_running:
            self.cutscene_running = self.cutscene.update()
        else:
            self.end_cutscene()

    def draw(self):
        if self.cutscene_running:
            # Draw rect generic to all cut scenes
            pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.screen.get_width(), self.window_size))
            # Draw specific cut scene details
            self.cutscene.draw(self.screen)

class CutsceneOne():
    def __init__(self):
        self.name = 'intro'
        self.step = 0
        self.timer = pygame.time.get_ticks()
        self.cutscene_running = True

        with open('assets/dialogue/dialogue1.json', 'r') as f:
            self.text = json.load(f)

        self.text_counter = 0
        self.space_pressed = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.space_pressed = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.space_pressed:
                    self.space_pressed = True
                    self.step += 1
                    self.text_counter = 0

        if self.step < 20:
            if int(self.text_counter) < len(self.text[str(self.step+1)]):
                self.text_counter += 1
        else:
            self.cutscene_running = False

        return self.cutscene_running

    def draw(self, screen):
        if self.step < 20:
            draw_text(screen, self.text[str(self.step+1)][0:int(self.text_counter)], 80, (180, 150, 100), 50, 40)
