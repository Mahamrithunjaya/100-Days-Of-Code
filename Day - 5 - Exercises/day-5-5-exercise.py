import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("WELCOME TO THE PY-PASSWORD GENERATOR .. !!!")
nos_letters = int(input("How many letters would you like to have in your password ? \n"))
nos_symbols = int(input("How many symbols would you like to have in your password ? \n"))
nos_numbers = int(input("How many numbers would you like to have in your password ? \n"))

# Eazy level - Order not randomised:

# password = ""
#
# for i in range(1, nos_letters + 1):
#     password += random.choice(letters)
#
# for i in range(1, nos_symbols + 1):
#     password += random.choice(symbols)
#
# for i in range(1, nos_numbers + 1):
#     password += random.choice(numbers)
#
#
# print("\nHere is your Password : " + password)


# Hard Level - Order randomised:

password_list = []

for i in range(1, nos_letters + 1):
    password_list.append(random.choice(letters))

for i in range(1, nos_symbols + 1):
    password_list.append(random.choice(symbols))

for i in range(1, nos_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print("\nHere is Your Password : " + password)
