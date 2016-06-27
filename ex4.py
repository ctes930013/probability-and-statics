# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 20:37:18 2016

@author: 孔令宣
"""

#_*_ coding:utf-8 _*_
# bouncingcircle.py
#遊戲說明:改編自訊號與系統的期末作業  玩法為玩家可控制一架飛機  螢幕上會有六顆球再飛來飛去  彼此若互相碰撞  則產生
#一個金屬碰撞聲(會延遲)  且彼此彈開  若玩家羽球發生碰撞  不會彈開  而是加分  且發出杯離杯碰撞聲(也會延遲)  分數依據球穿越飛機的長度而定  限時一分鐘  
#看看玩家的得分有多少  若時間到  則使用者可按上下左右鍵離開遊戲

import pygame, random, math, time, sys
from pygame.locals import *
from thinkdsp import *

pygame.init()

green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bluegreen = (0,255,255)
rightborder = 1150  #設定玩家移動邊界
leftborder = 50
topborder = 62
bottomborder = 605
mobile = 70  #定義玩家移動的單位長度
count = 0  #計數目前玩家的得分
pygame.mixer.init()

#radius = 20

size = 1200, 640
screen = pygame.display.set_mode((size))
screen.fill(black)
background = pygame.Surface(size)
background = background.convert()
background.fill(black)

class stony(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30,30))
		color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
		pygame.draw.circle(self.image, color, (15,15), 15,0)
		self.rect = self.image.get_rect()
		self.rect.centerx = random.randrange(0,1200)
		self.rect.centery = random.randrange(0,640)
		self.dx = random.randrange(-45,50)
		self.dy = random.randrange(-45,50)
	def checkbound(self):
		if (self.rect.left <= 0 or self.rect.right >= screen.get_width()):
			self.dx *= -1
		if (self.rect.top <= 0 or self.rect.bottom >= screen.get_height()):
			self.dy *= -1
	def update(self):
		self.checkbound()
		self.rect.centerx += self.dx
		self.rect.centery += self.dy
	
#檢查是否有球和玩家發生撞擊
def checkhit(a,b,ra,rb):
    rb = math.sqrt(math.pow(rb,2)+math.pow(rb,2))
    xa = a.rect.centerx
    xb = b.centerx
    ya = a.rect.centery
    yb = b.centery
    hit = math.sqrt(math.pow((xb-xa),2)+math.pow((yb-ya),2))
    if(hit <= (ra+rb)):
        return True
    else:
        return False
        
#輸出文字
def printchar(chstr,fonts,color,x,y,size):
    pygame.font.get_fonts()
    font = pygame.font.Font(fonts,size)
    text = font.render('%s'%chstr,True,color)
    screen.blit(text,(x,y))               

downcount = 60  #用來計算一分鐘的倒數計時器
shipimg = pygame.image.load("spaceship.png")
shipimg = shipimg.convert()
shipimg = pygame.transform.scale(shipimg, [50,50])
shipimg.set_colorkey((0,0,0))
shiprect = shipimg.get_rect()
shiprect.center = (600,580)

snow_list = []
for i in range(50):
    x = random.randrange(0, 1200)
    y = random.randrange(0, 640)
    snow_list.append([x, y])

b1 = stony()
b2 = stony()
b3 = stony()
b4 = stony()
b5 = stony()
b6 = stony()
allsprites = pygame.sprite.Group(b1, b2, b3, b4, b5, b6)
clock = pygame.time.Clock()
running = True
alien = pygame.mixer.Sound("alien.ogg")
alien.play(-1)  #背景音樂重複撥放
chstr = u"Time:"

track = pygame.mixer.Sound("hit.ogg")
over = pygame.mixer.Sound("gameover.ogg")
bread = pygame.mixer.Sound("break.ogg")
starttime = time.time()
while running:
    #清除螢幕
    screen.fill(black)
    endtime = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    for i in range(len(snow_list)):   
        # Draw the snow flake
        pygame.draw.circle(screen, white, snow_list[i], 2)
         
        # Move the snow flake down one pixel
        snow_list[i][1] += 1
         
        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 640:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 1200)
            snow_list[i][0] = x    
    
    outtime = downcount-(endtime-starttime)
    #me = unicode(outtime, "big5")
    printchar(chstr,None,green,1100,20,22)
    printchar(outtime,None,green,1150,20,22)  
    printchar("Score:",None,red,1100,40,22)
    printchar(count,None,red,1150,40,22)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and shiprect.right < rightborder:
        shiprect.centerx += mobile
    if keys[pygame.K_LEFT] and shiprect.left > leftborder:
        shiprect.centerx -= mobile
    if keys[pygame.K_DOWN] and shiprect.bottom < bottomborder:
        shiprect.centery += mobile
    if keys[pygame.K_UP] and shiprect.top > topborder:
        shiprect.centery -= mobile    
    
    if pygame.sprite.collide_rect(b1, b2):
        b1.dx *= -1
        b1.dy *= -1
        b2.dx *= -1
        b2.dy *= -1
        track.play()
    if pygame.sprite.collide_rect(b1, b3):
        b1.dx *= -1
        b1.dy *= -1
        b3.dx *= -1
        b3.dy *= -1
        track.play()
    if pygame.sprite.collide_rect(b1, b4):
        b1.dx *= -1
        b1.dy *= -1
        b4.dx *= -1
        b4.dy *= -1
        track.play() 
    if pygame.sprite.collide_rect(b1, b5):
        b1.dx *= -1
        b1.dy *= -1
        b5.dx *= -1
        b5.dy *= -1
        track.play() 
    if pygame.sprite.collide_rect(b1, b6):
        b1.dx *= -1
        b1.dy *= -1
        b6.dx *= -1
        b6.dy *= -1
        track.play()     
    if pygame.sprite.collide_rect(b2, b3):
        b2.dx *= -1
        b2.dy *= -1
        b3.dx *= -1
        b3.dy *= -1		
        track.play() 
    if pygame.sprite.collide_rect(b2, b4):
        b2.dx *= -1
        b2.dy *= -1
        b4.dx *= -1
        b4.dy *= -1		
        track.play() 
    if pygame.sprite.collide_rect(b2, b5):
        b2.dx *= -1
        b2.dy *= -1
        b5.dx *= -1
        b5.dy *= -1		
        track.play()
    if pygame.sprite.collide_rect(b2, b6):
        b2.dx *= -1
        b2.dy *= -1
        b6.dx *= -1
        b6.dy *= -1		
        track.play()    
    if pygame.sprite.collide_rect(b3, b4):
        b3.dx *= -1
        b3.dy *= -1
        b4.dx *= -1
        b4.dy *= -1		
        track.play()
    if pygame.sprite.collide_rect(b3, b5):
        b3.dx *= -1
        b3.dy *= -1
        b5.dx *= -1
        b5.dy *= -1		
        track.play()
    if pygame.sprite.collide_rect(b3, b6):
        b3.dx *= -1
        b3.dy *= -1
        b6.dx *= -1
        b6.dy *= -1		
        track.play() 
    if pygame.sprite.collide_rect(b4, b5):
        b4.dx *= -1
        b4.dy *= -1
        b5.dx *= -1
        b5.dy *= -1		
        track.play()
    if pygame.sprite.collide_rect(b4, b6):
        b4.dx *= -1
        b4.dy *= -1
        b6.dx *= -1
        b6.dy *= -1		
        track.play()
    if pygame.sprite.collide_rect(b5, b6):
        b5.dx *= -1
        b5.dy *= -1
        b6.dx *= -1
        b6.dy *= -1		
        track.play() 
    if outtime > 0:   
        if checkhit(b1,shiprect,15,25) == True:
            count = count +1 
            bread.play()
        if checkhit(b2,shiprect,15,25) == True:
            count = count +1
            bread.play()
        if checkhit(b3,shiprect,15,25) == True:
            count = count +1
            bread.play()
        if checkhit(b4,shiprect,15,25) == True:
            count = count +1
            bread.play()
        if checkhit(b5,shiprect,15,25) == True:
            count = count +1
            bread.play()
        if checkhit(b6,shiprect,15,25) == True:
            count = count +1
            bread.play()
    if outtime <= 0:  #代表遊戲時間結束
        printchar("YOUR SCORE:",None,(125,125,125),450,120,40)
        printchar(count,None,(200,125,200),660,120,40)
        printchar("GAMEOVER",None,bluegreen,450,320,60) 
        over.play()
        #femaleha = pygame.mixer.Sound("Femaleha.ogg")
        #femaleha.play()
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            pygame.quit()
			
    allsprites.clear(screen, background)
    allsprites.update()
    allsprites.draw(screen)
    screen.blit(shipimg, shiprect.topleft)
    pygame.display.update()
    clock.tick(15)

pygame.quit()