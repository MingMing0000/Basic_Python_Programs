#Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

print("Enter 10 numbers")

numbers_list = set()

for i in range(10):
    input_number = int(input("Enter number: "))
    numbers_list.add(input_number)

print(f"The Numbers are: {numbers_list}")