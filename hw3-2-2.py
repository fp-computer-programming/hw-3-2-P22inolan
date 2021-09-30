# Author: IBN (AMDG) 9/30/2021

weight = int(input("What is your weight? "))
height = int(input("What is your height? "))

bmi = (weight / height / height) * 703

if bmi < 19:
    print("You are underweight.")
elif bmi <=25 :
    print("You are healthy.")
