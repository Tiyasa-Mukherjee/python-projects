# 6. Simple Calculator
# - Take two numbers and operation
# - Perform +, -, *, /, %
# - Keep history of calculations

def add(a,b):
    c = a+b
    return c
def subtract(a,b):
    c=a-b
    return c
def multiply(a,b):
    c=a*b
    return c
def divide(a,b):
    if b!=0:
        c=a/b
        return c
    else:
        return "Error: Division by zero is not allowed."
def modulus(a,b):
    if b!=0:
        c=a%b
        return c
    else:
        return "Error: Modulus by zero is not allowed."
history = []


while True:
    print("\n1. Press + to perform addition")
    print("2. Press - to perform subtraction")
    print("3. Press * to perform multiplication")
    print("4. Press / to perform division")
    print("5. Press % to perform modulus")
    print("6. Press H/h to view history")
    print("7. Press X/x to exit")

    op = input("Enter your choice : ")

    # ✅ Handle history
    if op.lower() == "h":
        if not history:
            print("No history yet.")
        else:
            print("History:")
            for i in history:
                print(i)
        continue

    # ✅ Handle exit
    elif op.lower() == "x":
        print("Exiting...")
        break

    # ✅ Handle operations
    elif op in ['+','-','*','/','%']:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

        if op == "+":
            result_value = add(num1, num2)
        elif op == "-":
            result_value = subtract(num1, num2)
        elif op == "*":
            result_value = multiply(num1, num2)
        elif op == "/":
            result_value = divide(num1, num2)
        elif op == "%":
            result_value = modulus(num1, num2)

        result = f"{num1} {op} {num2} = {result_value}"
        print(result)
        history.append(result)

    # ✅ Invalid input
    else:
        print("Invalid operation entered.")