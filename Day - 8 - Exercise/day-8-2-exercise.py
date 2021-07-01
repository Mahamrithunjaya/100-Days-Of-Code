import math


def paint_calc(height, width, cover):
    nos_cans = (height * width) / cover
    print(f"You'll need {math.ceil(nos_cans)} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
