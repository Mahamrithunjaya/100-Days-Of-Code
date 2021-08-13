import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']

print("WELCOME TO THE PY-PASSWORD GENERATOR \n")
nos_letters = int(input("How many letters do you want to have in your password ? \n"))
nos_numbers = int(input("How many numbers do you want in your password ? \n"))
nos_symbols = int(input("How many symbols do you want in your password ? \n"))

# Easy Level - Order not Randomised

# password = ""
# for letter in range(1, nos_letters + 1):
#     password += random.choice(letters)
#
# for number in range(1, nos_numbers + 1):
#     password += random.choice(numbers)
#
# for symbol in range(1, nos_symbols + 1):
#     password += random.choice(symbols)
#
# print("\nHere is Your Password : " + password)


# Hard Level - Order Randomised

password_list = []
for letter in range(1, nos_letters + 1):
    password_list.append(random.choice(letters))

for symbol in range(1, nos_symbols + 1):
    password_list.append(random.choice(symbols))

for number in range(1, nos_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password_final = ""
for passcode in password_list:
    password_final += passcode

print("Here is your Password : ", password_final)
