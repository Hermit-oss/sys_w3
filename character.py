import pygame
import os
import sys

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

MENU_BASE_COLOR = (180, 150, 100)

class Character():
	instances = []
	def __init__(self, faction, name, fullname, classc, hp, attack, defense, speed, Cdescr1, Cdescr2):
		self.faction = faction
		# sprites
		self.image_front = pygame.image.load(os.path.join("assets", "img", "tmp_char.png"))
       # self.image_back = image_back
		self.name = name
		self.fullname = fullname
		self.classc = classc
		#stats
		self.hp = hp
		self.current_hp = hp
		self.attack = attack
		self.defense = defense
		self.speed = speed
		self.Cdescr1 = Cdescr1
		self.Cdescr2 = Cdescr2
		self.fainted = False
		# number of potions left
		self.num_potions = 3

		self.__class__.instances.append(self)

	def set_abilities(self):
		self.abilities = []

		targetFile = os.path.join("txt", self.name.lower() + '.txt')
		with open(targetFile, 'r') as f:
			fileString = f.read()
			fileList = fileString.split('\n')
			i = 0
			targetList = []
			while i<4:
				targetList.append(fileList[i])
				i += 1
			f.close()

		moveNumber = 0
		while moveNumber<4:
			moveName = os.path.join("txt", targetList[moveNumber].lower() + '.txt')
			with open(moveName, 'r') as f:
				fileString2 = f.read()
				fileList2 = fileString2.split('\n')
				j = 0
				singleAbility = []
				while j<6:
					singleAbility.append(fileList2[j])
					j += 1
				f.close()
			self.abilities.append(singleAbility)
			moveNumber += 1

	def stats_blit_(self,surface):
		font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 20)
		fontB = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 35)
		fontS = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 15)
		name_t = font.render(self.fullname, True, (65, 32, 96))
		class_t = fontB.render(self.classc, True, (45, 42, 76))
		hp_t = font.render('HP: ' + str(self.hp), True, (65, 32, 96))
		attack_t = font.render('Attack: ' + str(self.attack), True, (65, 32, 96))
		defense_t = font.render('Defense: ' + str(self.defense), True, (65, 32, 96))
		speed_t = font.render('Speed : ' + str(self.speed), True, (65, 32, 96))
		CD1 = fontS.render(self.Cdescr1, True, (65, 32, 96))
		CD2 = fontS.render(self.Cdescr2, True, (65, 32, 96))
		ABList = fontB.render("Abilities:", True, (65, 32, 96))
		ab1 = font.render(str(self.abilities[0][4]), True, (65, 32, 96))
		ab2 = font.render(str(self.abilities[1][4]), True, (65, 32, 96))
		ab3 = font.render(str(self.abilities[2][4]), True, (65, 32, 96))
		ab4 = font.render(str(self.abilities[3][4]), True, (65, 32, 96))
		ab1_desc = font.render(str(self.abilities[0][5]), True, (65, 32, 96))
		#ab1_rect = pygame.draw.rect(screen, "white", (WIDTH // 2, HEIGHT // 2.7, 200, 200), 2)
		ab2_desc = font.render(str(self.abilities[1][5]), True, (65, 32, 96))
		ab3_desc = font.render(str(self.abilities[2][5]), True, (65, 32, 96))
		ab4_desc = font.render(str(self.abilities[3][5]), True, (65, 32, 96))

		surface.blit(name_t, (width // 2, height // 6.5))
		surface.blit(class_t, (width // 2, height // 5.5))
		surface.blit(hp_t, (width // 2, height // 3.9))
		surface.blit(attack_t, (width // 2, height // 3.49))
		surface.blit(defense_t, (width // 2, height // 3.17))
		surface.blit(speed_t, (width // 2, height // 2.9))
		surface.blit(CD1, (width // 2.75, height // 2.5))
		surface.blit(CD2, (width // 2.75, height // 2.35))
		surface.blit(ABList, (width // 2.75, height // 1.9))
		surface.blit(ab1, (width // 2.75, height // 1.65))
		surface.blit(ab2, (width // 2.75, height // 1.515))
		surface.blit(ab3, (width // 2.75, height // 1.4))
		surface.blit(ab4, (width // 2.75, height // 1.3))	

		sprite = pygame.transform.scale(self.image_front, (200, 200))
		sprite_rect = sprite.get_rect(center=(width // 2.35, height // 3.8))
		surface.blit(sprite, sprite_rect)

	def select_list(self, surface, x, y): 
		spriteS = pygame.transform.scale(self.image_front, (100, 100))
		spriteS_rect = spriteS.get_rect(center=(x, y))
		surface.blit(spriteS, spriteS_rect)
		font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 30)
		name_text = font.render(self.name, True, MENU_BASE_COLOR)
		name_rect = name_text.get_rect(center=(x, y+75))
		class_text = font.render(self.classc, True, MENU_BASE_COLOR)
		class_rect = class_text.get_rect(center=(x, y+110))
		surface.blit(name_text, name_rect)
		surface.blit(class_text, class_rect)

	def use_potion(self):
        # check if there are potions left
		if self.num_potions > 0:
            # add 10 hp (but don't go over the max hp)
			self.current_hp += 10
			if self.current_hp > self.hp:
				self.current_hp = self.hp    
            # decrease the number of potions left
			self.num_potions -= 1

Valeria = Character(faction=1,name="Valeria",fullname="Valeria Bloodthorn",classc="Assassin",hp=30, attack=50, defense=40, speed=20,
Cdescr1="Resourceful, opportunistic, and skilled in stealth and infiltration,", Cdescr2="using their abilities to gather intelligence and strike with precision.")
Damien = Character(faction=1,name="Damien",fullname="Damien Darkbane",classc="Cleric",hp=35, attack=40, defense=30, speed=30,
Cdescr1="Zealous, fervent, and unwavering in their faith, using", Cdescr2="their divine powers to protect their comrades and spread their beliefs.")
Draven = Character(faction=1,name="Draven",fullname="Draven Bloodthorn",classc="Warrior",hp=25, attack=40, defense=20, speed=40,
Cdescr1="Fearless, tenacious, and driven by a sense of duty,", Cdescr2="always at the forefront of battle, protecting their allies and pushing forward.")
Lilith = Character(faction=1,name="Lilith",fullname="Lilith Shadowfire",classc="Mage",hp=30, attack=50, defense=40, speed=20,
Cdescr1="Ambitious, determined, and willing to push the boundaries of magic, utilizing", Cdescr2="their arcane powers to achieve their goals and further their knowledge.")
Viktor = Character(faction=1,name="Viktor",fullname="Viktor Blackthorn",classc="Paladin",hp=35, attack=40, defense=30, speed=30,
Cdescr1="Resolute, unyielding, and unwavering in their convictions, fighting", Cdescr2="for what they believe is right, even if it means making tough choices.")
Valeria.set_abilities()
Damien.set_abilities()
Draven.set_abilities()
Lilith.set_abilities()
Viktor.set_abilities()
Luna = Character(faction=2,name="Luna",fullname="Luna Shadowbane",classc="Assassin",hp=30, attack=50, defense=40, speed=20,
Cdescr1="Lethal, cunning, and secretive, with a penchant for stealth", Cdescr2="and subterfuge.")
Seraphina = Character(faction=2,name="Seraphina",fullname="Seraphina Lightbringer",classc="Cleric",hp=35, attack=40, defense=30, speed=30,
Cdescr1="Devout, compassionate, and wise, with a strong connection", Cdescr2="to the divine and a healing touch.")
Magnus = Character(faction=2,name="Magnus",fullname="Magnus Ironfoot",classc="Warrior",hp=25, attack=40, defense=20, speed=40,
Cdescr1="Brave, honorable, and skilled in combat, always ready to defend their allies and uphold justice.", Cdescr2="")
Aurora = Character(faction=2,name="Aurora",fullname="Aurora Starweaver",classc="Mage",hp=30, attack=50, defense=40, speed=20,
Cdescr1="Knowledgeable, arcane, and mysterious, with mastery over spells and the elements.", Cdescr2="")
Alistair = Character(faction=2,name="Alistair",fullname="Alistair Dawnhammer",classc="Paladin",hp=35, attack=40, defense=30, speed=30,
Cdescr1="Righteous, valiant, and dedicated to their code of honor,", Cdescr2="with unwavering faith in their cause.")
Luna.set_abilities()
Seraphina.set_abilities()
Magnus.set_abilities()
Aurora.set_abilities()
Alistair.set_abilities()

class HealthBar():
	def init(self,x,y):
		self.position = x,y
		self.negDimensions = (150,5)
		self.posDimensions = [150,5]

	def drawRects(self):
		#Function for drawing the actual rectangles that make up the health bar.
		 #(x,y,width,height)
		pygame.draw.rect(screen, (255, 0, 0), (self.position, self.negDimensions))
		pygame.draw.rect(screen, (0, 255, 0), (self.position, self.posDimensions))
  	
	def updateBar(self, charact, x, y):
		#Function for determining the appropriate current length of health stripe
		maxHealth = charact.hp
		currentHealth = charact.current_hp
		healthProportion = currentHealth/maxHealth
		newDimension = healthProportion*self.negDimensions[0]
		self.posDimensions[0] = newDimension
		# display "HP" text
		font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 15)
		text = font.render(f'HP: {charact.current_hp} / {charact.hp}', True, "black")
		text_rect = text.get_rect()
		text_rect.x = x
		text_rect.y = y 
		screen.blit(text, text_rect)

''' Ability attributes legend:

###Usage####
0. Mode
1. Damage
2. Stat effect
3. Stat target (A - Attack, D - Defense etc)
4. Name
5. Description

* indicates a situationally meaningless parameter.

####Mode Key####
1 = attack
21 = stat mod(self)
22 = stat mod(point)

##Effects Key###
+ = step up one stat level
- = step down one stat level
'''