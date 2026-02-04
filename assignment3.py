#1
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1

#2
while True:
    inch = float(input("Enter inches: "))
    if inch < 0:
        break
    print(inch * 2.54)

#3
numbers = []

while True:
    s = input("Enter a number: ")
    if s == "":
        break
    numbers.append(float(s))

print("Smallest:", min(numbers))
print("Largest:", max(numbers))

#4
import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct")
        break

#5
correct_user = "python"
correct_pass = "rules"
attempts = 0

while attempts < 5:
    user = input("Username: ")
    password = input("Password: ")

    if user == correct_user and password == correct_pass:
        print("Welcome")
        break
    attempts += 1
else:
    print("Access denied")

#6
def middle_char(s):
    n = len(s)
    if n % 2 == 0:
        return s[n//2 - 1 : n//2 + 1]
    return s[n//2]

#7
def acronym(phrase):
    return "".join(word[0].upper() for word in phrase.split())