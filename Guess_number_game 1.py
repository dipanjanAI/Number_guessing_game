import random

def Guess_number(max_num):
    return random.randint(1, max_num)

while True:
    print("\nChoose your difficulty level")
    print("1 = Easy\n2 = Medium\n3 = Hard")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        max_num = 50
        max_attempt = 18
        score = 50
    elif choice == 2:
        max_num = 250
        max_attempt = 15
        score = 100
    elif choice == 3:
        max_num = 500
        max_attempt = 7
        score = 200
    else:
        print("Invalid input")
        continue

    print(f"\nGuess number between 1 and {max_num}")
    
    secret_number = Guess_number(max_num)
    attempt = 0

    while attempt < max_attempt:
        guess = int(input(f"\nEnter your guess ({max_attempt - attempt} turns left): "))
        attempt += 1

        difference = abs(secret_number - guess)

        if guess > secret_number:
            print("📉 TOO HIGH!")
        elif guess < secret_number:
            print("📈 TOO LOW!")
        else:
            print("🎉 Congratulations!")
            print("Your final score =", score)
            break

        # 🔥 Hint system
        if difference <= 5:
            print("🔥 VERY HOT!")
        elif difference <= 15:
            print("🌡️ Warm")
        elif difference <= 30:
            print("❄️ Cold")
        else:
            print("🥶 Very Cold")

        # 💯 Score reduction
        score -= int(score / max_attempt)

    else:
        print("\n💀 Game Over!")
        print("The number was:", secret_number)
        print("Your score = 0")

    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! 👋")
        break
