#it stores data in key value pair
#to access an info we refer to its key
#key is an identification in dictionary and value is basically its definition

#All keys must always be unique

monthConversions = {
    "Jan": "January", #jan is key and january is its value
    "Feb": "February", #feb is key and february is value
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "Septemeber",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "Decemeber"
}#anything inside {} are part of dict

print(monthConversions) #prints whole dic
print(monthConversions["Oct"]) #prints value of oct key
print(monthConversions.get("Dec")) #prints value if present in dict else None

marks = {
    "Harry" : 100,
    "Shubham" : 86,
    "Rohan" : 23,
    "list" : [10,20,30]
}

print(marks, type(marks))
print(marks["Harry"]) #prints value of key harry
print(marks["list"])
print(marks["list"][1])

#keys are the indexing of values
