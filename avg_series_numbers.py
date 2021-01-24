import math

def main():

    tot_numbers = int(input("Please insert the total of numbers, which wil be summed: "))

    tot = 0
    for i in range(tot_numbers):

        number = float(input("Please insert the number: "))
        tot += number /tot_numbers
    print("The total is: {}".format(tot))

main()