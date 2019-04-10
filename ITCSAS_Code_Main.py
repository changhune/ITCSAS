# Import Libraries
import time
import board
import busio
import digitalio
import adafruit_max31855
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
# Define Pins For Thermocouple Amplifier Communication
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)
max31855 = adafruit_max31855.MAX31855(spi, cs)
# Define LCD Row/Column Numbers -- 2 Rows of 16 Columns Each
lcd_columns = 16
lcd_rows = 2
# Initialise I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

# Clear text from LCD
lcd.clear()

while True:
	# Read Temperature from Amplifier
	tempC = max31855.temperature
	
	# Convert Temperature to Fahreneit
    #tempF = tempC * 9 / 5 + 32
	
	# Optional: Print temperature to terminal
    #print('Temperature: {} C {} F '.format(tempC, tempF))
	
	lcd.color = [255,255,255]
	lcdText = ("Temp.:"+tempC+"°C\n"+"LINE 2")
	lcd.message = lcdText
	
	# Wait 2 Seconds
    time.sleep(2)
		

