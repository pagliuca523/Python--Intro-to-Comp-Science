


#Progam to convert from a date ex: 05/04/2021 to April 05, 2021
def main():

    
    dayStr, monthStr, yearStr = str(input("Please insert the date (format: dd/mm/yyyy): ")).split("/") # USR input date format
    
    months = ("January","February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December") # list months names
    monthStr = months[int(monthStr)-1]

    print("The day converted is: {} {}, {}".format(monthStr,dayStr,yearStr))


main()
    