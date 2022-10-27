# 3. RC카의 부착되어 있는 LED 4개를 0.5초에 하나씩 랜덤하게 10번 켜는 코드를 작성하시오.  
# 실행시마다 LED 점등 순서가 매번 달라지도록 한다.
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD) # mod : borad

GPIO.setup(37, GPIO.OUT) # LED1
GPIO.setup(36, GPIO.OUT) # LED2
GPIO.setup(38, GPIO.OUT) # LED3
GPIO.setup(40, GPIO.OUT) # LED4

led_list=[37,36,38,40]  # list에 led1, led2, led3, led4의 핀번호 저장

for i in range(0,10): # 0.5초에 하나씩 랜덤하게 10번 점등
    random_led=random.choice(led_list) # 킬 LED 핀 번호를 네개 중에서 랜덤으로 하나 선택 
    GPIO.output(random_led,GPIO.HIGH) # LED 킴
    time.sleep(0.5)           # 0.5초 유지 
    GPIO.output(random_led,GPIO.LOW)  # LED 끔 
    time.sleep(0.5)        
