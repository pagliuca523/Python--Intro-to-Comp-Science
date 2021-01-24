import math

def main():


    #User interaction
    x1 = int(input("Please enter the first x value: "))
    x2 = int(input("Please enter the second x value: "))
    y1 = int(input("Please enter the first y value: "))
    y2 = int(input("Please enter the second y value: "))


    #calculus

    dif_x = x1 - x2
    dif_y = y1 - y2

    slope = dif_x / dif_y

    print("The slope is: {}".format(slope))
main()