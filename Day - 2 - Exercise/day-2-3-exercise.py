age = input("Enter Your current Age : ")

age_as_int = int(age)

years_left = 90 - age_as_int

days = years_left * 365

weeks = years_left * 52

months = years_left * 12

message = f"You have left {days} days, {weeks} weeks and {months} months left"

print(message)

