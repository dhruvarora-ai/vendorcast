for letter in "Girrafe Academy": #for loop iterates through this string
    print(letter)

friends = ["Harry","King","Maam"]
for friend in friends:
    print(friend)

for i in range(10):
    print(i)
for i in range(1,12):
    print(i)
for i in range(1,10,2): #1-9 with diff of 2
    print(i)


#recurssion  fac
def factorial(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num* factorial(num-1)
print("Factorial of 5",factorial(5))

def fac(num):
    if num ==0 or num ==1:
        return 1
    else:
        return num*fac(num-1)
print(fac(3))

#sum and avg of n numbers entered by user
n = int(input("Enter number: "))
sum=0
for i in range(n):
    value = int(input("Enter value: "))
    sum = sum + value
print(sum)
print("avg: ",sum/n)


