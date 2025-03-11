#Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

print('Numbers between two numbers')
print("Enter two numbers to get all the numbers between them")

First_number = int(input("Enter first number: "))
Second_number = int(input("Enter second number: "))

for i in range(First_number+1, Second_number):
  print(i)