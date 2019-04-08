# MAX31855 Thermocouple Amplifier Test

# Wiring:
# Pi 3.3V to Sensor Vin
# Pi GND to Sensor GND
# Pi SCLK to Sensor CLK
# Pi MISO to Sensor DO
# Pi GPIO5 to Sensor CS -- Board D5 Can Be Substituted with Other Digital IO Pin

# Library Installation:
# sudo pip3 install adafruit-circuitpython-max31855

# Example Code:
  
  # Import Libraries:
    import time
    import board
    import busio
    import digitalio
    import adafruit_max31855
  # Define Required IO Pins:
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs = digitalio.DigitalInOut(board.D5)
  # Define Sensor IO:
    max31855 = adafruit_max31855.MAX31855(spi, cs)
    
    while True:     # Always (While program running)
        tempC = max31855.temperature    # Set tempC to the temperature, in degrees C, read by sensor
        tempF = tempC * 9 / 5 + 32    # Convert temperature to Fahrenheit
        print('Temperature: {} C {} F '.format(tempC, tempF))     # Display temperature in degrees C and degrees F
        time.sleep(2.0)     # Wait 2 seconds

