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

# enter while loop unitl exit 隨著時間迴圈會重複執行，直到強制離開
while True:

# set up input value as GPIO.11 將P1接頭的11腳位的值設定為inputValue
   inputValue = [GPIO.input(7),GPIO.input(11),GPIO.input(13),GPIO.input(15),GPIO.input(12),GPIO.input(16),GPIO.input(18)]

# when user press the btn 如果是真 (玩家按下按鈕)
   if inputValue != [0,0,0,0,1,0,1]:

# show string on screen   顯示被按下
      print("Button pressed ")
      print(inputValue)
      while inputValue != [0,0,0,0,1,0,1]:  
# Set time interval as 0.3 second delay 設定延遲間隔為零點三秒鐘
            time.sleep(0.3)
