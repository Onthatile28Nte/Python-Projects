print("==================== PYTHON CALCULATOR ===================")


while True:
    
    math_sign = input("Choose a sign (+, -, /, //, %, *, **) or q to quit: ")
    
    if math_sign.lower() == "q":
        break
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
        
    
    if math_sign == "+":
        print(f"Your answer is {num1 + num2}")
        
    elif math_sign == "-":
        print(f"Your answer is {num1 - num2}")
        
    elif math_sign == "/":
        if num2 == 0:
            print("Denominator cannot be zero.")
        else:
            print(f"Your answer is {num1 / num2}")
    elif math_sign == "//":
        print(f"Your answer is {num1 // num2}")
    elif math_sign == "%":
        print(f"Your answer is {num1 % num2}")
        
    elif math_sign == "*":
        print(f"Your answer is {num1 * num2}")
        
    elif math_sign == "**":
        print(f"Your answer is {num1 ** num2}")
    else:
        print("Invalid Operator. Please try again.")

