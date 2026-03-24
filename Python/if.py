#do this if this happens
cloudy = False
if cloudy == True: #if it meets the condition then python enters the statments under if
    print("Bring umbrella")
else: #if anything above is not correct then this runs
    print("Carry sunglasses")

if cloudy:
    print("Bring umbrella")
else: 
    print("Bring sunglasses")

is_male = True
is_tall = False
if is_male and is_tall:
    print("Handsome guy")
else:
    print("Ugly guy/girl")

is_male = True
is_tall = True  
if is_male or is_tall:
    print("You are either male or tall or both")
else:
    print("You are neither tall not male")

is_male = False
is_tall = True
if is_male and is_tall:
    print("Handsome guy")
elif is_male and not is_tall:
    print("You are Male and not tall")
elif not is_male and is_tall:
    print("You are tall and not male")
else:
    print("Ugly guy/girl")
print('''
''')
def max_num(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3 
print("Largest no is",max_num(8,9,1))


#wap to find greatest of 4 numbers entered by user
nums = []
for i in range(4):
    num = int(input("Enter a number: "))
    nums.append(num)
biggest = None
for number in nums:
    if biggest == None or number > biggest:
        biggest = number

        
print("Biggest number input is",biggest)

#Wap to find oit if a user has passed or failed
#It requires 40% in each subject and 33% overall to pass
#assume 3 subjects and take input from user
mark1 = int(input("Enter marks of user: "))
mark2 = int(input("Enter marks of user: "))
mark3 = int(input("Enter Marks of user: "))
overall = (mark1+mark2+mark3)/3
if mark1>=40 and mark2>=40 and mark3>=40 and overall>=33:
    print("You passed")
else:
    print("failed")

n = int(input("Enter no of subjects: "))
total = 0
for i in range(n):
    marks= int(input("Enter Marks in ",i+1,"subjects: "))
    total = total + marks
    if marks>40:
        if i==n-1:
            avg = total/n 
            if avg>=33:  
                print("you passed")
            else:
                print("You failed")
    else:
        print("you failed")
        break 
#wap to find if a given username has less than 10 character
username = input("Enter Username: ")
if len(username) >=10:
    print("Yes it has 10 or more char")
else:
    print("Username has less than 10 char")

#wap to find out if a given name is in a list or not
list_new = ["Dhruv","harry","carry","larry"]
name = "martin"
if name in list_new:
    print("Yes name exists in list")
else: 
    print("Name doesnt exist in list")


list_new = ["Dhruv","harry","carry","larry"]
name = input("Enter name to be searched: ")
count = 0
for word in list_new:
    word = word.lower()
    name = name.lower()
    if word == name:
        print("Yes name is in list")
        break
    elif count == len(list_new)-1:
        print("Name not in list")
    count = count+ 1

for word in list_new:
    if word.lower()==list_new.lower():
        print("Name is in the list")
        break
else:
    print("Not in the list")

#90-100;Ex 80-90;A , 70-80;B , 60-70;C , 50-60;D  <50;f

marks = int(input("Enter marks: "))
if marks>=90 and marks <=100:
    grade = "Ex"
elif marks >=80 and marks<90:
    grade = "A"
elif marks >=70 and marks<80:
    grade = "B"
elif marks>=60 and marks<70:
    grade = "C"
elif marks>=50 and marks<60:
    grade = "D"
elif marks<50:
    grade="F"
else:
    grade = "Invalid"
print(grade)