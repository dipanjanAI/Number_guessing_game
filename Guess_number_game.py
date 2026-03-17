import random
# Function to generate a random number between 1 and 100.
def Guess_number():
    random_num=random.randint(1,100)
    return random_num
print("Enter your guessed number between 1 and 100")
secrect_number=Guess_number()
attempt =0
score =100
# Using loop to check if the guessed number is correct.
while True:
    guess=int(input("Enter your guess "))
    attempt+=1
    if secrect_number<guess:
        print("TOO HIGH! The number is lower than ",guess)
    elif secrect_number>guess:
        print("TOO LOW! The number is higher than ",guess)
    else:
        print("Congratulation! You guessed it correct")
        print("The secrect number is ",secrect_number)
        break
# Showing number of attempts by the user.
print("Your number of attempts =",attempt)
# Calculating players score.
score-=10*attempt
print("Your score =",score)
 

