# A program to convert Celcius temps to Fahrenheit
# by : Raphael Pagliuca

def main():

    print("A program designed to converte Celcius to Fahrenheit")
    decision_making = (input("Would like to see a [t]able of conversion or just a [s]ingle conversion? "))
    if decision_making == 's':
        for i in range(5):
            celsius = eval(input("What is the Celcius Temperature? "))
            fahrenheit = 9/5 * celsius + 32
            print("The temperature is", fahrenheit, "degrees Fahrenheit")
    else:
        print("Celcius","|","Fahrenheit")
        for celsius in range(0,101,10):
            fahrenheit = 9/5 * celsius + 32
            print("  ",celsius,"  |",fahrenheit)
            
    print(input("Press <Enter> to quit."))

main()