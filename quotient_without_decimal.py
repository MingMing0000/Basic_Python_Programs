#Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

print("The quotient of two numbers without the decimal point")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

quotient = first_number // second_number
print(f"The quotient of the two numbers is {quotient}")