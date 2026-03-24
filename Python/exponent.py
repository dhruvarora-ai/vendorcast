print(2**3) #2 raise to power 3

def raise_to_power(base_num,pow_num): #power function
    result = 1 
    for i in range(pow_num):  #runs 3 times if pownum is 3
        result = result * base_num #performs the calculation
    return result  #returns the result

print(raise_to_power(2,5))

#using while loop
def raise_power(base_num,pow_num):
    result = 1
    i = 0
    while i<pow_num:
        result = result * base_num
        i= i+1
    return result
print(raise_power(2,5))