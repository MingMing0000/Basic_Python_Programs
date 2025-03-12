# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

#Create a list to store the numbers
numbers_list = []

#Ask user to input a number
while True:
    try:
        number_input = int(input("Enter a number: "))
        numbers_list.append(number_input)
    except:
        break

#Create a list to store the numbers that have duplicate
duplicate_list = []

#Check if the number has duplicate
for i in range(len(numbers_list)):
    if numbers_list.count(numbers_list[i]) > 1:
        duplicate_list.append(numbers_list[i])