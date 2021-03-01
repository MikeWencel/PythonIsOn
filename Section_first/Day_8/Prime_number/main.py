userInput = int(input("Write number: "))

if userInput == 2 or userInput == 3 or userInput == 5:
    print(f"{userInput} is a prime number")
    
if userInput % 2 != 0 and userInput % 3 != 0 and userInput % 5 != 0:
    print(f"{userInput} is a prime number")




