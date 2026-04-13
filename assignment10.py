#1
import requests
request= "https://api.chucknorris.io/jokes/random?"
response= requests.get(request)
if response.status_code == 200:
        data = response.json()
        print(data["value"])
else:
        print("Không lấy được dữ liệu!")

#2
import requests

def get_weather():
    city = "HaNoi"
    api_key = "12345"  
    
    url = f"http://api.openweathermap.org/data/3.0/weather?q={city}&appid={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        weather_desc = data["weather"][0]["description"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        
        print(f"Thời tiết: {weather_desc}")
        print(f"Nhiệt độ: {temp_celsius:.2f}°C")
    else:
        print("Không tìm thấy thành phố hoặc lỗi API!")

#3
from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=5000)

#4
from flask import Flask, jsonify

app = Flask(__name__)

airports = {
    "LFLL": {
        "name": "Lyon Saint-Exupery Airport",
        "city": "Lyon",
        "country": "FR"
    },
    "KJFK": {
        "name": "John F. Kennedy International Airport",
        "city": "New York",
        "country": "US"
    }
}

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    icao = icao.upper()  
    
    if icao in airports:
        data = airports[icao]
        result = {
            "icao": icao,
            "name": data["name"],
            "city": data["city"],
            "country": data["country"]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=5000 )