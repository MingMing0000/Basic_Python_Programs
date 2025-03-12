#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

#Create a list to store the numbers
numbers_list = []

#Ask user to input a number
while True:
    try:
        number_input = int(input("Enter a number: "))
        numbers_list.append(number_input)
    except:
        break

#Display the highest number
print("\nHighest number: ", max(numbers_list))