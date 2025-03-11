#Create a program that ask user to input 2 numbers. Print the smaller number.

print("The smaller number")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number < second_number:
    print(f"the smaller number is {first_number}")
else:
    print(f"the smaller number is {second_number}")