#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

print("Display the average")
#Create a list to store the numbers
numbers_list = []

#Ask user to input a number
while True:
    try:
        number_input = int(input("Enter a number: "))
        numbers_list.append(number_input)
    except:
        break

#Display the average
average = sum(numbers_list) / len(numbers_list)
print("Average: ", average)