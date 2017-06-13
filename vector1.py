#!/usr/bin/env python
__author__ = "Dante Calderon"

import math
import sys
import pygame
from pygame.locals import *


pygame.init()
DISPLAY = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Vector 1")


FPS = 30 # Frames por segundo
fpsClock = pygame.time.Clock()

# Colores
RED  = (255, 0,   0)
BLUE = (  0, 0, 255)
BLACK = (0, 0,0)


def limits(a):
	if a < 0:
		return 359
	elif a > 360:
		return 1
	else:
		return a



def main():

	angle = 0
	velocity = 5
	R = 20
	startPos = [400, 300]
	endPos = [30, 30]
	#        LEFT    RIGHT  UP    DOWN    
	keys = [False, False, False, False]


	while True:
		#-------- EVENT ----------------------
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					keys[0] = True
				if event.key == pygame.K_RIGHT:
					keys[1] = True
				if event.key == pygame.K_UP:
					keys[2] = True
				if event.key == pygame.K_DOWN:
					keys[3] = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					keys[0] = False
				if event.key == pygame.K_RIGHT:
					keys[1] = False
				if event.key == pygame.K_UP:
					keys[2] = False
				if event.key == pygame.K_DOWN:
					keys[3] = False

		#--------------------------------------
		if keys[0]:
			angle -= velocity
			angle = limits(angle)
		if keys[1]:
			angle += velocity
			angle = limits(angle)
		if keys[2]:
			R += velocity
		if keys[3]:
			R -= velocity

		DISPLAY.fill(BLACK)
		endPos[0] = math.cos(math.radians(angle)) # x Position
		endPos[1] = math.sin(math.radians(angle)) # y Position
		endPos[0] *= R
		endPos[1] *= R
		endPos[0] += 400
		endPos[1] += 300

		pygame.draw.line(DISPLAY, RED, (startPos[0], startPos[1]), (endPos[0], endPos[1]), 1)

		pygame.display.update()
		fpsClock.tick(FPS)


main()