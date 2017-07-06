# -*- coding: utf8 -*-
# import necessary library
import RPi.GPIO as GPIO   
import time

def get_button_input():
   x = raw_input("Enter what you want... ")
   return (int(x))

#TODO:
"""
def get_button_input():
   # to use Raspberry Pi board pin numbers
   GPIO.setmode(GPIO.BOARD)   

   # set up pins as an input 
   GPIO.setup(7, GPIO.IN)
   GPIO.setup(11, GPIO.IN)
   GPIO.setup(13, GPIO.IN)
   GPIO.setup(15, GPIO.IN)
   GPIO.setup(12, GPIO.IN)
   GPIO.setup(16, GPIO.IN)
   GPIO.setup(18, GPIO.IN)

   val_table = [["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"],
                ["*", "0", "#"]]
   
   # enter while loop unitl exit
   while True:

   # set up input value > row, column value

      rows = [GPIO.input(16),GPIO.input(7),GPIO.input(11),GPIO.input(15)]
      columns = [GPIO.input(12),GPIO.input(18),GPIO.input(13)]
      r, c = 0, 0

   # when user press the botton

      if True in rows:
         for i in rows:
            if i == True:
               row = r
            r+=1
         if True in columns:
            for j in columns:
               if j == True:
                  column = c
               c+=1
            print ("Button pressed: "+ val_table[row][column])

      time.sleep(0.3)
"""
