def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error while dividing zero"
    return a / b

def main():
    print("===CLI Calculator===")
    print("Available operations: add, substract, multiply, divide")

    operation = input("Enter opration: ").strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == "add":
        print("Result", add(a, b))
    elif operation == "substract":
        print("Result", substract(a, b))
    elif operation == "multiply":
        print("Result", multiply(a, b))
    elif operation == "divide":
        print("Result", divide(a, b))
    else:    
        print("Invalid operation")


if __name__ == "__main__":
    main()