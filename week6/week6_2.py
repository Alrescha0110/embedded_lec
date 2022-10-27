import RPi.GPIO as GPIO
import time

BUZZER =12

SW=[5,6,13,19]
state=[0,0,0,0]
gye=[262,294,330,349]  # 도 레 미 파

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)
for i in range(len(SW)):
	GPIO.setup(SW[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

p=GPIO.PWM(BUZZER,261)

try:
	while True:
		for i in range(len(SW)):
			state[i]=GPIO.input(SW[i])
		for i in range(len(SW)):
			if state[i]:
				p.start(50)
				p.ChangeFrequency(gye[i])
				# time.sleep(0.1)
			p.stop()
		
except KeyboardInterrupt:
	pass

p.stop()
GPIO.cleanup()