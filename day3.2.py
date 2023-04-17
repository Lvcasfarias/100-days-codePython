print("Welcome to BMI calculator 2.0")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height *2) 
if bmi <= 18.5:
    print(f"You are {bmi} ", "\033[1m" + "underweight" + "\033[0m")
elif bmi >= 18.5 and bmi <= 25:
    print(f"You are ", "\033[1m" + "normal weight" + "\033[0m")
elif bmi >= 25 and bmi <= 30:
    print(f"You are {bmi} ", "\033[1m" + "overweight" + "\033[0m")
elif bmi >= 35:
    print(f"You are {bmi} ", "\033[1m" + "clinically obese" + "\033[0m")