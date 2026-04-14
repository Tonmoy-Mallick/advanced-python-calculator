
print(" Simple Calculator 🔢")

while True:
    print("\n--- New Calculation ---")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print(" Please enter valid numbers! ❌")
        continue

    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print(" Result ✅ :", num1 + num2)

    elif choice == '2':
        print(" Result ✅ :", num1 - num2)

    elif choice == '3':
        print(" Result ✅ :", num1 * num2)

    elif choice == '4':
        if num2 != 0:
            print(" Result ✅ :", num1 / num2)
        else:
            print(" Cannot divide by zero! ❌")

    else:
        print(" Invalid choice ❌")
        continue

    # Ask user to continue
    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again in ['yes', 'y']:
        continue
    elif again in ['no', 'n']:
        print("👋 Exiting calculator. Bye!")
        break
    else:
        print("❌ Invalid input, exiting for safety!")
        break
