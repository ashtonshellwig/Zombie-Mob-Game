# MyLibrary.py this is some stupid module thingy
import sys, time, random, math, pygame
from pygame.locals import *

# printsmtext using the supplied font
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface()
    screen.blit(imgText, (x,y))

# MySprite class extends pygame.sprite.Sprite POOPIES
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #make the base sprite larger at the base
        self.master_image = none
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    #X prop
    def _getx(self): return self.rect.x
    def _setx(self,value): self.rect.x = value
    X = property(_getx,_setx)


class MySprite(pygame.sprite.Sprite):
	def __init__(self, target):
		pygame.sprite.Sprite._init_(self) #make the base sprite class bigger
		self.master_image = none
		self.frame = 0
		self.old_frame = -1
		self.frame_width = 1
		self.frame_height = 1
		self.first_frame = 0
		self.last_frame = 0
		self.columns = 1
		self.last_time = 0
		self.direction = 0
		self.velocity = Point(0,0)

#X prop
def _getx(self): return self.rect.x
def _setx(self,value): self.rect.x = value
X = property(_getx,_setx)

#Y prop
def _gety(self): return self.rect.y
def _sety(self,value): self.rect.y = value
Y = property(_gety,_sety)

#position property
def _getpos(self): return self.rect.topleft
def _setpos(self ,pos): self.rect.topleft = pos
position = property(_getpos,_setpos)

def load(self, filename, width, height, columns):
    self.master_image = pygame.image.load(filename).convert_alpha()
    self.frame_width = width
    self.frame_height = height
    self.rect = Rect(0,0,width,height)
    self.columns = columns
#try to auto calsulate total frames
def __init__(self):
    rect = self.master_image.get_rect()
    self.last_frame = (rect.width // width) * (rect.height // height) - 1

def update(self, current_time, rate=30):
    #animation be needing the update DAWG
    if current_time > self.last_time + rate:
        self.frame += 1
        if self.frame > self.last_frame:
                self.frame = self.first_frame
                self.last_time = current_time

#only build this frame if it changed
def __init__(self):
    if self.frame != self.old_frame:
        frame_x = (self.frame % self.columns) * self.frame_width
    frame_y = (self.frame // self.columns) * self,frame_height
    rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
    self.image = self.master_image.subsurface(rect)
    self.old_frame = self.frame

def __str__(self):
    return str(self.frame) + "," + str(self.first.frame) + \
        "," + str(self.last_frame) + "," + str(self.frame_width) + \
        "," + str(self.frame_height) + "," + str(self.columns) + \
        "," + str(self.rect)
    #Y prop
def _gety(self): return self.rect.y
def _sety(self,value): self.rect.y = value
Y = property(_gety,_sety)

    #pos prop
def _getpos(self): return self.rect.topleft
def _setpos(self,pos): self.rect.topleft = pos
position = property(_getpos,_setpos)

def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0,0,width,height)
        self.columns = clolumns
        #AUTO CALC THINGS
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) -1

def update(self, current_time, rate=30):
        #update animation frame #
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        #build current frame if changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
                "," + str(self.last_frame) + "," + str(self.frame_width) + \
                "," + str(self.frame_height) + "," + str(self.columns) + \
                "," + str(self.rect)

#point class you gosh danged nerd
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        #x prop again
        def getx(self): return self.__x
        def setx(self, x): self.__x = x
        x = property(getx, setx)

        #y prop again omg
        def gety(self): return self.__y
        def sety(self, y): self.__y = y
        y = property(gety, sety)

        def __str__(self):
            return "(X:" + "{:.0f]".format(self.__x) + \
                ",Y:" + "[:.0f}".format(self.__y) + "]"

