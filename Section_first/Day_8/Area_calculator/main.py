import math
print("Paint calculator")


can_yield = 5
# 1 can = 5 sq meter

height = int(input("What is height of the wall: "))
width = int(input("What is width of the wall: "))

squere_meters = height * width

print(f"There is {squere_meters} squere meters")

cans = squere_meters / can_yield

cans = math.ceil(cans)

print(f"use {cans} cans")