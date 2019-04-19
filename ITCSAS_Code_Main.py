# Import Libraries
import time
import board
import busio
import digitalio
import adafruit_max31855
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import MLX90640
import ITCSAS_Config as cfg

# Define IR Camera
cam = MLX90640.MLX90640('0x33')

#To get readings from 32x24 pixel array, where (i,j) are coordiates of a pixel:
#cam.getCompensatedPixData(i,j)

# Define Pins For Thermocouple Amplifier Communication
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)
amp = adafruit_max31855.MAX31855(spi, cs)

# Define LCD Row/Column Numbers -- 2 Rows of 16 Columns Each
lcd_columns = cfg.dispColumn
lcd_rows = cfg.dispRow

# Initialise I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

# Clear text from LCD
lcd.clear()

while True:  
	# Take about 30 seconds to take 2 temperature readings 15 seconds apart and average them.
	tempSum = 0
	for x in range(numAvg+1):
		tempSum = tempSum+amp.temperature
		time.sleep(cfg.timeAvg)  # Wait between readings
	tempAvg = tempSum/numAvg  # Calculate average

	tempC = tempAvg+cfg.tempOffset  # Adjust temperature based on value defined in config

	# Convert Temperature from Celsius to Fahreneit
    tempF = tempC*9/5+32
	
	# Convert Temperature from Celsius to Kelvin
	tempK = tempC+273.15
	
	# Optional: Print Temperature to Terminal (Uncomment Next Line)
    #print('Temperature: {} C {} F {} K'.format(tempC, tempF, tempK))
	
	if cfg.dispTempFormat == 1:
		dispTemp = round(tempF,1)
	else:
		if cfg.dispTempFormat == 2:
			dispTemp = round(tempK,1)
		else:
			dispTemp = round(tempC,1)
			
	lcd.color = cfg.defaultDisplayColor
	lcdText = ("Temp.: "+dispTemp+"°C\n"+"LINE 2")
	lcd.message = lcdText