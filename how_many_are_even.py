#Create a program that ask user to input 10 numbers. Print how many are even numbers.

print("how many are even numbers")
print("Enter 10 numbers: ")

even_numbers_count = 0
for i in range(10):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        even_numbers_count += 1
