secret_word = "help"
chance = 0

print("you get 3 chances ")
while chance<3:
    guess = input("Enter your guess: ")
    if guess == secret_word:
        print("Correct guess")
        break
    else:
        chance = chance + 1
        print("You have",3-chance,"left")
        
if chance == 3:
    print("You couldnt guess")
