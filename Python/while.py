#runs till  condition is true

i = 1
while i<=10: #runs till this condition is true
    print(i)
    i = i+1
print("done")

#wap to print multiplication table of a given num using for loop
num = int(input("Enter number whose table you want: "))
for i in range(1,11):
    print(num,"X",i,"=",num*i)

#wap to greet all the person names stored in a list l which starts with S
l = ["Harry","Soham","Sachin","Rahul"]
for name in l:
    if name.startswith("S"):
        print("Good morning",name)
    else:
        continue

#wap to print multiplication table of a given num using while loop
i = 1
num2= int(input("Enter number whose table you want."))
while i<=10:
    print(num2,"X",i,num2*i)
    i = i+1

import math
#wap to find whether given num is prime or not
num3 = int(input("Enter number you want to check for prime: "))
for i in range(2,num3):
    if num3%i == 0:
        print("Not a prime no")
        break
else: 
    print("Prime number")

#wap to find sum of first n nat no in while
natural = 1
sum = 0
num = int(input("enter nth value"))
while natural<=num:
    sum = sum + natural
    natural = natural +1
print("Sum is",sum)

#factorial using for loop
fac = 1
num = int(input("Enter number for fac: "))
for i in range(1,num+1):
    fac = fac * i
print(fac)

#  *
# *** 
#*****
space =" "
n = 3
for i in range(1,n+1):
    print(" "*(n-i),)