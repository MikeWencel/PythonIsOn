student_heights = [183, 183, 165, 189, 169, 159, 192]
res = 0

for height in student_heights:
    res += height / len(student_heights)

final = round(res,2) 
print(final)    