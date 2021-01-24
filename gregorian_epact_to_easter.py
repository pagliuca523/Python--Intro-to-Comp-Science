import math

def main():

    print("Gregorian Epact is the number of days between January 1st and the previous new moon. \nUsed to figure out the Easter date.")

    year = int(input("Please enter the Year: "))

    calculus = year // 100
    epact = (8+(calculus//4) - calculus + ((8*calculus + 13)//25) + 11 * (year % 19)) % 30


    print("The epact is: {} days".format(epact))
main()