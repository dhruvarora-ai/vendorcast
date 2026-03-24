employee_file = open("employee.txt","r") #filename, mode of opening file(r-read)
'''
a-append
r-read
r+ read append
'''
print(employee_file.readable()) #tells if readable or not

# print(employee_file.read()) #read the file

print(employee_file.readline()) #reads first line
print(employee_file.readline()) #2nd line

print(employee_file.readlines()[1]) #each line becomes a list element
employee_file.close()

employee_file = open("employee.txt","r")
for employee in employee_file.readlines():
    print(employee)








