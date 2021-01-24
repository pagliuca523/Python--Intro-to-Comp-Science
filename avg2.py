# av2.py
# A program to average three exam scores
#   Illustratesuse of multiple inputs

def main():
    print("This progrm computes the average of three exam scores.")

    score1, score2, score3 = eval(input("Enter three scores separate by a coma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is:", average)

main()