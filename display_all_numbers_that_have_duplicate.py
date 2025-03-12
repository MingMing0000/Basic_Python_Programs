#Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#Create a list to store the numbers
numbers_list = []

#Ask user to input 10 numbers
for i in range(10):
    number_input = int(input("Enter a number: "))
    numbers_list.append(number_input)
