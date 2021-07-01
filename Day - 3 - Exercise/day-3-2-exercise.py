height = float(input("Enter your height in Metres (m):  "))
weight = float(input("Enter your weight in Kilograms (kg):  "))

bmi = weight / height ** 2
bmi_result = round(bmi, 2)

if bmi_result < 18.5:
    print(f"Your BMI is -> {bmi_result}, You are Underweight")
elif bmi_result < 25:
    print(f"Your BMI is -> {bmi_result}, You have a Normal weight")
elif bmi_result <30:
    print(f"Your BMI is -> {bmi_result}, You are slightly Overweight")
elif bmi_result < 35:
    print(f"Your BMI is -> {bmi_result}, You are Obese")
else:
    print(f"Your BMI is -> {bmi_result}, You are Clinically Obese")

