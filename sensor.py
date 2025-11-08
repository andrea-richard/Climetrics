import time
import board
import adafruit_ahtx0
import Therduce.presets as presets

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    temp = sensor.temperature
    humidity = sensor.relative_humidity
    time.sleep(2)