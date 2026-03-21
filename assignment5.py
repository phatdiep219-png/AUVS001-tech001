#1
numbers = []

while True:
    s = input("Enter number: ")
    if s == "":
        break
    numbers.append(float(s))

numbers.sort(reverse=True)

for n in numbers[:5]:
    print(n)

#2
n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number")
else:
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

#3
cities = []

for i in range(5):
    city = input("Enter city: ")
    cities.append(city)

for city in cities:
    print(city)

#4
def sum_list(numbers):
    return sum(numbers)

nums = [1,2,3,4,5]
print(sum_list(nums))

#5
def remove_odds(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

nums = [1,2,3,4,5,6,7]
new_list = remove_odds(nums)

print("Original:", nums)
print("Without odds:", new_list)