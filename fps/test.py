#Program: Simulation for Wagon wheel effect.

#Importing libraries
import math
from graphics import *


def main()->None:
    #Time for each frame
    frame_time = eval(input('Enter the time for each frame (1, 1/3, 2/3): '))

    #calculating the displacement angle in radians
    dis_angle:float = (frame_time * 360) * (math.pi / 180)

    win = GraphWin('Circle fps', 500, 500)
    #drawing the circle
    circle = Circle(Point(250, 250), 100)
    circle.draw(win)

    #Dot properties
    radius:int = 10
    x:int
    y:int
    x, y = 400, 250 #initial point
    angle = 0 #initial reference angle
    
    for i in range(100):
        #drawing the dot in reference angle
        circle_dot = Circle(Point(x , y), radius = 6)
        circle_dot.setFill('red')
        circle_dot.draw(win)
        
        #Updating the angle
        angle = angle + dis_angle
        
        #Updating the new x and y values
        x = circle.getCenter().getX() + (150 * math.cos(angle))
        y = circle.getCenter().getY() + (150 * math.sin(angle))
        
        print(x, y)
        time.sleep(0.25)
        circle_dot.undraw()
        
        
    input("")
    win.close()

    


main()
