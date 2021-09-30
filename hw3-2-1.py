# Author: IBN (AMDG) 9/30/2021

grade = int(input("What is your GPA? "))

if grade < 60:
    print("You got an F.")
elif grade <= 64.999:
    print("You got a D. ")
elif grade <= 69.999:
    print("You got a D+.")
elif grade <= 72.999:
    print("You got a C-. ")
elif grade <= 76.999:
    print("You got a C.")
elif grade <= 79.999:
    print("You got a C+. ")
elif grade <= 82.999:
    print("You got a B-.")
elif grade <= 86.999:
    print("You got a B. ")
elif grade <= 89.999:
    print("You got a B+.")
elif grade <= 92.999:
    print("You got a A-.")
else:
    print("You got a A. ")
