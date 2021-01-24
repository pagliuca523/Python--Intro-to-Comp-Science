import math

def main():

    usr_num = int (input("Please insert which position would like to know: "))

    curr, prev = 1, 1
    for i in range(usr_num-2):
        curr, prev = curr+prev, curr


    print (curr)
main()