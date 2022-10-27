import RPi.GPIO as GPIO
import time

SW=[5,6,13,19]
state=[0,0,0,0]
PWMA=18
AIN1=22
AIN2=27

PWMB=23
BIN1=25
BIN2=24
moterSet=[PWMA,AIN1,AIN2,PWMB,BIN1,BIN2]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(len(SW)):
	GPIO.setup(SW[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for i in range(len(moterSet)):
	GPIO.setup(moterSet[i], GPIO.OUT)

L_Motor=GPIO.PWM(PWMA,500)
L_Motor.start(0)
R_Motor=GPIO.PWM(PWMB,500)
R_Motor.start(0)

def go():
	GPIO.output(AIN1,0)
	GPIO.output(AIN2,1)
	L_Motor.ChangeDutyCycle(100)
	GPIO.output(BIN1,0)
	GPIO.output(BIN2,1)
	R_Motor.ChangeDutyCycle(100)

def back():
	GPIO.output(AIN1,1)
	GPIO.output(AIN2,0)
	L_Motor.ChangeDutyCycle(100)
	GPIO.output(BIN1,1)
	GPIO.output(BIN2,0)
	R_Motor.ChangeDutyCycle(100)

def right():
	GPIO.output(AIN1,0)
	GPIO.output(AIN2,1)
	L_Motor.ChangeDutyCycle(100)
	GPIO.output(BIN1,1)
	GPIO.output(BIN2,0)
	R_Motor.ChangeDutyCycle(100)

def left():
	
	GPIO.output(AIN1,1)
	GPIO.output(AIN2,0)
	L_Motor.ChangeDutyCycle(100)
	GPIO.output(BIN1,0)
	GPIO.output(BIN2,1)
	R_Motor.ChangeDutyCycle(100)

def stop():
	GPIO.output(AIN1,1)
	GPIO.output(AIN2,0)
	L_Motor.ChangeDutyCycle(0)
	GPIO.output(BIN1,1)
	GPIO.output(BIN2,0)
	R_Motor.ChangeDutyCycle(0)



try:
	while True:
			for i in range(len(SW)):
				state[i]=GPIO.input(SW[i])
			if state[0]:
				go()
			elif state[1]:
				right()
			elif state[2]:
				left()
			elif state[3]:
				back()
			else:
				stop()
				
except KeyboardInterrupt:
	pass

GPIO.cleanup()