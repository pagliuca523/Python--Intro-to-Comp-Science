import math

def main():

    print("Welcome to Konditorei Coffee Shop Order")

    #costs
    coffee_pnd = 10.50
    order_shipp = 0.86
    fixed_cost_shipp = 1.50

    #user interaction

    usr_tot_coffee = float(input("How many pounds of coffee you would like to order? "))

    cost_final = (usr_tot_coffee * coffee_pnd) + (order_shipp*usr_tot_coffee)+fixed_cost_shipp

    print ("Your cost to buy a coffee from us is: {}".format(cost_final))

main()