import random
name = input ("Enter your name: ")
attempts = 7
attempt = 0

print (f"Welcome {name}")
print ("I have a number between 1-100 can you guess it?")

randnum = random.randint(1,100)

while attempt < attempts:
    attempt += 1
    number = int(input ("Guess the number: "))
    if attempt >= attempts:
        print ("Game Over")
        break
    elif number > randnum:
        print ("Lower")
    elif number < randnum:
        print ("Higher")
    else:
        print (f"Correct you guessed it right")
        break
    
