num1 = float(input("Enter first number: "))
print("Which operation?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = input("Enter operation (1, 2, 3, 4): ")
num2 = float(input("Enter second number: "))

if operation == "1":
    ans = num1 + num2
elif operation == "2":
    ans = num1 - num2
elif operation == "3":
    ans = num1 * num2
else:
    ans = num1 / num2

print("Your result is", ans)

while True:
    choice = input("Would you like to continue? (Y/N): ")
    if choice == "N":
        print("bye")
        break

    operation2 = input("Enter next operation (1, 2, 3, 4): ")
    num3 = float(input("Enter next number: "))

    if operation2 == "1":
        ans += num3
    elif operation2 == "2":
        ans -= num3
    elif operation2 == "3":
        ans *= num3
    elif operation2 == "4":
        ans /= num3
    
    print("Your result is", ans)

        
