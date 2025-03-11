#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

number_list = []

#Ask user to input a number until invalid
while True:
    try:
        number = int(input("Enter a number: "))
        number_list.append(number)
    except ValueError:
        break

#Display the number from lowest to highest
number_list.sort()
print("The numbers from lowest to highest:", number_list)