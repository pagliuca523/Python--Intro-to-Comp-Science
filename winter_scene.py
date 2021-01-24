from graphics import *

def main():

    win = GraphWin("Winter Scene", 400,300)
    win.setBackground (color_rgb(225,231,228))

    #Snowman
    head = Circle(Point(100,150),25)
    head.setFill(color_rgb(239,222,215))
    head.draw(win)
    body = Circle(Point(100,215),40)
    body.setFill(color_rgb(239,222,215))
    body.draw(win)
    eye_left = Circle(Point(90,145),2)
    eye_left.setFill(color_rgb(0,0,0))
    eye_left.draw(win)
    eye_right = Circle(Point(113,144),2)
    eye_right.setFill(color_rgb(0,0,0))
    eye_right.draw(win)
    nose_up = Line(Point(100,150),Point(110,155))
    nose_up.setFill(color_rgb(0,0,0))
    nose_up.draw(win)
    nose_down = Line(Point(101,159),Point(110,155))
    nose_down.setFill(color_rgb(0,0,0))
    nose_down.draw(win)


    win.getMouse()
    win.close()

main()