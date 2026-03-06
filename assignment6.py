#1
numbers = []

while True:
    s = input("Enter number: ")
    if s == "":
        break
    numbers.append(float(s))

numbers.sort(reverse=True)

print("Top 5 numbers:")
for n in numbers[:5]:
    print(n)

#2
seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter month (1-12): "))

season = seasons[(month % 12) // 3]
print(season)

#3
names = set()

while True:
    name = input("Enter name: ")
    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nNames entered:")
for n in names:
    print(n)

#4
def word_frequency(text):
    words = text.split()
    freq = {}

    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return freq

#5
def remove_odds(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


nums = [1,2,3,4,5,6,7,8]
print("Original:", nums)
print("Without odds:", remove_odds(nums))

#6
import random

points = int(input("How many random points: "))

inside = 0

for i in range(points):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x*x + y*y < 1:
        inside += 1

pi = 4 * inside / points

print("Approximation of pi:", pi)