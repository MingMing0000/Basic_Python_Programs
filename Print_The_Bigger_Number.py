#Create a program that ask user to input 2 numbers. Print the bigger number.

print("print the bigger number")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number > second_number:
    print("The bigger number is: ", first_number)
else:
    print("The bigger number is: ", second_number)