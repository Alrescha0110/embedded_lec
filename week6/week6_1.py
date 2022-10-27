import RPi.GPIO as GPIO
import time


SW=[5,6,13,19]

state=[0,0,0,0]
GPIO_past_List=[0,0,0,0]

num=[0,0,0,0]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(len(SW)):
	GPIO.setup(SW[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
try:
	while True:
		for i in range(len(SW)):
			state[i]=GPIO.input(SW[i])
		for i in range(len(SW)):
			if (state[i]==1 and GPIO_past_List[i]==0):
				num[i]+=1
				print('SW'+ str(i+1) + ' click', num[i])
				GPIO_past_List[i]=state[i]	
				if(GPIO_past_List[i]==1):
					continue
			if (state[i]==0 and GPIO_past_List[i]==1):
				GPIO_past_List[i]=state[i]	
		time.sleep(0.1)
				
			
except KeyboardInterrupt:
	pass

GPIO.cleanup()