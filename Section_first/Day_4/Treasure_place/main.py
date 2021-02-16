row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1, row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("wgere do you want to put the treasure ")

pos_split = position.split(",")

first = pos_split[0]
second = pos_split[1]

if first == "0":
    if second == "0":
        map[0][0] = "X"
    if second == "1":
        map[0][1] = "X"
    if second == "2":
        map[0][2] = "X"    
elif first == "1":
    if second == "0":
        map[1][0] = "X"
    if second == "1":
        map[1][1] = "X"
    if second == "2":
        map[1][2] = "X"   
elif first == "2":
    if second == "0":
        map[2][0] = "X"
    if second == "1":
        map[2][1] = "X"
    if second == "2":
        map[2][2] = "X"   


print(f"{row1}\n{row2}\n{row3}")