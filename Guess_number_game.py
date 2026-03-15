import random
def Guess_number():
    random_num=random.randint(1,100)
    return random_num
print("Enter your guessed number between 1 nad 100")
secrect_number=Guess_number()
while True:
    guess=int(input("Enter your guess"))
    if secrect_number<guess:
        print("TOO HIGH! The number is lower than ",guess)
    elif secrect_number>guess:
        print("TOO LOW! The number is higher than ",guess)
    else:
        print("Congratulation! You guessed it correct")
        print("The secrect number is ",secrect_number)
        break

