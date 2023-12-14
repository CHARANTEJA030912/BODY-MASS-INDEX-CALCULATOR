def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: BMI = weight (kg) / (height (m))^2
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI categories
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        category = interpret_bmi(bmi)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are categorized as: {category}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numerical values.")

if __name__ == "__main__":
    main()
