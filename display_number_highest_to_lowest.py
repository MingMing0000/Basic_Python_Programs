#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

print("Display the number from highest to lowest")
#Create a list to store the numbers
numbers_list = []

#Ask user to input a number
while True:
    try:
        number_input = int(input("Enter a number: "))
        numbers_list.append(number_input)
    except:
        break

#Display the number from highest to lowest
numbers_list.sort(reverse=True)
print("Number from highest to lowest: ", numbers_list)