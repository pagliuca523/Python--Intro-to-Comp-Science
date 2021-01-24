import math

def main():

    usr_num = int(input("Please input the number: "))

    tot = 0
    sgn = 1 #alternet the signal

    for i in range (1,2*usr_num,2):
        tot = tot + sgn * 4/i
        sgn = -sgn #flip the signal

    print ("Aprox to pi is: {} \nDifference from math.pi is: {}".format(tot,math.pi - tot))
    
main()