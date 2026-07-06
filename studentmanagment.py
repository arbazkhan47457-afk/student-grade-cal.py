# a simple python project that will helps student to calculate their grade

marks = int(input("Enter your marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter 0 to 100 only")
else:
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif marks >= 33:
        grade = "E - Pass"
    else:
        grade = "F - Fail"
    
    print(f"Your grade is: {grade}")