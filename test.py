#THIS IS A BASIC CALCULATOR CREATED USING SIMPLE PYTHON PROGRAM.


# import math

# print("Is it a basic arithmetic procedure?")
# arithmetic = input("Yes or No: ").lower()

# if arithmetic == 'yes':
#     operand1 = float(input("Please enter the first digit: "))
#     operator = input("Please select the operator for the mathematical expression: ")
#     operand2 = float(input("Please enter the second digit: "))

#     if operator == '+':
#         result = operand1 + operand2
#         print(f"The result for the addition of {operand1} and {operand2} = {result}")
#     elif operator == '-':
#         result = operand1 - operand2
#         print(f"The subtraction between {operand1} and {operand2} = {result}")
#     elif operator == '*':
#         result = operand1 * operand2
#         print(f"The multiplication between {operand1} and {operand2} = {result}")
#     elif operator == '/':
#         result = operand1 / operand2
#         print(f"The division between {operand1} and {operand2} = {result}")
#     elif operator == '%':
#         result = operand1 % operand2
#         print(f"The modulus between {operand1} and {operand2} = {result}")
#     else:
#         print("Please enter a relevant mathematical operator.")

# else:
#     print("What mathematical procedure are we finding: power, exponential, sin, cosine, or tan of a value?")
#     math_operation = input("Enter procedure here: ").lower()

#     if math_operation == 'power':
#         operand3 = float(input("Enter the number to get the power for: "))
#         operand4 = float(input("What power do you want it to?: "))
#         power_result = math.pow(operand3, operand4)
#         print(f"{operand3} to the power of {operand4} = {power_result}")

#     elif math_operation == 'sin':
#         operand5 = float(input("Please enter the angle you want to find the sin for: "))
#         # Convert to radians first
#         radians_result = math.radians(operand5)
#         sine_value = math.sin(radians_result)
#         print(f"The sin of {operand5} degrees = {sine_value}")

#     elif math_operation == 'cosine':
#         operand6 = float(input("Please input the angle you want to find the cosine for: "))
#         # Convert to radians first
#         radians_result = math.radians(operand6)
#         cosine_value = math.cos(radians_result)
#         print(f"The cosine of {operand6} degrees = {cosine_value}")

#     elif math_operation == 'tan':
#         operand7 = float(input("Enter the angle to find the tan: "))
#         radians_result = math.radians(operand7)
#         tan_value = math.tan(radians_result)
#         print(f"The tangent of {operand7} degrees = {tan_value}")

#     elif math_operation == 'exponential':
#         exponential_number = float(input("Enter number to find exponential: "))
#         exponential_result = math.exp(exponential_number)
#         print(f"The exponential of {exponential_number} = {exponential_result}")

#     else:
#         print("Please select a valid option.")

import math

def main():
    while True:
        print("\nWelcome to the Python Calculator!")
        print("Are you performing a basic arithmetic procedure or a mathematical function?")
        choice = input("Enter 'arithmetic' for basic operations or 'math' for functions (or 'exit' to quit): ").lower()

        if choice == 'arithmetic':
            operand1 = float(input("Please enter the first number: "))
            operator = input("Please select the operator (+, -, *, /, %): ")
            operand2 = float(input("Please enter the second number: "))

            if operator == '+':
                result = operand1 + operand2
                print(f"The result of {operand1} + {operand2} = {result}")
            elif operator == '-':
                result = operand1 - operand2
                print(f"The result of {operand1} - {operand2} = {result}")
            elif operator == '*':
                result = operand1 * operand2
                print(f"The result of {operand1} * {operand2} = {result}")
            elif operator == '/':
                if operand2 != 0:
                    result = operand1 / operand2
                    print(f"The result of {operand1} / {operand2} = {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif operator == '%':
                result = operand1 % operand2
                print(f"The result of {operand1} % {operand2} = {result}")
            else:
                print("Invalid operator. Please enter a valid operator.")

        elif choice == 'math':
            print("Which mathematical procedure would you like to perform?")
            print("Options: power, exponential, sin, cosine, tan")
            math_operation = input("Enter procedure here: ").lower()

            if math_operation == 'power':
                base = float(input("Enter the base number: "))
                exponent = float(input("Enter the exponent: "))
                result = math.pow(base, exponent)
                print(f"{base} to the power of {exponent} = {result}")

            elif math_operation == 'sin':
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                result = math.sin(radians)
                print(f"The sine of {angle} degrees = {result}")

            elif math_operation == 'cosine':
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                result = math.cos(radians)
                print(f"The cosine of {angle} degrees = {result}")

            elif math_operation == 'tan':
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                result = math.tan(radians)
                print(f"The tangent of {angle} degrees = {result}")

            elif math_operation == 'exponential':
                number = float(input("Enter the number for exponential calculation: "))
                result = math.exp(number)
                
                print(f"The exponential of {number} = {result}")

            else:
                print("Invalid option. Please select a valid mathematical procedure.")

        elif choice == 'exit':
            print("Thank you for using the calculator. Goodbye!")
            break

        else:
            print("Invalid input. Please enter 'arithmetic', 'math', or 'exit'.")

if __name__ == "__main__":
    main()
