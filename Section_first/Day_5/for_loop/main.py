import random

fruits = ["Apple","Peach","Ananas"]

for fruit in fruits:
    print(fruit)

numbers_list = []
number = 0  
for x in range (1,6):
    number = random.randint(1,48)
    numbers_list.append(number)

    
print(numbers_list)     