row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map1 = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map1[vertical - 1]
selected_row[horizontal - 1] = "XX  "

# map1[vertical - 1][horizontal - 1] = "XX  "

print(f"{row1}\n{row2}\n{row3}")
