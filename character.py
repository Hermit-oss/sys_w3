import pygame
import os

"""
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Era of Conflict")
"""
class Character():
	instances = []
	def __init__(self, faction, name, classc, hp, attack, defense, speed):
		self.faction = faction
		self.image_front = pygame.image.load(os.path.join("assets", "img", "tmp_char.png"))
       # self.image_back = image_back
	    self.font = pygame.font.Font(os.path.join("assets", "font", "Bitmgothic.ttf"), 30)
		self.name = self.font.render(name, True, (65, 32, 96))
		self.classc = self.font.render(classc, True, (65, 32, 96))
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.speed = speed
		self.__class__.instances.append(self)
	def _stats_blit_(self,surface):
        surface.blit(self.name, self.name.get_rect(center=(width // 5, height // 1.9)))
		surface.blit(self.classc, self.classc.get_rect(center=(width // 5, height // 1.75)))

Name1 = Character(faction=1,name="Name1",classc="Warrior",hp=30, attack=50, defense=40, speed=20)
Name2 = Character(faction=1,name="Name2",classc="Sorcerer",hp=35, attack=40, defense=30, speed=30)
Name3 = Character(faction=1,name="Name3",classc="Assassin",hp=25, attack=40, defense=20, speed=40)
"""
for instance in Character.instances:
	if instance.faction == 1 :
   		print(instance.name)
"""