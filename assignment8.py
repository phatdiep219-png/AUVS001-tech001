#1
import time

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Thang máy đang ở tầng: {self.current_floor}")
        else:
            print("Đã ở tầng cao nhất!")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Thang máy đang ở tầng: {self.current_floor}")
        else:
            print("Đã ở tầng thấp nhất!")

    def go_to_floor(self, target_floor):
        print(f"--- Bắt đầu di chuyển đến tầng {target_floor} ---")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Đã đến tầng {self.current_floor}.\n")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        # Tạo danh sách các thang máy
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        if 0 <= elevator_num < len(self.elevators):
            print(f">> Điều khiển thang máy số {elevator_num + 1}:")
            self.elevators[elevator_num].go_to_floor(destination_floor)
        else:
            print("Số thứ tự thang máy không hợp lệ.")

    def fire_alarm(self):
        print("\n!!! BÁO CHÁY !!! TẤT CẢ THANG MÁY QUAY VỀ TẦNG TRỆT")
        for i, elevator in enumerate(self.elevators):
            print(f"Thang máy số {i + 1} đang di chuyển xuống...")
            elevator.go_to_floor(self.bottom_floor)

#2
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        
        self.current_speed = max(0, min(self.max_speed, self.current_speed + change))

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
           
            speed_change = random.randint(-15, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\nCuộc đua: {self.name}")
        print(f"{'Biển số':<10} | {'Vận tốc tối đa':<15} | {'Vận tốc hiện tại':<18} | {'Quãng đường':<12}")
        print("-" * 65)
        for car in self.cars:
            print(f"{car.registration_number:<10} | {car.max_speed:<15} | "
                  f"{car.current_speed:<18} | {car.travelled_distance:<12.1f} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False
car_list = []
for i in range(10):
    max_spd = random.randint(100, 200)
    car_list.append(Car(f"ABC-{i+1}", max_spd))

race = Race("Grand Demolition Derby", 8000, car_list)

hours_elapsed = 0
while not race.race_finished():
    race.hour_passes()
    hours_elapsed += 1
    

    if hours_elapsed % 10 == 0:
        print(f"\n--- Trạng thái sau {hours_elapsed} giờ ---")
        race.print_status()

print(f"\n==== CUỘC ĐUA KẾT THÚC SAU {hours_elapsed} GIỜ ====")
race.print_status()
