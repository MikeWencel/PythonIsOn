year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} It's a leap year")
    elif year % 400 == 0:
         print(f"{year} It's a leap year")   
    else:
        print(f"{year} It's not a leap year")        
else:
    print(f"{year} It's not a leap year")