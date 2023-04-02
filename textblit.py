import pygame
import os
import sys

# Initialize Pygame
pygame.init()

class _text_():
    def __init__(self,text,pos):
        pygame.init()
        self.antialias = True
        self.colour = (255,255,255)    
        self.background = None
        self.pos = pos
        self.font = pygame.font.SysFont("arialblack",40)
        self.img = self.font.render(text, self.antialias, self.colour,self.background)
    def _textblit_(self,surface):
        surface.blit(self.img, self.img.get_rect(center=(self.pos)))

# Set up the screen
#width, height = screen.get_size()
pygame.display.set_caption("Era of Conflict")

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
text1 = _text_(": )",(SCREEN_WIDTH // 2,SCREEN_HEIGHT //2))  
text2 = _text_("Koniec testu",(SCREEN_WIDTH // 2,SCREEN_HEIGHT //2.5))

run = True

while run:
    screen.fill((52,78,91))
    text1._textblit_(screen)
    text2._textblit_(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    pygame.display.update()
    
pygame.quit()