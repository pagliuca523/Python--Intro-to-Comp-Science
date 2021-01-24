from graphics import *

def main():

     #Intro
    print ("This program plots the growth of a 10-year investment.")

     #Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualizes interest rate: "))


    #Create a graphic window with labels on left edge
    
    win = GraphWin("Invetment Growth Chart",640,480)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1,0), ' 0.0K').draw(win)
    Text(Point(-1,2500), ' 2.5K').draw(win)
    Text(Point(-1,500), ' 5.0K').draw(win)
    Text(Point(-1,7500), ' 7.5K').draw(win)
    Text(Point(-1,10000), '10.0K').draw(win)

    #Draw a bar for initial principal
    
    bar = Rectangle(Point(0,0), Point(1,principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #Draw bars for sucessive years
    for year in range (1,11):
        #calculate value for the next year
        principal = principal * (1 + apr)
        #draw bar fot this value
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)


        input("Press <Enter> to quit ")
        win.close()


main()