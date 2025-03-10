#Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

print("Sum of all numbers")
number_list = []
for i in range(1, 11):
    number = (input(f"({i}) Enter a number: "))
    number = int(number)
    number_list.append(number)
    
result = sum(number_list)
    
print("The sum is:", result)