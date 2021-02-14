print("Welcome to the Rollercoaster!")

bill = 0
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5 zloty")
    elif age <= 10:
        print("Youth tickets are 7 zloty")
        bill = 7
    else:
        print("Adult tickets are 12 zloty")
        bill = 12
        
    photo = input("Do you want a photo taken? Y or N ")
    if photo == "Y":
        bill += 3
    
    print(f"Your bill is {bill} zloty")
   


else:
    print("Sorry, you have to be taller to ride rollercoaster.")