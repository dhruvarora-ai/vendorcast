number = int(input("Enter a number: "))
print(number)
#if we dont input a number but a str then it will show error
#so we use try except block to avoid error

try:
    number = int(input("Enter a number: "))
    print(number) #if input is int then it prints number
except: 
    print("Invalid input") #if input is not int then it prints this


try:
    value = 10/0 
    number = int(input("Enter a number: "))
    print(number) #if input is int then it prints number
except ZeroDivisionError: 
    print("Divided by zero") #if input is not int then it prints this
except ValueError:
    print("Invalid input")