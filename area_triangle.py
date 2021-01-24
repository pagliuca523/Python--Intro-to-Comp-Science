import math

def main():

    a = float(input("Please input the A value: "))
    b = float(input("Please input the B value: "))
    c = float(input("Please input the C value: "))

    len_tri = (a + b + c) / 2
    calculus = len_tri*((len_tri - a)*(len_tri - b)*(len_tri - c))
    calculus = math.sqrt(calculus)

    print ("The result of an Triangle Area is: {}".format(calculus))

main()