import pygame, math, random

pygame.init()

plane = pygame.image.load("plane.png")
bulletIm = pygame.image.load("bullet.png")

planeSpeed = 4.5
bulletSpeed = 12

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((800, 600))
map = pygame.Surface((3000, 1000))
map.fill((150, 226, 219))

for x in range(10):
    pygame.draw.rect(map, (0, 0, 0),((x*100,x*100),(20,20)))


class bullet():
	def __init__(self, xPos, yPos, angle):
		self.xPos = xPos
		self.yPos = yPos
		self.img = bulletIm
		self.angle = angle

	def update(self):
		self.xPos += bulletSpeed * math.cos(math.radians(self.angle))
		self.yPos -= bulletSpeed * math.sin(math.radians(self.angle))

	def draw(self):
		map.blit(pygame.transform.rotate(bulletIm, self.angle - 90), (self.xPos, self.yPos))


class player():
	def __init__(self, xPos, yPos, angle):
		self.xPos = xPos
		self.yPos = yPos
		self.img = plane
		self.angle = angle
		self.xCam = 0
		self.yCam = 0
		self.bullets = []

	def update(self):
		self.xPos += planeSpeed * math.cos(math.radians(self.angle))
		self.yPos -= planeSpeed * math.sin(math.radians(self.angle))
		self.xCam -= planeSpeed * math.cos(math.radians(self.angle))
		self.yCam += planeSpeed * math.sin(math.radians(self.angle))
		if self.xPos < 0:
			self.xPos = 0
			
		if self.xPos > 2970:
			self.xPos = 2970
			
		if self.yPos < 0:
			self.yPos = 0
			
		if self.yPos > 970:
			self.yPos = 970
			

		if self.xPos < 400:
			self.xCam = 0
		elif self.xPos > 2600:
			self.xCam = -2200
		else:
			self.xCam = 400 - self.xPos

		if self.yPos < 300:
			self.yCam = 0
		elif self.yPos > 700:
			self.yCam = -400
		else:
			self.yCam = -(self.yPos - 300)



	def draw(self):
		map.blit(pygame.transform.rotate(plane, self.angle - 90), (self.xPos, self.yPos))

	def changeAngle(self, direction):
		if (direction == 'R'):
			self.angle -= 3.2
		else:
			self.angle += 3.2
		self.angle %= 360

	def fireBullet(self):


		if self.angle > 0 and self.angle <= 90:
			self.bullets.append(bullet(self.xPos + 15, self.yPos + 7.5, self.angle))


		elif self.angle > 90 and self.angle <= 180:
			self.bullets.append(bullet(self.xPos - 2, self.yPos + 7.5, self.angle))


		elif self.angle >= 180 and self.angle < 270:
			self.bullets.append(bullet(self.xPos - 2, self. yPos + 7.5, self.angle))


		else:
			self.bullets.append(bullet(self.xPos + 15, self.yPos + 7.5, self.angle))

	def drawBullet(self):
		print len(self.bullets)
		for bullet in self.bullets:
			bullet.draw()
			bullet.update()
			if (bullet.xPos > 3000 or bullet.xPos < 0 or bullet.yPos > 1000 or bullet.yPos < 0):
				self.bullets.remove(bullet)

	def getCam(self):
		return (self.xCam, self.yCam)

gameExit = False

f1 = 0
f2 = 0
fireBullet = 0
obj = player(0, 300, 0)



while not gameExit:
	gameDisplay.fill((255, 255, 255))
	map.fill((150, 226, 219))
	for x in range(30):
        	pygame.draw.rect(map, (0, 0, 0),((x*100,300),(20,20)))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				f1 = 1
			elif event.key == pygame.K_LEFT:
				f2 = 1
			elif event.key == pygame.K_SPACE:
				obj.fireBullet()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				f1 = 0
			elif event.key == pygame.K_LEFT:
				f2 = 0
			elif event.key == pygame.K_SPACE:
				fireBullet = 0


	if f1 == 1 and f2 == 0:
		obj.changeAngle('R')
	if f1 == 0 and f2 == 1:
		obj.changeAngle('L')

	

	
	obj.drawBullet()
	obj.update()
	obj.draw()
	camPos = obj.getCam()

	gameDisplay.blit(map, camPos)
	pygame.display.update()

	clock.tick(60)














