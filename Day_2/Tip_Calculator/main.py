print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? PLN "))
percent_of_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split? "))

tip = ((percent_of_tip/100* bill + bill) / people)
#round to TWO decimal points round(var,'How many decimal points?')
answer = round(tip,2)

print(f"Each person should pay: {answer} zł")