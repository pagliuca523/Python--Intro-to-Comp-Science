import math

def main():

    diameter = float(input("What is the diameter of the pizza?: "))
    price = float(input("Whats is the price of the pizza?: "))

    radius_pizza = diameter/2

    area_pizza = math.pi * (radius_pizza**2)

    price_per_inch = price / area_pizza

    print("Price per inch is {}".format(price_per_inch))

main()