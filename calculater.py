def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice not in ['1', '2', '3', '4']:
    print("Invalid choice. Please select a valid operation.")
elif choice == '5':
    print("Exiting the calculator.")
elif choice == '6':
    print("Calculator is in debug mode.")
    print("Debugging information:")
    print(f"Choice: {choice}, Num1: {num1}, Num2: {num2}")
elif choice == '5':
    print("Exiting the calculator.")    
else:
    print("Invalid input")

