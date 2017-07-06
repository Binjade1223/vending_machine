# import necessary library �פJRPi.GPIO�Ptime�ɶ��禡�w
import RPi.GPIO as GPIO   
import time   

# to use Raspberry Pi board pin numbers �ϥΪO�W�w�q���}�츹�X
GPIO.setmode(GPIO.BOARD)   

# set up pin 11 as an output  �NP1���Y��11�}��]�w����J 
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)

# enter while loop unitl exit �H�ۮɶ��j��|���ư���A����j�����}
while True:

# set up input value as GPIO.11 �NP1���Y��11�}�쪺�ȳ]�w��inputValue
   inputValue = [GPIO.input(7),GPIO.input(11),GPIO.input(13),GPIO.input(15),GPIO.input(12),GPIO.input(16),GPIO.input(18)]

# when user press the btn �p�G�O�u (���a���U���s)
   if False in inputValue:

# show string on screen   ��ܳQ���U
      print("Button pressed ")
      print(inputValue)
      while inputValue ==  False:  
# Set time interval as 0.3 second delay �]�w���𶡹j���s�I�T����
            time.sleep(0.3)
