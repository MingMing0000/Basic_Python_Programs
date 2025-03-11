#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

print('Numbers that don\'t have duplicate')
print("Enter 10 numbers")

number_list = []

for i in range(10):
    number = int(input("Enter a number: "))
    number_list.append(number)

