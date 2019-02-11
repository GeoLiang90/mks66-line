from display import *
from draw import *

screen = new_screen()
color = [ 255, 0, 0 ]
vals = []

i = 0
while i < 505:
    vals.append(i)
    i += 5
for x in vals:
    if x <= 250:
        color = [0,0,255]
        draw_line(x,0,250,500,screen,color)
        draw_line(x,500,250,0,screen,color)
    else:
        color = [0,255,0]
        draw_line(250,0,x,500,screen,color)
        draw_line(250,500,x,0,screen,color)
    color = [255,0,0]
    draw_line(0,250,500,x,screen,color)
    draw_line(0,x,500,250,screen,color)

'''
#Test Cases
#Octant 1
draw_line(250,250,500,250,screen,color)
draw_line(250,250,500,380,screen,color)
draw_line(250,250,500,500,screen,color)
#Octant 2
draw_line(250,250,380,500,screen,color)
draw_line(250,250,300,500,screen,color)
draw_line(250,250,250,500,screen,color)
#Octant 7
draw_line(250,250,400,0,screen,color)
draw_line(250,250,300,0,screen,color)
draw_line(250,250,350,0,screen,color)
draw_line(250,250,250,0,screen,color)
#Octant 8
draw_line(250,250,500,180,screen,color)
draw_line(250,250,500,120,screen,color)
draw_line(250,250,500,0,screen,color)

#Other tests
draw_line(0,250,250,250,screen,color)
draw_line(0,500,250,250,screen,color)
draw_line(0,0,250,250,screen,color)
draw_line(180,500,250,250,screen,color)
draw_line(0,300,250,250,screen,color)
draw_line(0,180,250,250,screen,color)
draw_line(100,0,250,250,screen,color)
'''
display(screen)
save_extension(screen, 'img.png')
