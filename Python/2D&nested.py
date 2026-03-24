number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
] #in this list every element itself is a list

print(number_grid[0][0]) #1st element of 1st list of number grid list

#printing diagnol
for i in range (len(number_grid)):
    for j in range (len(number_grid[i])):
        if i==j:
            print(number_grid[i][i])

#also
for i in range(len(number_grid)):
    print(number_grid[i][i])    

#print whole list element 1 by 1
for row in number_grid:
    for element in row:
        print(element)


