import math

def main():

    height = float(input("Please input the Height: "))
    angle_ladder = float(input("Please input the Angle in Degrees: "))

    #Convert degrees to radians

    radians = (math.pi/180)*angle_ladder

    len_ladder = height / math.sin(radians)

    print(radians)
    print("The total lenght required is: {}".format(len_ladder)) 

main()