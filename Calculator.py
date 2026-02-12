print("==================== PYTHON CALCULATOR ===================")

math_sign = input("Choose a sign (+, -, /, //, %, *, **): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

while True:
    if math_sign == "+":
        print(f"Your answer is {num1 + num2}")
    if math_sign == "-":
        print(f"Your answer is {num1 - num2}")
    if math_sign == "/":
        if num2 == 0:
            print("Denominator cannot be zero.")
    print(f"Your answer is {num1 / num2}")
    if math_sign == "//":
        print(f"Your answer is {num1 // num2}")
    if math_sign == "%":
        print(f"Your answer is {num1 % num2}")
    if math_sign == "*":
        print(f"Your answer is {num1 * num2}")
    if math_sign == "**":
        print(f"Your answer is {num1 ** num2}")
        

