#Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

print("The first number minus all of the remaining numbers")
number_list = []
for i in range(10):
    number = int(input("Enter a number: "))
    number_list.append(number)
