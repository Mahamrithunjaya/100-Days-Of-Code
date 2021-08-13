print("Welcome to the Tip Calculator \n")

bill = float(input("Enter your total Bill :  ₹"))
tip_percentage = int(input("What percentage tip would you like to give ? 10, 12 or 15 ? :  "))
split_bill = int(input("How many people to split the bill?  "))

tip_calc = (bill * (tip_percentage / 100))

total_bill = bill + tip_calc

share_bill = total_bill / split_bill

print("Each person should pay : ₹", round(share_bill, 2))

