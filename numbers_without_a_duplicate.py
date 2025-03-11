#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

print("Enter 10 numbers")

numbers_list = []

for i in range(10):
    input_number = int(input("Enter number: "))
    numbers_list.append(input_number)

