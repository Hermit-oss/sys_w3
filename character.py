import pygame
import os
import sys

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

MENU_BASE_COLOR = (180, 150, 100)

class Character():
	instances = []
	def __init__(self, faction, name, classc, hp, attack, defense, speed):
		self.faction = faction
		self.image_front = pygame.image.load(os.path.join("assets", "img", "tmp_char.png"))
       # self.image_back = image_back
		self.name = name
		self.classc = classc
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.speed = speed
		self.__class__.instances.append(self)

	def stats_blit_(self,surface):
		font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 20)
		fontB = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 35)
		name_t = font.render(self.name, True, (65, 32, 96))
		class_t = fontB.render(self.classc, True, (45, 42, 76))
		hp_t = font.render('HP: ' + str(self.hp), True, (65, 32, 96))
		attack_t = font.render('Attack: ' + str(self.attack), True, (65, 32, 96))
		defense_t = font.render('Defense: ' + str(self.defense), True, (65, 32, 96))
		speed_t = font.render('Speed : ' + str(self.speed), True, (65, 32, 96))
		
		surface.blit(name_t, (width // 2, height // 6.5))
		surface.blit(class_t, (width // 2, height // 5.5))
		surface.blit(hp_t, (width // 2, height // 3.9))
		surface.blit(attack_t, (width // 2, height // 3.49))
		surface.blit(defense_t, (width // 2, height // 3.17))
		surface.blit(speed_t, (width // 2, height // 2.9))

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


Name1 = Character(faction=1,name="Name1",classc="Warrior",hp=30, attack=50, defense=40, speed=20)
Name2 = Character(faction=1,name="Name2",classc="Sorcerer",hp=35, attack=40, defense=30, speed=30)
Name3 = Character(faction=1,name="Name3",classc="Assassin",hp=25, attack=40, defense=20, speed=40)
Name4 = Character(faction=2,name="Name1",classc="Necromancer",hp=30, attack=50, defense=40, speed=20)
Name5 = Character(faction=2,name="Name2",classc="Paladin",hp=35, attack=40, defense=30, speed=30)
Name6 = Character(faction=2,name="Name3",classc="Rogue",hp=25, attack=40, defense=20, speed=40)
