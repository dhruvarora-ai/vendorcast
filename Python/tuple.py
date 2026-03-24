coordinates = ("Hello",2,4)
print(coordinates)
#tuples are immutable
print(coordinates[1])

coordinates = [(2,3),(4,5),(7,8)] #list of tuples

#wap to count the num of zeros in the tuple
x = (7,0,8,0,0,9)
print(x.count(0))

count=0
for i in x:
    if i == 0:
        count = count+1
print(count)

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