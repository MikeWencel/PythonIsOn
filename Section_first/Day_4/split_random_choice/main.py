import random

print("GAME - WHO WILL PAY!")

names_string = input("Write the names ")

list_names = names_string.split(",")

number = random.randint(1,5)

if number == 1:
    print(list_names[0])
elif number == 2:
    print(list_names[1])
elif number == 3:
    print(list_names[2])
else:
    print(list_names[3])


print(random.choice(list_names))


names = ["Denis","Borys", "Valav", "Shutkin", "Pushkin"]

num_of_names = len(names)

print(names[num_of_names - 1])