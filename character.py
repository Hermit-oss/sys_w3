import pygame
import os

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

Name1 = Character(faction=1,name="Name1",classc="Warrior",hp=30, attack=50, defense=40, speed=20)
Name2 = Character(faction=1,name="Name2",classc="Sorcerer",hp=35, attack=40, defense=30, speed=30)
Name3 = Character(faction=1,name="Name3",classc="Assassin",hp=25, attack=40, defense=20, speed=40)
"""
for instance in Character.instances:
	if instance.faction == 1 :
   		print(instance.name)
"""