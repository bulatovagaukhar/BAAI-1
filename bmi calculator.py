
#Gaukhar
2024/11/6
#BMI calculator

def calculate_bmi():
    while True:
        # Taking input for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculating BMI
        bmi = weight / (height ** 2)
        print(f"Your BMI is: {bmi:.10f}")
        
        # Check if user wants to continue
        continue_choice = input("Continue? (yes/no): ").strip().lower()
        if continue_choice == "no":
            break

# Run the BMI calculator
calculate_bmi()
