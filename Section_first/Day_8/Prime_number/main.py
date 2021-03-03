userInput = int(input("Write number: "))


def prime_checker(number):
    if number == 2 or number == 3 or number == 5:
        print(f"{number} is a prime number")
    if number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
        print(f"{number} is a prime number")


prime_checker(userInput)

print("********************")


def prime_checker_loop(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} It's a prime number.")
    else:
        print(f"{number} It's not a prime number.")    


prime_checker_loop(userInput)