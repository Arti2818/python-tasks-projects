print("What is your name human")
name = input()


print("How old are you (in years)?")
age = int(input())

print("How tall are you (in meter)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = float(input())

bmi = weight / height ** 2

print(f"{name} you are {age} years old and your bmi is {bmi}. ")


