# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

#Create a list to store the numbers
numbers_list = {}
#Ask user to input a number
while True:
    try:
        number_input = int(input("Enter a number: "))
        if number_input in numbers_list:
            numbers_list[number_input] += 1
        else:
            numbers_list[number_input] = 1
    except:
        break

#Find and display the number with the most number of duplicate
most_duplicate = max(numbers_list.values())
for number, count in numbers_list.items():
    if count == most_duplicate:
        print("Number with the most number of duplicate: ", number)
        break