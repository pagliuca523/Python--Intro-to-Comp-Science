# simple program to show a chaotic environment

def main():
    print ("This program illustrate a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print (x)
main()