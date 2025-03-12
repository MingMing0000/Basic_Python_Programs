#Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#Create a list to store the numbers
numbers_list = []

#Ask user to input 10 numbers
for i in range(10):
    number_input = int(input("Enter a number: "))
    numbers_list.append(number_input)

#Create a list to store the numbers that have duplicate
duplicate_list = []

#Check if the number has duplicate
for i in range(10):
    if numbers_list.count(numbers_list[i]) > 1:
        duplicate_list.append(numbers_list[i])

#Display the numbers that have duplicate
print("Numbers that have duplicate: ", duplicate_list)