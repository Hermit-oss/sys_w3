import pygame

class Character():

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

	# def image_resize(self, image_back):