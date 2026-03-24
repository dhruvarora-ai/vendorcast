num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
def calc(num1,num2):
    print("1.Add / 2.Subtract / 3.Multiply / 4. Divide")
    choice = int(input("Enter operation choice: "))
    if choice == 1:
        result = num1+num2
        print(num1,"+",num2,"is",result)
    elif choice == 2:
        result = num1 - num2
        print(num1,"-",num2,"is",result)
    elif choice == 3:
        result = num1*num2
        print(num1,"*",num2,"is",result)
    elif choice == 4: 
        result = num1/num2
        print(num1,"/",num2,"is",result)
    else:
        print("Invalid choice of operator")
calc(num1,num2)

