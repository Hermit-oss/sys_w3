import pygame
import sys, os, random, time
from button import Button, ToggleButton
from character import *
from cutscene import Cutscene, CutsceneOne

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

# Main menu background animation
CUTSCENE1_FRAMES = []
for i in range(1, 4):
    filename = os.path.join('assets/img/cs1', f'{i}.png')
    frame = pygame.transform.scale(pygame.image.load(filename).convert_alpha(), SCREEN.get_size())
    CUTSCENE1_FRAMES.append(frame)

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

# Set up cutscenes admin
cutscene = Cutscene(SCREEN)

# Lists
chosen = []
enemies = []

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
        MOUSE_POS = pygame.mouse.get_pos()

        # Draw the screen
        SCREEN.fill((0, 0, 0))

        # Set up credits background
        BG = pygame.transform.scale(pygame.image.load("assets/img/bgwood.jpg"), SCREEN.get_size())
        SCREEN.blit(BG, (0, 0))

        # Set up credits text
        TEXT = getFont(100).render("We're thankful to", True, MENU_BASE_COLOR)
        RECT = TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 6))
        SCREEN.blit(TEXT, RECT)

        # Set up credits text
        TEXT1 = getFont(50).render("Creators: JJEntertainment", True, MENU_BASE_COLOR)
        RECT1 = TEXT1.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        SCREEN.blit(TEXT1, RECT1)

        # Set up credits text
        TEXT2 = getFont(50).render("BG Anima: Camille Unknown", True, MENU_BASE_COLOR)
        RECT2 = TEXT2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        SCREEN.blit(TEXT2, RECT2)

        # Set up credits text
        TEXT3 = getFont(50).render("BG Music: Ruiqi Zhao", True, MENU_BASE_COLOR)
        RECT3 = TEXT3.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
        SCREEN.blit(TEXT3, RECT3)

        # Set up credits BACK button
        BACK = Button(image=None, pos=(WIDTH // 3.5, HEIGHT // 1.06),
                            text_input="BACK", font=getFont(90), base_color=MENU_BASE_COLOR, hovering_color="red")
        BACK.changeColor(MOUSE_POS)
        BACK.update(SCREEN)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MOUSE_POS):
                    main_menu()

        pygame.display.update()

