#Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

print('Numbers between two numbers')
print("Enter two numbers to get all the numbers between them")

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print(f"Numbers between {first_number} and {second_number} are:")
if first_number < second_number:
  for i in range(first_number+1, second_number):
    print(i)
else:
  for i in range(second_number+1, first_number):
    print(i)