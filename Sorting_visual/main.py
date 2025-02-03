import pygame
import random
pygame.init()

width = 1500
height = 900 
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bubble sort")

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)

running = True
class block:
	def __init__(self,value,x,colour):
		self.value = value
		self.x = x
		self.colour = colour

	def draw_self(self):	
		pygame.draw.rect(screen,self.colour,(self.x,self.value,13,height-self.value))

blocks = []
for i in range(0,width+1,width//100):
	blocks.append(block(random.randint(1,850),i,green))

while running :
	screen.fill(black)
	for i in blocks:
		i.draw_self()
	pygame.display.flip()
	pygame.display.update()
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.time.delay(100)


pygame.quit()

