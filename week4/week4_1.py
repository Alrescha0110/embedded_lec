# 1. GPIO핀 모드를 Board로 하여 LED 4개를 켜고 끄는 코드를 작성하시오.
# 시계방향으로 순차적으로 점등되도록 함

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # mod : borad

GPIO.setup(37, GPIO.OUT) # LED1
GPIO.setup(36, GPIO.OUT) # LED2
GPIO.setup(38, GPIO.OUT) # LED3
GPIO.setup(40, GPIO.OUT) # LED4

while True: # 무한히 시계 방향으로 순차적 점등
    GPIO.output(37,GPIO.HIGH) # LED1 킴
    time.sleep(1.0)           # 1초 유지 
    GPIO.output(37,GPIO.LOW)  # LED1 끔 
    time.sleep(1.0)
    
    GPIO.output(36,GPIO.HIGH) # LED2 킴
    time.sleep(1.0)
    GPIO.output(36,GPIO.LOW)  # LED2 끔 
    time.sleep(1.0)
    
    GPIO.output(40,GPIO.HIGH) # LED4 킴
    time.sleep(1.0)
    GPIO.output(40,GPIO.LOW)  # LED4 끔 
    time.sleep(1.0)
    
    GPIO.output(38,GPIO.HIGH) # LED3 킴
    time.sleep(1.0)
    GPIO.output(38,GPIO.LOW)  # LED3 끔 
    time.sleep(1.0) 