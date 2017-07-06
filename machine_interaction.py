#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import server_connection as sConnect

"""Some params"""
continue_reading = True

#informations of products
products = [[example, 999999], [coke, 20], [orange_juice, 15]]

host = '127.0.0.1' #TODO: check...

"""main function"""
def main():
    while True:
        # Hook the SIGINT
        signal.signal(signal.SIGINT, end_read)

        # Create an object of the class MFRC522
        MIFAREReader = MFRC522.MFRC522()
        rfidRead()
"""get = getInputValue()
        pData = productData(get)
        if pData[2] != False: # check whether user choose drinks or not
            card = rfidRead()
            serverConnect = sConnect.serverConnect(card, pData[1])
            #TODO: resp = serverConnect[some_index...]
            #TODO: productNum = serverConnect[some_index...]
            if resp == True:
                productDropping(productNum)
                #TODO: myPrint(tell user the transaction is complete...)"""

"""Some useful functions"""

def myPrint(s, onLCD = None):
    #TODO: some information show on LCD
    print(s)
    
"""Step 1. choose product"""

def getInputValue():
    #TODO: defined by buttons on the vendor machine
    return 

"""Step 2. return the product information"""

def productData(user_req = None):
    #receive users request
    if user_req != None:
        return (user_req, products[user_req], True)
    else:
        return (None, None, False)


"""Step 3, 4, 5. read the card information from RFID"""

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

def rfidRead():
    # Welcome message
    print "Welcome to the MFRC522 data read example"
    print "Press Ctrl-C to stop."

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while continue_reading:
    
        # Scan for cards    
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print "Card detected"
    
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # UID
            uid = [int(uid[0]), int(uid[1]), int(uid[2]), int(uid[3])]
            print uid
            return uid
    
"""Step 9. pick product"""
    
def productDropping(number):
    #TODO: give machine the exact number to drop the right product
        
"""Main function"""       
if __name__ == '__main__':
    main()
                
