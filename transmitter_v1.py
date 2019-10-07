import serial

ser = serial.Serial('/dev/ttyUSB0', 9600,timeout = .3) 
#.3 is 300 ms. If you change this parameter, you have to change this parameter in receiver code.  
# You have to use XBee explorer. Because it's right way for communication.

while True:
    ser.write('H \n'.encode())
    print("while") 