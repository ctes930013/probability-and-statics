# -*- coding: utf-8 -*-
"""
Created on Tue May 17 20:37:53 2016

@author: user
"""

#程式執行須按兩下run file

import turtle

wn=turtle.Screen()
#先將輸出畫面顯示

wn.bgcolor("black")
#背景設為黑色

wn.title("機統HW")
#定義標題

alex = turtle.Turtle()

alex.color("blue")

alex.forward(340)

alex.right(90)

alex.forward(280)

alex.clear()

alex.left(180)

alex.color("blue")

alex.speed(1)
for i in range(15):
    alex.begin_fill()    
    alex.circle(25,180)    
    alex.end_fill()    
    alex.left(180)
    
#alex為下圖奇怪的波浪    
  
tess = turtle.Turtle()

tess.color("#FFFF33")

tess.speed(1)

tess.right(90)

tess.clear()

tess.right(90)

tess.forward(140)

tess.right(90)

tess.forward(200)

tess.clear()

tess.begin_fill()

tess.circle(60,360)

tess.end_fill()
tess.left(90)
tess.forward(10)

#tess為滿月

cess = turtle.Turtle()

cess.color("black")

cess.speed(1)

cess.left(180)

cess.forward(140)

cess.right(90)

cess.forward(200)

cess.clear()

cess.begin_fill()

cess.circle(55,360)

cess.end_fill()  

#cess為天狗食月

six = turtle.Turtle()

six.color("#880000")

six.left(60)

six.forward(90)

six.forward(150)

six.clear()

six.speed(1)

six.left(30)

for i in range(3):
    six.right(90)
    for i in range(5):
        six.forward(100)
        six.right(144)
    six.left(90)    
    six.forward(5)    
    
#six為六芒星    
    
pj = turtle.Turtle()

pj.color("blue")   

pj.speed(1)

pj.left(180)

pj.forward(80)

pj.left(90)

pj.forward(45)

pj.right(180)

pj.clear()
    
pj.circle(120,360)

pj.circle(60,180)

pj.left(180)

pj.circle(-60,180)

pj.circle(-120,180)

pj.left(180)

pj.circle(60,180)  

pj1 = turtle.Turtle()

pj1.color("#FF3EFF")   

pj1.speed(1)

pj1.left(180)

pj1.forward(80)

pj1.left(90)

pj1.forward(45)

pj1.right(90)

pj1.forward(25)

pj1.right(90)

pj1.clear()

pj1.begin_fill()

pj1.circle(30,360)

pj1.end_fill()

pj1.left(90) 

pj1.forward(15)  

pj2 = turtle.Turtle()

pj2.color("#BBFFEE")   

pj2.speed(1)

pj2.left(180)

pj2.forward(80)

pj2.left(90)

pj2.forward(45)

pj2.right(90)

pj2.forward(155)

pj2.right(90)

pj2.clear()

pj2.begin_fill()

pj2.circle(30,360)

pj2.end_fill()

pj2.left(90) 

pj2.forward(15)

#pj1 pj2 pj為太極

house_ridge = turtle.Turtle()

house_ridge.color("#DDDDDD")

house_ridge.speed(1)

house_ridge.forward(160)

house_ridge.left(90)

house_ridge.forward(120)

house_ridge.left(135)

house_ridge.clear()

house_ridge.begin_fill()

house_ridge.forward(220)

house_ridge.left(90)

house_ridge.forward(25)

house_ridge.left(90)

house_ridge.forward(202)

house_ridge.right(90)

house_ridge.forward(202)

house_ridge.left(90)

house_ridge.forward(25)

house_ridge.left(90)

house_ridge.forward(220)

house_ridge.end_fill()

#house_ridge為房子屋脊

house_arc = turtle.Turtle()

house_arc.color("#CC6600")

house_arc.speed(1)

house_arc.forward(40)

house_arc.right(90)

house_arc.forward(40)

house_arc.clear()

house_arc.begin_fill()

house_arc.forward(200)

house_arc.left(90)

house_arc.forward(255)

house_arc.left(90)

house_arc.forward(200)

house_arc.left(45)

house_arc.forward(183)

house_arc.left(90)

house_arc.forward(183)

house_arc.left(135)

house_arc.forward(30)

house_arc.end_fill()

#house_arc為房子底層結構

house_window = turtle.Turtle()

house_window.color("#FF0000")

house_window.forward(70)

house_window.speed(1)

house_window.right(90)

house_window.forward(45)

house_window.clear()

house_window.begin_fill()

for i in range(4):
    
    house_window.forward(95)
    house_window.left(90)
    
house_window.end_fill()    
      
house_window.forward(30)

house_window.left(90)

house_window.forward(30) 

#house_window為房子窗戶   

house_ws = turtle.Turtle()

house_ws.color("black")

house_ws.pensize(4)

house_ws.forward(70)

house_ws.speed(1)

house_ws.right(90)

house_ws.forward(92.5)

house_ws.clear()

house_ws.left(90)

house_ws.forward(95)

house_ws.forward(-47.5)

house_ws.left(90)

house_ws.forward(47.5)

house_ws.forward(-95)

house_ws.forward(47.5)

#house_ws.為窗戶溝朝

house_door = turtle.Turtle()

house_door.color("#886600")

house_door.forward(180)

house_door.speed(1)

house_door.right(90)

house_door.forward(70)

house_door.clear()

house_door.begin_fill()

house_door.forward(170)

house_door.left(90)

house_door.forward(70)

house_door.left(90)

house_door.forward(170)

house_door.left(90)

house_door.forward(70)

house_door.end_fill()

house_door.left(90)

house_door.forward(30)

house_door.left(90)

house_door.forward(30)

#house_door為房子的門

house_chimney = turtle.Turtle()

house_chimney.color("#AAAAAA")

house_chimney.left(90)

house_chimney.forward(70)

house_chimney.right(90)

house_chimney.forward(280)

house_chimney.speed(1)

house_chimney.clear()

house_chimney.right(90)

house_chimney.begin_fill()

house_chimney.forward(60)

house_chimney.right(180)

house_chimney.forward(60)

house_chimney.right(90)

house_chimney.forward(35)

house_chimney.right(90)

house_chimney.forward(95)

house_chimney.right(135) 

house_chimney.forward(50)

house_chimney.end_fill()

house_chimney.forward(-20)

house_chimney.right(90)

house_chimney.forward(16)

#house_chimney為房子煙囪
    
wn.mainloop()