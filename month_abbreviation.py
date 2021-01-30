#Program to show a short name for months

def main():

    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    usr_month = int(input("Please enter the month number (1-12): "))
    usr_month = ((usr_month -1) * 3)

    month_abbrev = months [usr_month:usr_month+3]

    print("Month: {}".format(month_abbrev))
main()