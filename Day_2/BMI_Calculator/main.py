weight = float(input("What's your weight?\n"))
height = float(input("What's your height?\n"))

bmi = (weight / (height ** 2))

res = str(bmi)

print("Your BMI is: " + res)