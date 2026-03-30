# 🎯 Number Guessing Game

![Python](https://img.shields.io/badge/python-3.x-blue?logo=python\&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

A fun and interactive Python game where you guess a randomly generated number. Includes multiple difficulty levels, a hint system, scoring, and replay options!

---

## 🚀 Features

* **Difficulty Levels**

  * **Easy:** 1–50, 18 attempts, starting score 50
  * **Medium:** 1–250, 15 attempts, starting score 100
  * **Hard:** 1–500, 7 attempts, starting score 200
* **Hint System**

  * 🔥 Very Hot (difference ≤ 5)
  * 🌡️ Warm (difference ≤ 15)
  * ❄️ Cold (difference ≤ 30)
  * 🥶 Very Cold (difference > 30)
* **Scoring**

  * Score decreases after each wrong attempt
  * Try to maximize your final score!
* **Replay Option**

  * Play multiple times without restarting the program

---

## 🎮 How to Play

1. Run the Python script:

   ```bash
   python Guess_number_game_updated_version.py
   ```
2. Choose a difficulty level:

   ```
   1 = Easy
   2 = Medium
   3 = Hard
   ```
3. Guess the secret number within the allowed attempts.
4. Follow the hints after each guess to get closer to the number.
5. After the game ends, decide whether to play again.

---

## 💡 Example Gameplay

```
Choose your difficulty level
1 = Easy
2 = Medium
3 = Hard
Enter your choice: 2

Guess number between 1 and 250

Enter your guess (15 turns left): 100
📈 TOO LOW!
🌡️ Warm

Enter your guess (14 turns left): 150
📉 TOO HIGH!
🔥 VERY HOT!

Enter your guess (13 turns left): 145
🎉 Congratulations!
Your final score = 93
```

---

## 🛠 Requirements

* Python 3.x
* No external libraries required

---

## 🤝 Contributing

1. Fork the repository
2. Make your changes or add new features
3. Submit a pull request with a description of your updates

---

## 📄 License

MIT License – free to use and modify for educational purposes.
