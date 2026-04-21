# Basic Python Exercises

## 1. Hello, Python

```python
print("Hello, Python!")
print("My name is Suha.")
print("I am excited to learn Python!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 \* num2)
print("Quotient:", num1 / num2)

age = int(input("Enter your age: "))
dog_years = age \* 7

print("Your age in dog years is:", dog_years)

food = input("What is your favourite food? ")

print(food, "sounds delicious! If I could code a meal, I would make a giant plate of", food + "!")


import random

secret_number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Correct! You guessed the number.")
else:
    print("Nice try! The correct number was", secret_number)

    I found the number guessing game the most fun because it felt more interactive than the other exercises. It was interesting to use the random module and see how Python can be used to make a simple game.

How did you feel when you saw your code running correctly for the first time?

I felt proud and excited when my code worked correctly for the first time. It was satisfying to see that even a few lines of Python could create something useful and interactive.

How could you imagine using these skills to solve problems or make daily tasks easier?

I can imagine using these skills to automate simple tasks, build small tools, and make programs that save time. For example, Python could be used to create calculators, simple trackers, reminders, or scripts to organise information more efficiently.
```
