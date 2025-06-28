#basic calculator for basic operation via python


num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
choice = input("Enter the operator (+ - * / % // **) : ")

if choice == '+':
    print(f"Addition : {num1 + num2}")
elif choice == '-':
    print(f"Subtraction : {num1 - num2}")
elif choice == '*':
    print(f"Multiplication : {num1 * num2}")
if choice == '/':
    print(f"Division : {num1 / num2}")
elif choice == '%':
    print(f"Remainder : {num1 % num2}")
elif choice == '//':
    print(f"floor division : {num1 // num2}")
elif choice == '**':
    print(f"Exponential : {num1 ** num2}")
else:
    print("Invalid input")
