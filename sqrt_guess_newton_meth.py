import math

def main():

    sqrt_usr = float(input("Please input the desired number: "))
    n = int(input("How many interactions? "))
   

    
    guess = sqrt_usr / 2.0
    for i in range(n):
        guess = (guess + (sqrt_usr/guess))/2
    print("The diference between your guess and the actual number is {}".format(guess-math.sqrt(sqrt_usr)))
    print()
    print (guess,math.sqrt(sqrt_usr))


main()