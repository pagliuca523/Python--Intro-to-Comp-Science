from graphics import *

def main():

    win = GraphWin("Archery target", 400, 300)
    shape_circle = Circle(Point(200,140), 120)
    shape_circle.draw(win)
    shape_circle.setFill ("white")
    shape_circle = Circle(Point(200,140), 95)
    shape_circle.draw(win)
    shape_circle.setFill ("black")
    shape_circle = Circle(Point(200,140), 75)
    shape_circle.draw(win)
    shape_circle.setFill ("blue")
    shape_circle = Circle(Point(200,140), 55)
    shape_circle.draw(win)
    shape_circle.setFill ("red")
    shape_circle = Circle(Point(200,140), 35)
    shape_circle.draw(win)
    shape_circle.setFill ("yellow")

    win.getMouse()
    win.close()
main()