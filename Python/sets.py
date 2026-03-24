d = d = {} #empty dictionary
s  = {1,5,12}
empty_set  = set() #empty set
print(type(empty_set))
#elements dont get repeated in sets
#only takes duplicate elements once
#unordered

s.add(566)
print(s)

#operations on set
print(len(s))
print(s.remove(1))
print(s)

s1 = {1,45,6}
s2 = {7,8,1,78}
print(s1.union(s2)) #combined
print(s1.intersection(s2)) #common values


#wap to create a dict of hindi words with values as their english translation. provide user with an option to look up to it
words = {
    "madad" : "help",
    "kursi" : "chair",
    "kutta" : "dog"
}

word = input("Enter  hindi word whose meaning you want: ")
print(words.get(word))


#wap to input 8 numbers from user and siplay all unique numbers once
s_new = set()
for i in range(8):
    num = int(input("Enter number: "))
    s_new.add(num)
print(s_new) 

#create an empty dictionary. allow 4 friends to enter their fav lang as value and keys as their names. 
d = {}
for i in range(4):
    name = input("Enter friends name: ")
    lang = input("Enter friends fav lang: ")
    d.update({name:lang})
print(d)

