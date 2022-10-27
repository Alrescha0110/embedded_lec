import threading
import serial
import RPi.GPIO as GPIO
import time

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.01)

PWMA=18
AIN1=22
AIN2=27

PWMB=23
BIN1=25
BIN2=24
moterSet=[PWMA,AIN1,AIN2,PWMB,BIN1,BIN2]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

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
	R_Motor.ChangeDutyCycle(0)

def left():
	
	GPIO.output(AIN1,1)
	GPIO.output(AIN2,0)
	L_Motor.ChangeDutyCycle(0)
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

gData = ""

def serial_thread():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data

def main():
    global gData
    try:
        while True:
            if gData.find("go") >= 0:
                gData=""
                print("ok go")
                go()
            elif gData.find("right") >= 0:
                gData=""
                print("ok right")
                right()
                time.sleep(1.0)
                go()
            elif gData.find("left") >= 0:
                gData=""
                print("ok left")
                left()
                time.sleep(1.0)
                go()
            elif gData.find("back") >= 0:
                gData=""
                print("ok back")
                back()
            elif gData.find("stop") >= 0:
                gData=""
                print("ok stop")
                stop()
    except KeyboardInterrupt:
        pass

if __name__=='__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()
