year = int(input("Which Year do you want to check?  "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The Year is a Leap Year. ")
        else:
            print("The Year is Not a Leap Year. ")
    else:
        print("The Year is Leap Year. ")
else:
    print("The Year is not a Leap Year. ")

