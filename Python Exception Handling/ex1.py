def calculate_letter_grade(score):
    if 90 <= score <=100:
        return "A"
    elif 80 <= score <=89:
        return "B"
    elif 70 <= score <=79:
        return "C"
    elif 60 <= score <=69:
        return "D"
    else:
        return "F"
    

# Enter 1 - 100
# Out ò range == > error
# else print(grade)
# congratudation
    
try:
    grade = int(input("Enter grade from 0 - 100: "))
    letter = calculate_letter_grade(grade)
    if (0 > grade) or (grade >100):
        raise KeyError("grade must in range 0 to 100")
except KeyError as e:
    print(f"{e}")
else:
    print(f"grade: {letter}")
finally:
    print("thank for using")