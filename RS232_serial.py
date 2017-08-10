#!/usr/bin/python

import serial, time

ser = serial.Serial(
    port = '/dev/ttyUSB1', #TO MODIFY
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
)

#ser.timeout = None          #block read
ser.timeout = 1            #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write

try: 
    ser.open()
except Exception, e:
    print "error open serial port: " + str(e)
    exit()

if ser.isOpen():

    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()#flush output buffer, aborting current output 
                 #and discard all that is in buffer

        #write data
        ser.write("AT+CSQ")
        print("write data: AT+CSQ")
        time.sleep(0.5)
        numOfLines = 0
        while True:
            response = ser.readline()
            print("read data: " + response)

        numOfLines = numOfLines + 1

        ser.close()
    except Exception, e1:
        print "error communicating...: " + str(e1)

else:
    print "cannot open serial port "
