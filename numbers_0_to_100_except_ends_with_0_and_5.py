#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

print("all the numbers starting from 0 to 100 except numbers ending in zero or ending five")

for number in range(101):
    if number % 10 != 0 and number % 10 != 5:
        print(number)