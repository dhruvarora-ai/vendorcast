#.items()
marks = {
    "harry" : 100,
    "Shubham" : 20,
    "Rohan" :70,
    0 : "harry"
}
print(marks)
print(marks.items()) #gives key value pair in list, each pair is in tuple
print(marks.keys())
print(marks.values())

marks.update({"harry":99, "renuka":39}) #renuka gets added to the end of dict
print(marks)

print(marks.get("Shivika")) #will print none
print(marks.get("harry")) #99






























