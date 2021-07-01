print("Welcome to the Roller Coaster Ride !!! \n")

height = int(input("What is your height in CM :  "))
bill = 0

if height >= 120:
    print("You can Ride Roller Coaster...")

    age = int(input("What is your Age ?  "))

    if age < 12:
        bill = 5
        print("Child Tickets are ₹5.")
    elif age <= 18:
        bill = 7
        print("Youth Tickets are ₹7.")
    elif 45 <= age <= 55:
        print("Your Ticket is Free..")
    else:
        bill = 12
        print("Adult Tickets are ₹12.")

    want_photos = input("Do you want to take Photos? Y or N :  ")
    if want_photos == "Y":
        bill += 3

    print(f"Your final Ticket Bill is ₹{bill}")

else:
    print("Sorry, You have to grow taller before you can Ride Roller Coaster.. \nHave A Good Day... \nThank You....")

