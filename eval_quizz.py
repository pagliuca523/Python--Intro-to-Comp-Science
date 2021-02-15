# A Program to evaluate a 5 point quizzes that are graded on a scale
# 5-A , 4-B, 3-C, 2-D, 1-F, 0-F

def main():

    quiz_score = int(input("Please enter the result: "))
    dict_values = {
        5:"A",
        4:"B",
        3:"C",
        2:"D",
        1:"F",
        0:"F" 
    }
    print("The quiz result grade score is:",dict_values[quiz_score])
    

main()
