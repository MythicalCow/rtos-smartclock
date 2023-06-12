
import serial
import time
from datetime import datetime
import requests

#open serial port
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

key = open('key.txt', 'r').read().rstrip()
city = 'HERNDON'
state = 'VA'
country = 'US'

temp = 0
condition = ''

while True:
    if int(datetime.now().strftime('%M')) % 10 == 0:
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + state + ',' + country + '&appid=' + key
        response = requests.get(url)
        data = response.json()
        temp = int(data['main']['temp'] * 9/5 - 459.67)
        condition = data['weather'][0]['main']
    #send the time and weather to the arduino in this format: 23:59:59 00__clear military time
    k = datetime.now().strftime('%H:%M:%S') + ' ' + str(temp) + ' Deg. ' + condition
    #convert to byte string
    k = k.encode('utf-8')
    print(k)
    ser.write(k)
    time.sleep(5)


