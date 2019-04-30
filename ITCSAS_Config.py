######################################################################
# IMPROVED THERMAL CONCRETE STRENGTH ASSESSMENT SYSTEM CONFIGURATION #
######################################################################

#--------------------------------------------------------------------#
# Camera Settings
#--------------------------------------------------------------------#

# Set Camera Resolution
camXRes = 32	# Width (columns)
camYRes = 24	# Height (rows)

#--------------------------------------------------------------------#
# LCD/Display Settings
#--------------------------------------------------------------------#

# Set RGB Display Color 
defaultDisplayColor = [100,100,100]	# [RED,GREEN,BLUE] (0-100)
	
# Set Temperature Format - Celsius, Fahrenheit, or Kelvin
dispTempFormat = 0	# 0 for °C, 1 for °F, 2 for K
	
# Set Display Size
dispColumn = 16
dispRow = 2
	
#--------------------------------------------------------------------#	
# Temperature Reading Settings
#--------------------------------------------------------------------#

# Set Number of Readings to Average
numAvg = 2
# Set Time Between Readings
timeAvg = 15
# Set Temperature Adjustment Offset
tempOffset = -23
