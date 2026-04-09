@ -0,0 +1,31 @@
# simple_calculator.py
def calculator():
    print("\n--- Simple Calculator ---")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operation!")
            return
        
        print(f"\nResult: {num1} {op} {num2} = {result}")
    except ValueError:
        print("Invalid input! Please enter numbers.")

if __name__ == "__main__":
    calculator()