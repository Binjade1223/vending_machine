# -*- coding: utf8 -*-
# import necessary library 匯入RPi.GPIO與time時間函式庫
import RPi.GPIO as GPIO   
import time   

# to use Raspberry Pi board pin numbers 使用板上定義的腳位號碼
GPIO.setmode(GPIO.BOARD)   

# set up pin 11 as an output  將P1接頭的11腳位設定為輸入 
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

# enter while loop unitl exit 隨著時間迴圈會重複執行，直到強制離開
while True:

# set up input value > row, column value

   rows = [GPIO.input(16),GPIO.input(7),GPIO.input(11),GPIO.input(15)]
   columns = [GPIO.input(12),GPIO.input(18),GPIO.input(13)]
   r, c = 0, 0

# when user press the btn 如果是真 (玩家按下按鈕)

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

   time.sleep(1)
