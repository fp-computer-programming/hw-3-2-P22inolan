# Author: IBN (AMDG) 9/30/2021

weight = int(input("What is your weight in pounds? "))
height = int(input("What is your height in inches? "))

bmi = (weight / height / height) * 703

if bmi < 19:
    print("You are underweight.")
elif bmi <= 25:
    print("You are healthy.")
elif bmi <= 30:
    print("You are overweight.")
elif bmi <= 40:
    print("You are Obese.")
else:
    print("You are Extremely Obese.")
