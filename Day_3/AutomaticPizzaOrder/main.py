print("Welcome to automatic pizza center!")
size = input("What's size of pizza do you want? S, M or L ")
bill = 0
if size == "L":
    bill = 25
    #Pepperoni    
    peper = input ("Do you want extra peperoni? Y or N ")
    if peper == "Y":
        bill += 3
    #Cheese        
    cheese = input("Do you want extra cheese? Y or N ")
    if cheese == "Y":
        bill += 1
        print(f"Your final bill is: {bill}")
    else:
        print(f"Your final bill is: {bill}")
        
elif size == "M":
    bill = 20    
#Pepperoni    
    peper = input ("Do you want extra peperoni? Y or N ")
    if peper == "Y":
        bill += 3
#Cheese        
    cheese = input("Do you want extra cheese? Y or N ")
    if cheese == "Y":
        bill += 1
        print(f"Your final bill is: {bill}")
    else:
        print(f"Your final bill is: {bill}")

elif size == "S":
    bill = 15
#Pepperoni    
    peper = input ("Do you want extra peperoni? Y or N ")
    if peper == "Y":
        bill += 2
#Cheese        
    cheese = input("Do you want extra cheese? Y or N ")
    if cheese == "Y":
        bill += 1
        print(f"Your final bill is: {bill}")
    else:
        print(f"Your final bill is: {bill}")
else:
    print("Wrong answer!")

          