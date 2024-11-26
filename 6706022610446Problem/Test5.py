print("***Convert BMI***")
wei = int(input("Enter your weight (kg): "))
hei = int(input("Enter your height (m): "))

bmi = wei/(hei**2)
print(f"Your BMI is: {bmi:.5f}")