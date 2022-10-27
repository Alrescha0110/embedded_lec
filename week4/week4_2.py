# 2. GPIO.cleanup() 함수를 넣어 할당된 핀을 reset하려고 한다. 
# python의 "try~ expect" 구문을 사용하여 ctrl+c 입력으로 종료된 경우 LED를 모두 끄고 핀을 reset 하시오.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # mod : borad

GPIO.setup(37, GPIO.OUT) # LED1
GPIO.setup(36, GPIO.OUT) # LED2
GPIO.setup(38, GPIO.OUT) # LED3
GPIO.setup(40, GPIO.OUT) # LED4

while True: # 무한히 시계 방향으로 순차적 점등
    try: # 예외가 발생하기 전까지 동작
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
    except KeyboardInttrupt: # ctrl + c 하면 예외 발생
        GPIO.cleanup() # 핀 reset
        exit() # 모두 종료