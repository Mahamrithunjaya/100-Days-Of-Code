height = input("Enter your height in metres :   ")
weight = input("Enter your weight in kilograms :   ")

float_height = float(height)
int_weight = int(weight)

# bmi = (int_weight / (float_height * float_height))
bmi = int_weight / float_height ** 2

result = int(bmi)

print("Your BMI is :   ", result)
