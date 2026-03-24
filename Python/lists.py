#list a data structure to organize different values together
#its mutable
friends = ["Kevin","Karen","Jim"] # we store multiple names under friends variable which represents a list

print(friends)

friends = ["kevin",2,"jan"]
print(friends)
print(friends[0]) #prints 1st element of list
print(friends[1]) #prints 2nd element of list
print(friends[-1]) #prints last element of list
print('''
''')
print(friends[1:]) #prints every element except 1st
employee = ["Sam","Harry","Martin","Jack","Henry"]
print('''
''')
print(employee[1:3]) #prints element with index 1,2

#modify values
employee[1] = "Mike"
print(employee[1])
