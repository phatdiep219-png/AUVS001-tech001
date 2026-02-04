#1
def kiem_tra_ca_zander():
    chieu_dai = float(input("Nhập chiều dài cá zander (cm): "))
    gioi_han = 42

    if chieu_dai < gioi_han:
        thieu = gioi_han - chieu_dai
        print("Cá không đạt kích thước. Hãy thả cá lại hồ.")
        print(f"Cá ngắn hơn quy định {thieu:.1f} cm.")
    else:
        print("Cá đạt kích thước cho phép.")
#2
def cabin_description():
    cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()

    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")
#3
def check_hemoglobin():
    sex = input("Enter biological sex (male/female): ").lower()
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))

    if sex == "female":
        if hemoglobin < 117:
            print("Hemoglobin level is low.")
        elif hemoglobin <= 155:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")

    elif sex == "male":
        if hemoglobin < 134:
            print("Hemoglobin level is low.")
        elif hemoglobin <= 167:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")
    else:
        print("Invalid sex input.")
#4
def check_leap_year():
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
#5
import math

def pizza_unit_price(d, p):
    r = (d / 2) / 100
    return p / (math.pi * r * r)

d1 = float(input("Pizza 1 diameter (cm): "))
p1 = float(input("Pizza 1 price (USD): "))
d2 = float(input("Pizza 2 diameter (cm): "))
p2 = float(input("Pizza 2 price (USD): "))

u1 = pizza_unit_price(d1, p1)
u2 = pizza_unit_price(d2, p2)

if u1 < u2:
    print("Pizza 1 is cheaper per square meter.")
elif u2 < u1:
    print("Pizza 2 is cheaper per square meter.")
else:
    print("Both pizzas have the same price.")