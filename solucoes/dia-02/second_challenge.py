def calculator(): #defining the calculator function
    print('Simple calculator')
    print('Operators: +, -, *, /')

    #set a while loop in order to keep the calculator running until the user decide to stop using
    while True: 
        #receiving inputs from the user

        num1 = input('Enter the first number: ') 
        operator = input('Enter the operator you want to use: ')
        num2 = input("Enter the second number: ")

        #Making the coercion to float

        float_num1 = float(num1)
        float_num2 = float(num2)

        if operator == "+":
            result = float_num1 + float_num2
        elif operator == "-":
            result = float_num1 - float_num2
        elif operator == "*":
            result = float_num1 * float_num2
        elif operator == "/":
            if float_num2 != 0:
                result = float_num1 / float_num2
            else:
                print("Error: Division by zero!")
                continue
        
        print(f'Result: {result:.2f}')

        again = input("Do you want to calculate again? (yes/no): ")
        if again.lower() != "yes":
            break  # Exit the loop if the user doesn't want to continue

calculator()