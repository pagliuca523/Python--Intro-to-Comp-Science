#futval.py
#A program designed for calculates the future value of a 10-year investment

def main():

    
    print("This program was designed to calculates a future value in X years of investment")
    quartely_interest = 4
    
    #Inputs 
    years = eval(input("Years: "))
    principal = eval(input("Enter the initial amount: "))
    y_reinvest = (eval(input("Enter a total year by year reinvestment: ")))
    apr = eval(input("Enter the apr , use decimal numbers: "))

    if y_reinvest <= 0:

        for i in range(years):
            fv = (principal * (1 + (apr/quartely_interest))**(years*quartely_interest))
        print("Total value in ",years,"years:",fv)
        #(y_reinvest * ((1+ (apr/quartely_interest))**(years*quartely_interest)-1)/(apr/quartely_interest))
    else:
        for i in range(years):
            fv = (principal * (1 + (apr/quartely_interest))**(years*quartely_interest))

            fv_reinvest = fv + y_reinvest * ((1+ (apr/quartely_interest)) ** ((years*quartely_interest)-1) / (apr/quartely_interest))
            tot = fv  fv_reinvest

        print("Total value in ",years,"years:",tot,fv_reinvest)

main()                                                                                                