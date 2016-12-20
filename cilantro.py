from entity import *
import pygame
import math


class cilantro(entity):

    def __init__(self, name, x, y, img1, img2, img3, vel, playerPos):
        entity.__init__(self, name, x, y, img1)
        self.img1 = pygame.image.load(img1)
        self.img2 = pygame.image.load(img2)
        self.img3 = pygame.image.load(img3)
        self.velocity = vel
        self.angle = 0
        self.dest = playerPos
        self.xMove, self.ymove = 0, 0
        self.which_image = 0
        x = self.dest[0] - self.getPos()[0] + 0.1
        y = self.dest[1] - self.getPos()[1] + 0.1
        rads = math.atan2(-y,x)
        rads %= 2*math.pi
        self.angle = math.degrees(rads)
        x, y = x / max(x, y), y / max(x,y)
        self.angle = 90
        print(self.angle)
        self.xMove = x * self.velocity
        self.yMove = y * self.velocity

    def move(self):
        self.which_image += 1
        self.selectImage()
        self.x = self.x + self.xMove
        self.y = self.y + self.yMove

    def selectImage(self):
        if self.which_image % 48 == 0:
            self.img = pygame.transform.rotate(self.img1, -self.angle)
        elif self.which_image % 24 == 0:
            self.img = pygame.transform.rotate(self.img2, -self.angle)
        elif self.which_image % 12 == 0:
            self.img = pygame.transform.rotate(self.img3, -self.angle)

    def setPos(self, x, y):
        self.x, self.y = x, y
