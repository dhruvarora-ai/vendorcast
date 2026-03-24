print("Anything inside double quotations is a string")

print("Hello \nWorld") #newline after \n

phrase = "Animal academy"
print(phrase)

#String concatenation
print(phrase + " is cool")

#string functions
print(phrase.lower()) #all become lower
print(phrase.upper()) #all become upper
print(phrase.isupper()) #gives true or false
print(phrase.islower())
print(phrase.upper().isupper())

new_str = "Barber  Good"
print(len(new_str))
print(new_str[0])
print(new_str[0:4])
print(new_str.index("e")) #gives index of e
print(new_str.replace("Good","Bad")) #replaces words 

print("  " in new_str)
print(new_str.index("  "))
print(new_str.replace("  ","   "))


print('''
''')
print("Anything inside a quotation is string")
print("Hello \nworld")
phrase = "Giraffe Academy"
print(phrase + " is cool") #string concatenation
print(phrase.lower()) #all in lower
print(phrase.upper()) # all in upper
print(phrase) #shows that string is immutable
print(phrase.isupper()) #checks if all letters are uppercase
print(len(phrase),"length of variable value") 
print(phrase.find("y")) #finds index of y
print(phrase.index("G")) #gives index value of G
print(phrase.replace("G","K"))
print(phrase)

#wap to display a user entered name followed by good afternoon using input
name = input("Enter name: ")
print(f"Good morning, {name} ")
print("Good afternoon, "+name)

#problem 2
letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>
'''
print(letter.replace("Name","Dhruv").replace("Date","24|09|2026")) #chaining of replace function

#WAP to detect double spacing
str1 = "Good word  done"
print(name.find("  ")) #checks for index of the value
#if -1 then  value not in the parent string
print(str1.find("w"))

#replace double space with single space
print(str1.replace("  "," "))