import math

def main():

#User interaction
    x1 = int(input("Please enter the first x value: "))
    x2 = int(input("Please enter the second x value: "))
    y1 = int(input("Please enter the first y value: "))
    y2 = int(input("Please enter the second y value: "))


    calculus = ((x2 - x1)**2) + ((y2 - y1)**2)
    calculus = math.sqrt(calculus)

    print("The difference between two points is: {}".format(calculus))


main()