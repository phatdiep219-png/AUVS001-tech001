import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# --- PART 1: create a car ---
car = Car("ABC-123", 142)

print("Car information:")
print(car.registration_number, car.max_speed, car.current_speed, car.travelled_distance)


# --- PART 2: accelerate ---
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("Current speed:", car.current_speed)

car.accelerate(-200)
print("Final speed after brake:", car.current_speed)


# --- PART 3: drive ---
car.current_speed = 60
car.travelled_distance = 2000
car.drive(1.5)

print("Travelled distance:", car.travelled_distance)


# --- PART 4: car race ---
cars = []

for i in range(1, 11):
    reg = "ABC-" + str(i)
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))

race = True

while race:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.travelled_distance >= 10000:
            race = False

# print results
print("\nRace results:")
print("Reg\tMax\tSpeed\tDistance")

for car in cars:
    print(car.registration_number, car.max_speed,
          car.current_speed, round(car.travelled_distance, 1), sep="\t")