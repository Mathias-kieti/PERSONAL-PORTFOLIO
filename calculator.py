num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operater = input("Enter the operator to use: ")

if operater == "+":
    answer = num1 + num2
    print(f"The result for num1 + num2 is: {answer}" )
elif operater == "-":
    answer = num1 - num2  
    print(f"The result for num1 - num2 is: {answer}" )
elif operater == "*":
    answer = num1 * num2 
    print(f"The result for num1 * num2 is: {answer}" )
elif operater == "/":
    answer = num1 / num2
    print(f"The result for num1 / num2 is: {answer}" )
else:
    print("Invaid operator,  Please enter +, -, *, or /.")