def menu_selection(): # Menu selection method
    # Set the window caption
    pygame.display.set_caption("Menu Selection")
    frame_index = 0

    while True:
        # Get menu selection mouse position
        MENU_SELECTION_MOUSE_POS = pygame.mouse.get_pos()

        # Draw the screen
        SCREEN.fill((0, 0, 0))

        cutscene.start_cutscene(CutsceneOne())

        if cutscene.cutscene_running:
            frame = CUTSCENE1_FRAMES[frame_index]
            frame_index = (frame_index + 1) % len(CUTSCENE1_FRAMES)
            SCREEN.blit(frame, (0, 0))

            # Set up menu selection text
            CUTSCENE1_TEXT = getFont(60).render("Press SPACE", True, MENU_BASE_COLOR)
            CUTSCENE1_RECT = CUTSCENE1_TEXT.get_rect(center=(7*WIDTH // 8, HEIGHT // 1.06))
            SCREEN.blit(CUTSCENE1_TEXT, CUTSCENE1_RECT)

            cutscene.update()
            cutscene.draw()
        else:
            # Set up menu selection background
            MENU_SELECTION_BG = pygame.transform.scale(pygame.image.load("assets/img/bgwood.jpg"), SCREEN.get_size())
            SCREEN.blit(MENU_SELECTION_BG, (0, 0))

            # Set up menu selection text
            MENU_SELECTION_TEXT = getFont(100).render("Pledge your allegiance", True, MENU_BASE_COLOR)
            MENU_SELECTION_RECT = MENU_SELECTION_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 6))
            SCREEN.blit(MENU_SELECTION_TEXT, MENU_SELECTION_RECT)

            # Set up menu selection FACTION1 button
            MENU_SELECTION_FACTION1 = Button(image=None, pos=(WIDTH // 2, HEIGHT // 2.25),
                                text_input="The Crimson Legion", font=getFont(70), base_color=MENU_BASE_COLOR, hovering_color="red")
            MENU_SELECTION_FACTION1.changeColor(MENU_SELECTION_MOUSE_POS)
            MENU_SELECTION_FACTION1.update(SCREEN)

            # Set up menu selection FACTION2 button
            MENU_SELECTION_FACTION2 = Button(image=None, pos=(WIDTH // 2, HEIGHT // 1.75),
                                text_input="The Mystic Conclave", font=getFont(70), base_color=MENU_BASE_COLOR, hovering_color="red")
            MENU_SELECTION_FACTION2.changeColor(MENU_SELECTION_MOUSE_POS)
            MENU_SELECTION_FACTION2.update(SCREEN)

            # Set up menu selection BACK button
            MENU_SELECTION_BACK = Button(image=None, pos=(WIDTH // 3.5, HEIGHT // 1.06),
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
     
    
    SELECT_CHARACTER_1 = ToggleButton(image=pygame.transform.scale(pygame.image.load("assets/img/buttonbg.png"), (220, 60)), pos=(305, 570),
                 text_input="PICK", font=getFont(30), base_color=MENU_BASE_COLOR, hovering_color="red")
    SELECT_CHARACTER_2 = ToggleButton(image=pygame.transform.scale(pygame.image.load("assets/img/buttonbg.png"), (220, 60)), pos=(555, 570),
                 text_input="PICK", font=getFont(30), base_color=MENU_BASE_COLOR, hovering_color="red")
    SELECT_CHARACTER_3 = ToggleButton(image=pygame.transform.scale(pygame.image.load("assets/img/buttonbg.png"), (220, 60)), pos=(805, 570),
                 text_input="PICK", font=getFont(30), base_color=MENU_BASE_COLOR, hovering_color="red")
    SELECT_CHARACTER_4 = ToggleButton(image=pygame.transform.scale(pygame.image.load("assets/img/buttonbg.png"), (220, 60)), pos=(1055, 570),
                 text_input="PICK", font=getFont(30), base_color=MENU_BASE_COLOR, hovering_color="red")
    SELECT_CHARACTER_5 = ToggleButton(image=pygame.transform.scale(pygame.image.load("assets/img/buttonbg.png"), (220, 60)), pos=(1305, 570),
                 text_input="PICK", font=getFont(30), base_color=MENU_BASE_COLOR, hovering_color="red")

    index = 0
    for instance in Character.instances:
        if instance not in enemies and index==0: 
            if instance.faction != set_n and len(enemies)<3:
                enemies.append(instance)

    while True:
        # Get character selection mouse position
        CHARACTER_SELECTION_MOUSE_POS = pygame.mouse.get_pos()

        # Draw the screen
        SCREEN.fill((0, 0, 0))

        # Set up character selection background
        CHARACTER_SELECTION_BG = pygame.transform.scale(pygame.image.load("assets/img/bgwood.jpg"), SCREEN.get_size())
        SCREEN.blit(CHARACTER_SELECTION_BG, (0, 0))

        # Set up character selection text
        CHARACTER_TEXT = getFont(100).render("Pick three companions", True, MENU_BASE_COLOR)
        CHARACTER_RECT = CHARACTER_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 6))
        SCREEN.blit(CHARACTER_TEXT, CHARACTER_RECT)

        # Set up character selection BACK button
        CHARACTER_SELECTION_BACK = Button(image=None, pos=(WIDTH // 3.5, HEIGHT // 1.06),
                            text_input="BACK", font=getFont(90), base_color=MENU_BASE_COLOR, hovering_color="red")
        CHARACTER_SELECTION_BACK.changeColor(CHARACTER_SELECTION_MOUSE_POS)
        CHARACTER_SELECTION_BACK.update(SCREEN)

        x = 305 
        y = 350
        i=0

        for instance in Character.instances:

            if instance.faction == set_n :
                instance.select_list(SCREEN, x, y)
                i+=1 
                 # Set up character selection ABOUT button
                ABOUT_CHARACTER = Button(image=pygame.transform.scale(pygame.image.load("assets/img/buttonbg.png"), (220, 60)), pos=(x, y+165),
                text_input="ABOUT", font=getFont(30), base_color=MENU_BASE_COLOR, hovering_color="red")
                ABOUT_CHARACTER.changeColor(CHARACTER_SELECTION_MOUSE_POS)
                ABOUT_CHARACTER.update(SCREEN)
                # Set up character selection PICK button
                SELECT_CHARACTER_1.changeColor(CHARACTER_SELECTION_MOUSE_POS)
                SELECT_CHARACTER_1.update(SCREEN)
                SELECT_CHARACTER_2.changeColor(CHARACTER_SELECTION_MOUSE_POS)
                SELECT_CHARACTER_2.update(SCREEN)
                SELECT_CHARACTER_3.changeColor(CHARACTER_SELECTION_MOUSE_POS)
                SELECT_CHARACTER_3.update(SCREEN)
                SELECT_CHARACTER_4.changeColor(CHARACTER_SELECTION_MOUSE_POS)
                SELECT_CHARACTER_4.update(SCREEN)
                SELECT_CHARACTER_5.changeColor(CHARACTER_SELECTION_MOUSE_POS)
                SELECT_CHARACTER_5.update(SCREEN)                
                x += 250 # wyświetlenie zmian na ekranie
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if ABOUT_CHARACTER.checkForInput(CHARACTER_SELECTION_MOUSE_POS):
                            info_window(instance) 
                        if i==1:
                            if SELECT_CHARACTER_1.checkForInput(CHARACTER_SELECTION_MOUSE_POS):
                                if instance not in chosen:
                                    chosen.append(instance)
                                else:
                                    chosen.remove(instance) 
                        if i==2:
                            if SELECT_CHARACTER_2.checkForInput(CHARACTER_SELECTION_MOUSE_POS):
                                if instance not in chosen:
                                    chosen.append(instance)
                                else:
                                    chosen.remove(instance)      
                        if i==3:
                            if SELECT_CHARACTER_3.checkForInput(CHARACTER_SELECTION_MOUSE_POS):
                                if instance not in chosen:
                                    chosen.append(instance)
                                else:
                                    chosen.remove(instance)
                        if i==4:
                            if SELECT_CHARACTER_4.checkForInput(CHARACTER_SELECTION_MOUSE_POS):
                                if instance not in chosen:
                                    chosen.append(instance)
                                else:
                                    chosen.remove(instance)      
                        if i==5:
                            if SELECT_CHARACTER_5.checkForInput(CHARACTER_SELECTION_MOUSE_POS):
                                if instance not in chosen:
                                    chosen.append(instance)
                                else:
                                    chosen.remove(instance)                                                                                                 
                        if CHARACTER_SELECTION_BACK.checkForInput(CHARACTER_SELECTION_MOUSE_POS):
                            return            

        if len(chosen) > 2 and len(chosen) < 4 :
            battle()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CHARACTER_SELECTION_BACK.checkForInput(CHARACTER_SELECTION_MOUSE_POS):
                    menu_selection()
                    chosen.clear()
                    enemies.clear()


        pygame.display.update()

def info_window(character): # Screen that contains informations about character
     # Set the window caption
    pygame.display.set_caption("Character Stats and Abilities")
    while True:
        # Draw the screen
        SCREEN.fill((0, 0, 0))

        # Set up menu selection background
        MENU_SELECTION_BG = pygame.transform.scale(pygame.image.load("assets/img/bgwood.jpg"), SCREEN.get_size())
        SCREEN.blit(MENU_SELECTION_BG, (0, 0))

        # Get mouse position
        X_MOUSE_POS = pygame.mouse.get_pos()

        SCALED_BOX = pygame.transform.scale(pygame.image.load("assets/img/metal.png"), (700, 825))
        SCREEN.blit(SCALED_BOX, (425, 25))   

        # Set up X button (back to character selection)
        X = Button(image=None, pos=(WIDTH // 1.5, HEIGHT // 10),
                            text_input="X", font=getFont(50), base_color="red", hovering_color=(255, 77, 77))
        X.changeColor(X_MOUSE_POS)
        X.update(SCREEN)   

        character.stats_blit_(SCREEN)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if X.checkForInput(X_MOUSE_POS):
                     # Set up character selection background
                    CHARACTER_SELECTION_BG = pygame.transform.scale(pygame.image.load("assets/img/bgwood.jpg"), SCREEN.get_size())
                    SCREEN.blit(CHARACTER_SELECTION_BG, (0, 0))
                    return

        pygame.display.flip()


def battle():
    pygame.display.set_caption("Battle Mode")
    iP = 0
    iC = 0
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill(MENU_BASE_COLOR)
        #over = False

        player = chosen[iP]
        rival = enemies[iC]
        playerBar = HealthBar()
        playerBar.init(350,270)
        playerBar.drawRects()
        playerBar.updateBar(player,425,250)
        computerBar = HealthBar()
        computerBar.init(1100,50)
        computerBar.drawRects()
        computerBar.updateBar(rival,1175,30)

        spriteP = pygame.transform.scale(player.image, (250, 250))
        spriteP_rect = spriteP.get_rect(center=(width // 3.5, height // 2))
        SCREEN.blit(spriteP, spriteP_rect)
        spriteR = pygame.transform.scale(rival.image, (200, 200))
        spriteR_rect = spriteR.get_rect(center=(width // 1.3, height // 5))
        SCREEN.blit(spriteR, spriteR_rect)
        actions = pygame.transform.scale(pygame.image.load("assets/img/scroll.png"), (1500, 400))
        actions_rect =  actions.get_rect(center=(width // 2, height // 1.1))
        SCREEN.blit(actions, actions_rect)

        # Set up buttons
        ABILITY1 = Button(image=None, pos=(WIDTH // 5, HEIGHT // 1.17),text_input=str(player.abilities[0][4]), 
        font=getFont(20), base_color=MENU_BASE_COLOR, hovering_color="red")
        ABILITY2 = Button(image=None, pos=(WIDTH // 2.5, HEIGHT // 1.17),text_input=str(player.abilities[1][4]), 
        font=getFont(20), base_color=MENU_BASE_COLOR, hovering_color="red")
        ABILITY3 = Button(image=None, pos=(WIDTH // 5, HEIGHT // 1.07), text_input=str(player.abilities[2][4]), 
        font=getFont(20), base_color=MENU_BASE_COLOR, hovering_color="red")
        ABILITY4 = Button(image=None, pos=(WIDTH // 2.5, HEIGHT // 1.07),text_input=str(player.abilities[3][4]), 
        font=getFont(20), base_color=MENU_BASE_COLOR, hovering_color="red")
        POTIONS = Button(image=None, pos=(WIDTH // 1.5, HEIGHT // 1.17), text_input="Use Potion (+10 HP)",
        font=getFont(20), base_color=MENU_BASE_COLOR, hovering_color="red")
        ABILITY1.changeColor(MOUSE_POS)
        ABILITY1.update(SCREEN)
        ABILITY2.changeColor(MOUSE_POS)
        ABILITY2.update(SCREEN)
        ABILITY3.changeColor(MOUSE_POS)
        ABILITY3.update(SCREEN)
        ABILITY4.changeColor(MOUSE_POS)
        ABILITY4.update(SCREEN)
        POTIONS.changeColor(MOUSE_POS)   
        POTIONS.update(SCREEN)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ABILITY1.checkForInput(MOUSE_POS):
                    pAction = player.abilities[0]
                    turn(player, rival, pAction)
                if ABILITY2.checkForInput(MOUSE_POS):  
                    pAction = player.abilities[1]
                    turn(player, rival, pAction)
                if ABILITY3.checkForInput(MOUSE_POS):
                    pAction = player.abilities[2]
                    turn(player, rival, pAction)
                if ABILITY4.checkForInput(MOUSE_POS):
                    pAction = player.abilities[3]
                    turn(player, rival, pAction)

                if POTIONS.checkForInput(MOUSE_POS):
                    player.use_potion()
                    POTION_TEXT = getFont(20).render(f'You have {player.num_potions} potions left', True, "red")
                    POTION_RECT = POTION_TEXT.get_rect(center=(WIDTH // 1.5, HEIGHT // 1.07))
                    SCREEN.blit(POTION_TEXT, POTION_RECT)
                    pygame.display.update()
                    time.sleep(2)
                    if player.num_potions > 0:
                        rivalturn(player,rival)

        if player.fainted == True:
            if iP == 2:
                END_TEXT = getFont(80).render('GAME OVER', True, "red")
                END_RECT = END_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                SCREEN.blit(END_TEXT, END_RECT)
                pygame.display.update()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            DEF_TEXT = getFont(40).render('Your hero fainted, next one will enter the fight', True, "red")
            DEF_RECT = DEF_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            SCREEN.blit(DEF_TEXT, DEF_RECT)
            pygame.display.update()
            time.sleep(1.5)
            iP += 1
            player = chosen[iP]
                
        if rival.fainted == True:
            if iC == 2:
                END_TEXT = getFont(80).render('VICTORY!', True, "red")
                END_RECT = END_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                SCREEN.blit(END_TEXT, END_RECT)
                pygame.display.update()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            DEF_TEXT = getFont(40).render('Enemy defeaded, prepare for next one', True, "red")
            DEF_RECT = DEF_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            SCREEN.blit(DEF_TEXT, DEF_RECT)
            pygame.display.update()
            time.sleep(1.5)
            iC += 1
            rival = enemies[iC]

        playerBar.updateBar(player,425,250)
        playerBar.drawRects()
        computerBar.drawRects()
        computerBar.updateBar(rival,1175,30)
        pygame.display.update()

def rivalturn(player,rival):
    rAction =  rival.abilities[random.randint(0,3)]
    Attack(rAction, player, rival)
    if player.current_hp <= 0:
        player.fainted = True
        return

def turn(player, rival, pAction):
    rAction =  rival.abilities[random.randint(0,3)]
    if player.current_hp <= 0:
        player.fainted = True
        return
    if rival.current_hp <= 0:
        rival.fainted = True
        return  
    if player.speed > rival.speed:
        Attack(pAction, rival, player)
        if player.current_hp <= 0:
            player.fainted = True
            return
        if rival.current_hp <= 0:
            rival.fainted = True
            return        
        Attack(rAction, player, rival)
        if player.current_hp <= 0:
            player.fainted = True
            return
        if rival.current_hp <= 0:
            rival.fainted = True
            return          
    else:
        Attack(rAction, player, rival)       
        if player.current_hp <= 0:
            player.fainted = True
            return
        if rival.current_hp <= 0:
            rival.fainted = True
            return         
        Attack(pAction, rival, player)
        if player.current_hp <= 0:
            player.fainted = True
            return
        if rival.current_hp <= 0:
            rival.fainted = True
            return          

def Attack(Action, target, attacker):
    SCREEN.fill(MENU_BASE_COLOR)
    stringT = str(attacker.name) + " used " + str(Action[4])
    TEXT = getFont(80).render(stringT, True, "red")
    RECT = TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    SCREEN.blit(TEXT, RECT)
    pygame.display.update()
    time.sleep(1.5)
    TEXT = getFont(80).render(stringT, True, MENU_BASE_COLOR)
    SCREEN.blit(TEXT, RECT)
    pygame.display.update()
    mode = Action[0]
    if mode == "1":
        DamageMod(attacker, Action, target, False)
    if mode == "2":
        DamageMod(attacker, Action, target, True)
    elif mode == "21":
        StatMod(Action, attacker)
    elif mode == "22":
        StatMod(Action, target)

def DamageMod(attacker, attack, target, isDrain):
    SCREEN.fill(MENU_BASE_COLOR)
    DMG = int(attack[1])
    aATK = attacker.attack
    tDEF = target.defense
    effect = DMG*(aATK/tDEF) #Calculate actual damage effect
    target.current_hp = target.current_hp - round(effect)

    stringT = str(attacker.name) + " dealt " + str(round(effect)) + " damage!"
    TEXT = getFont(80).render(stringT, True, "red")
    RECT = TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
    SCREEN.blit(TEXT, RECT)
    pygame.display.update()
    time.sleep(1.5)
    TEXT = getFont(80).render(stringT, True, MENU_BASE_COLOR)
    SCREEN.blit(TEXT, RECT)
    pygame.display.update()
    if isDrain == True:
        heal = round(effect) * 0.3
        attacker.current_hp = attacker.current_hp + round(heal)
        stringT = str(attacker.name) + " drained " + str(round(effect)) + "HP from target", 
        TEXT = getFont(40).render(stringT, True, "red")
        RECT = TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
        SCREEN.blit(TEXT, RECT)
        pygame.display.update()
        time.sleep(1.5)
        TEXT = getFont(40).render(stringT, True, MENU_BASE_COLOR)
        SCREEN.blit(TEXT, RECT)
        pygame.display.update()
    return 

def StatMod(ability, target):
    SCREEN.fill(MENU_BASE_COLOR)
    targetStat = ability[3]
    effect = ability[2]
    if targetStat == "A": #If target stat is attack
        if effect == "-":
            target.attack -= 1 #target's attack is lowered
            stringT = str(target.name) + "'s Attack fell."
            TEXT = getFont(80).render(stringT, True, "red")
            RECT = TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()
            time.sleep(1.5)
            TEXT = getFont(80).render(stringT, True, MENU_BASE_COLOR)
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()
            return 
        else:
            target.attack += 1 #target's atack is raised
            stringT = str(target.name) + "'s Attack rose."
            TEXT = getFont(80).render(stringT, True, "red")
            RECT = TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()
            time.sleep(1.5)
            TEXT = getFont(80).render(stringT, True, MENU_BASE_COLOR)
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()  
            return 
    elif targetStat == "D": #If target stat is defense
        if effect == "-": 
            target.defense -= 1 #target's defense is lowered
            stringT = str(target.name) + "'s Defense fell."
            TEXT = getFont(80).render(stringT, True, "red")
            RECT = TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()
            time.sleep(1.5)
            TEXT = getFont(80).render(stringT, True, MENU_BASE_COLOR)
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()
            return 
        else: 
            target.defense += 1 #target's defense is raised
            stringT = str(target.name) + "'s Defense rose."
            TEXT = getFont(80).render(stringT, True, "red")
            RECT = TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()
            time.sleep(1.5)
            TEXT = getFont(80).render(stringT, True, MENU_BASE_COLOR)
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()    
            return 
    else: #If target stat is speed (S)
        if effect == "-": 
            target.defense -= 1 #target's speed is lowered
            stringT = str(target.name) + "'s Speed fell."
            TEXT = getFont(80).render(stringT, True, "red")
            RECT = TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()
            time.sleep(1.5)
            TEXT = getFont(80).render(stringT, True, MENU_BASE_COLOR)
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()
            return 
        else: 
            target.defense += 1 #target's speed is raised
            stringT = str(target.name) + "'s Speed rose."
            TEXT = getFont(80).render(stringT, True, "red")
            RECT = TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()
            time.sleep(1.5)
            TEXT = getFont(80).render(stringT, True, MENU_BASE_COLOR)
            SCREEN.blit(TEXT, RECT)
            pygame.display.update()    
            return 

main_menu()
