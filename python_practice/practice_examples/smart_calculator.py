history = []

def calculate():
    while True:
        print("\n--- Smart Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "6":
            break

        if choice == "5":
            print("\nHistory:")
            for h in history:
                print(h)
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = a + b
                operation = f"{a} + {b} = {result}"
            elif choice == "2":
                result = a - b
                operation = f"{a} - {b} = {result}"
            elif choice == "3":
                result = a * b
                operation = f"{a} * {b} = {result}"
            elif choice == "4":
                if b == 0:
                    print("Cannot divide by zero")
                    continue
                result = a / b
                operation = f"{a} / {b} = {result}"
            else:
                print("Invalid choice")
                continue

            print("Result:", result)
            history.append(operation)

        except:
            print("Invalid input")

calculate()