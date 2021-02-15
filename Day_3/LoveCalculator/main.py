print("Welcome to the love calculator program!")

first_name = input("Write the first name ")
second_name = input("Write the second name ")

newFirst = first_name.lower()
newSecond = second_name.lower()

first_number = newFirst.count("t")+ newFirst.count("r")+newFirst.count("u")+newFirst.count("e")+newFirst.count("l")+newFirst.count("o")+newFirst.count("v") 


first_str = str(first_number)

second_number = second_name.count("t") + second_name.count("r") + second_name.count("u") + second_name.count("e") + second_name.count("l") + second_name.count("o") + second_name.count("v")


second_str = str(second_number)

sum_str = first_str + second_str

final_num = int(sum_str)

if final_num < 10 or final_num > 90:
    print(f"Your score is {final_num}, you go together like coke and mentos")
elif final_num > 40 and final_num < 50:
    print(f"Your score is {final_num}, you are alright together")
else:
    "your score is {final_num}"