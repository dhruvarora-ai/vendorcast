employee_file = open("employee.txt","a")
employee_file.write("\nKelly - Customer service")
employee_file.close()

employee_file = open("employee.txt","w")
#write clears the file and then adds text
employee_file.write("This is new file")

#1
poems_read = open("poems.txt","r")
f= poems_read.read()
if "twinkle" in f:
    print("true")
else:
    print("False")

#2
