
#BMI calculator

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height_int = float(height)
weight_int = float(weight)

bmi = weight_int/height_int**2

bmi_int = int(bmi)

print(bmi_int)