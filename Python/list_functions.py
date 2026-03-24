lucky_numbers = [4,8,16,23,42]
friends = ["Kevin","Karen","Jim","Oscar","Toby"]

print(friends)
friends.extend(lucky_numbers) #adds one list at the end of another
print(friends)
friends.append("Dhruv") #adds an element to end of a list
print(friends)
friends.insert(1, "Kelly") #insert values in a list at a specific position
friends.remove("Jim")
print(friends)
print(friends.pop()) #removes last element
print(friends.index("Kelly")) #finds index of any value
print('''
''')
unlucky_numbers = [4,8,16,23,12]
print(friends.count("Jim"))
print(unlucky_numbers.sort())
print(unlucky_numbers)

#wap to store seven fruits in a list enetered by user
fruits=[]
for i in range(7):
    fruit = input("enter fruit name: ")
    fruits.append(fruit)
print(fruits)

#wap to enter marks of 6 students aand dsiplay them in sorted manner
marks = []
for i in range(6):
    mark = int(input(f"Enter marks of {i} student: "))
    marks.append(mark)
marks.sort()
print(marks)

#wap to sum a list with 4 number
x = [1,10,23,3]
sum = 0
for i in range(len(x)):
    sum = sum + x[i]
print("Sum of list elements is ", sum)

#wap to store seven fruits in a list enetered by user
fruits = []
for i in range(7):
    fruit = input("Enter fruit name: ")
    fruits.append(fruit)
print(fruits)

#wap to enter marks of 6 students aand dsiplay them in sorted manner
marks =  []
for i in range(6):
    mark  = input("Enter marks of student")
    marks.append(mark)
marks.sort()
print(marks)


#wap to sum a list with 4 number
list1= [2,5,7,1]
sum = 0
for list in list1:
    sum = sum + list1
print(sum)

