# EASY METHOD
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number - 1):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a Prime Number. ")
#     else:
#         print("It's not a Prime Number. ")


def prime_checker(number):
    num = number
    j = 0
    for i in range(1, number + 1):
        if num % i == 0:
            j += 1
    if j == 2:
        print("It's a Prime Number. ")
    else:
        print("It's not a Prime Number. ")


n = int(input("Check this number: "))
prime_checker(number=n)
