#Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

number_list = []
#Ask user to input a number until invalid
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)
    except ValueError:
        break

