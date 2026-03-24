''' 
vowels - g
eg- dog - dgg
cat - cgt
'''

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation =  translation + "g"
        else:
            translation = translation + letter
    return translation

print("The translation is",translate(input("Enter a phrase: ")))