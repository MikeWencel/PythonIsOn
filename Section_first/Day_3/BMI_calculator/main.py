print("Welcome to BMI Calculator version 2.0")
height = float(input("What's your heighit in m: "))
weight = float(input("What's your weight in kg: "))

result = weight / (height ** 2)

newRes = round(result,2)

print(newRes)

if result < 18.5:
    print("Underweight")
elif result > 18.5 and result < 25:
    print("Normal weight")
elif result > 25 and result < 30:
    print("Overweight")
elif result > 30 and result < 35:
    print("Obese")
else:
    print("Clinically obese")

