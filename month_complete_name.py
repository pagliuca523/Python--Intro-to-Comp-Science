#Program to show a long name for months

def main():

    months = ("January","February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    usr_month = int(input("Please enter the month number (1-12): "))
    usr_month = usr_month -1
    #print(type(months)) -- Tuple
    print(months[usr_month])
main()