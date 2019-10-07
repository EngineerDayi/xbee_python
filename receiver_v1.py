import serial
 
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout = .15)
#.15 is 150 ms. If you change this parameter, you have to change this parameter in receiver code.  
# You have to use XBee explorer. Because it's right way for communication.

while True:

    response = ser.readline().strip()
    new = response.decode("utf-8")
    print(new)