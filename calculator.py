num1 = float(input("Enter first number: "))
print("Which operation?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = input("Enter operation (1, 2, 3, 4): ")
num2 = float(input("Enter second number: "))

match operation:
    case "1":
        ans = num1 + num2
    case "2":
        ans = num1 - num2
    case "3":
        ans = num1 * num2
    case "4":
        ans = num1 / num2
    case _:
        print("Please choose a valid operation")

print("Your result is", ans)

while True:
    choice = input("Would you like to continue? (Y/N): ")
    if choice == "N":
        print("bye")
        break

    operation2 = input("Enter next operation (1, 2, 3, 4): ")
    num3 = float(input("Enter next number: "))

    match operation2:
        case "1":
            ans += num3
        case "2":
            ans -= num3
        case "3":
            ans *= num3
        case "4":
            ans /= num3
        case _:
            print("Please choose a valid operation")
    
    print("Your result is", ans)

        
