# A Program to evaluate a 100 point quizzes that are graded on a scale
# 90-100-A , 80-89-B, 70-79-C, 60-69-D, <60-F


class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item) 

quiz_score = int(input("Please enter the result: "))
    
dict_values = RangeDict({range(90,101): 'A', range(80,90): 'B',range(70,80): 'C', range(60,70): 'D', range(0,61): 'F'})

print("The quiz result grade score is:",dict_values[quiz_score])

