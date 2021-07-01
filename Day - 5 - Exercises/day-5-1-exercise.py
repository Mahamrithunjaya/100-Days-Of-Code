students_heights = input("Input a list of student heights : ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

i = 0
heights_sum = 0
for heights in students_heights:
    heights_sum += heights
    i += 1

average_height = heights_sum / i

print("Average Height : ", round(average_height))

