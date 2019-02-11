from display import *
import math
#This is the equation of the line multiplied by two
#Keep A,B as the constants and multiply the x and the y by two so that we don't have floats
def twoDFunc(A,B):
    return 2 * A + B

def draw_line( x0, y0, x1, y1, screen, color ):
    dY = y1 - y0
    dX = x1 - x0
    #Starting at (x0,y1)
    currX = x0
    currY = y0
    #Constants
    a = y1 - y0
    b = -1 * (x1 - x0)
    #1st Octant
    if (((dY >= 0 and dX > 0)or (dY <= 0 and dX < 0)) and math.fabs(dY)<= math.fabs(dX)):
        twoD = twoDFunc(a,b)
        while(currX <= x1):
            plot(screen,color,currX,currY)
            if (twoD > 0):
                currY+=1
                twoD += 2 * b
            currX+=1
            twoD += 2 * a
    #2nd Octant
    if (((dY > 0 and dX >= 0)or (dY < 0 and dX < 0)) and math.fabs(dY)>math.fabs(dX)):
        twoD = twoDFunc(b,a)
        while(currY <= y1):
            plot(screen,color,currX,currY)
            if (twoD < 0):
                currX+= 1
                twoD += 2 * a
            currY += 1
            twoD += 2 * b
    #7th Octant
    if (math.fabs(dY) > math.fabs(dX) and ((dY < 0 and dX >= 0) or (dY >0 and dX <= 0))):
        twoD = twoDFunc(b,a)
        while(currY >= y1):
            plot(screen,color,currX,currY)
            if (twoD > 0):
                currX += 1
                twoD += 2 * a
            currY -= 1
            twoD += -2 * b

    #8th Octant
    if (math.fabs(dY) <= math.fabs(dX) and ((dY <= 0 and dX > 0) or (dY >=0 and dX < 0))):
        twoD = twoDFunc(-a,b)
        while(currX <= x1):
            plot(screen,color,currX,currY)
            if (twoD > 0):
                currY -=1
                twoD += 2 * b
            currX+= 1
            twoD += -2 * a
