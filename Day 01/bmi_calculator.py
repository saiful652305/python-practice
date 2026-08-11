weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: " ))
BMI = float(weight / (height * height))
print(f"Your BMI is: {BMI: .2f}")