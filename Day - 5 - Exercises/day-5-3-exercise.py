print("Summation of all the even numbers from 1 to 100 \n")

sum_even = 0
for nos in range(1, 101):
    if nos % 2 == 0:
        sum_even += nos

# Using STEP method of range()

# for nos in range(2, 101, 2):
#     sum_even += nos

print("The total summation is : ", sum_even)
