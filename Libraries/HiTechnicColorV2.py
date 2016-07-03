from mindsensors_i2c import mindsensors_i2c
class HiTechnicColorV2(mindsensors_i2c):
    Color_ADDRESS = (0x02)
    Color_COMMAND = (0x41)
   
## Initialize the class with the i2c address of your Hitechnic Color Sensor
    #  @param self The object pointer.
    #  @param i2c_address Address of your Hitechnic Color Sensor.
    def __init__(self, color_address = Color_ADDRESS):
        #the DIST address
        mindsensors_i2c.__init__(self, color_address >> 1)
 
## Reads the color number of your Hitechnic Color Sensor
    #  @param self The object pointer.
    def get_colornum(self):
        try:
            return (self.readIntegerBE(self.Color_COMMAND))
        except:
            print "Error: Could not read color"
            return ""


