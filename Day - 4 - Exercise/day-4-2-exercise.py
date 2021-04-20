import random


test_seed = int(input("Create a seed number : "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, separate by a comma : \n")
names = namesAsCSV.split(", ")

# Get the total number of items in list
list_length = len(names)

# Generate random numbers between 0 and the last item of the list
random_names = random.randint(0, list_length - 1)

print(f"{names[random_names]} is going to buy the meal today !! 😂😂😂😂😂😂")

