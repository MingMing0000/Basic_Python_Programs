#Create a program that ask user to input 10 numbers. Print how many are odd numbers.

print("How many odd numbers are there?")
odd_numbers = []

for i in range(1, 11):
    number = int(input("Enter a number: "))
    if number % 2 != 0:
        odd_numbers.append(number)