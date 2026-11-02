def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def main():
    print("Simple Calculator (type 'q' to quit)")
    while True:
        try:
            first = input("\nFirst number: ").strip()
            if first.lower() == "q":
                break
            op = input("Operation (+, -, *, /): ").strip()
            if op.lower() == "q":
                break
            second = input("Second number: ").strip()
            if second.lower() == "q":
                break

            if op not in OPERATIONS:
                print("Invalid operation. Use +, -, * or /.")
                continue

            result = OPERATIONS[op](float(first), float(second))
            print(f"Result: {first} {op} {second} = {result:g}")
        except ValueError:
            print("Invalid number. Please try again.")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except (EOFError, KeyboardInterrupt):
            break
    print("Goodbye!")


if __name__ == "__main__":
    main()