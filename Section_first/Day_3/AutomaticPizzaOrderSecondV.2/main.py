print("Welcome to automatic pizza center!")
size = input("What's size of pizza do you want? S, M or L ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25        

peper = input ("Do you want extra peperoni? Y or N ")
if peper == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or "L":
        bill += 3

cheese = input("Do you want extra cheese? Y or N ")
if cheese == "Y":
    bill += 1

print(f"Your final bill is: {bill}")