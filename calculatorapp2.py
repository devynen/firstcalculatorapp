#my simple calculator app

print("""1. Addition
2. Subtracttion"
3. Multiplication"
4. Division"
""")
#prompt user for input
print("Enter two numbers to add")
first_number=float(input("Enter first Number:"))
second_number=float(input("Enter Second Number:"))

#for Addition operation
sum = first_number + second_number
print(f"{first_number} + {second_number} = {sum}")

#prompt user for input
print("Enter two to perform subtraction")
first_number=float(input("Enter first Number:"))
second_number=float(input("Enter Second Number:"))

#for Subtration operation
answer = first_number - second_number
print(f"{first_number} + {second_number} = {answer}")



