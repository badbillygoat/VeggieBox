#import necessary libraries
import time
import adafruit_dht
import board
import LCD
from datetime import datetime

#define the DHT11 temp/humidity sensor as being input through GPIO17 pin on the Pi.
dht = adafruit_dht.DHT11(board.D17)

#connect to my Adafruit account so the program knows where to send my data on the internet.
from Adafruit_IO import Client
aio = Client('badbillygoat', 'aio_PTkT48yedCgFHq9Emwd8Os5orjJl')

#begin the while loop that contiously reads the tempature + humidiy, and logs it to the LCD display and cloud dashboard.
while True:
    try:
        temperature_f = (dht.temperature * 9/5) + 32
        temperature_c = round(dht.temperature, 2)
        humidity = dht.humidity
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        
        LCD.write(str(temperature_f) + "F  " + str(current_time),str(humidity) + "% Humidity")
        time.sleep(10)
        LCD.write("Hey Jordan","I'm learning!")
        time.sleep(10)

        humfeed = aio.feeds('roomhumidity')
        aio.send_data(humfeed.key, humidity)

        tempfeed = aio.feeds('roomtemperature')
        aio.send_data(tempfeed.key, round(temperature_f,2))

    except RuntimeError as e:
        print("Reading from DHT failure: ", e.args)
