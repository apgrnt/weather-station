import time
import board
import adafruit_bmp280

#Create sensor object, comm over boards default I2C bus
i2c = board.I2C()
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

bmp280.sea_level_pressure = 1013.25

while True:
    print("\nTempC: %0.1f C" % bmp280.temperature)
    print("TempF: %0.1f F" % (bmp280.temperature * (9 / 5) + 32.0))
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)
    time.sleep(2)
