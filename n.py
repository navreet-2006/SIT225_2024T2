import serial
import csv
import time
from datetime import datetime

s = serial.Serial('COM13', 9600, timeout=2)
time.sleep(2)  

file = "navreet.csv"

with open(file, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "X", "Y", "Z"])

    try:
        while True:
            if s.in_waiting > 0:
                data = s.readline().decode('utf-8').strip()
                print(f"Raw data: {data}")  
                values = data.split(',')
                if len(values) == 3:
                    x, y, z = values
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    writer.writerow([timestamp, x, y, z])
                    print(f"Timestamp: {timestamp}, X: {x}, Y: {y}, Z: {z}")
    except KeyboardInterrupt:
        print("Stopped")
        s.close()