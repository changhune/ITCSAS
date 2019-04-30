import time
import board
import busio
import digitalio
import adafruit_max31855
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import ITCSAS_Config as cfg

# Define LCD Row/Column Numbers -- 2 Rows of 16 Columns Each
lcd_columns = cfg.dispColumn
lcd_rows = cfg.dispRow

# Initialise I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialise the LCD class
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

# Clear text from LCD
lcd.clear()

lcd.color = cfg.defaultDisplayColor
lcd.message = ("     ITCSAS     \nInitializing")
time.sleep(.75)
lcd.message = ("     ITCSAS     \nInitializing.")
time.sleep(.75)
lcd.message = ("     ITCSAS     \nInitializing..")
time.sleep(.75)
lcd.message = ("     ITCSAS     \nInitializing...")
time.sleep(.75)
pin = digitalio.DigitalInOut(board.D4)
("   Digital IO   \nTest Successful")
time.sleep(.75)
i2c = busio.I2C(board.SCL, board.SDA)
("    I2C Bus     \nTest Successful")
time.sleep(.75)
lcd.clear()