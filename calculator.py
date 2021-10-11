first_number = int(input("Please provide first_number:"))
second_number = int(input("Please provide second_number:"))
operation = input("Please state operation ("+", "-", "*" or "/")")

if operation == "+":
    print (first_number + second_number)
elif operation == "-":
    print (first_number - second_number)
elif operation == "*":
    print (first_number * second_number)
elif operation == "/":
    print (first_number / second_number)
else:
    print ("I can't complete this operation")

