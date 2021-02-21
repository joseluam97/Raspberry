import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
aux = 0
while True:
     inputValue = GPIO.input(24)
     if (inputValue == True):
	if(aux == 0):
        	GPIO.output(18, GPIO.HIGH)
        	print("Encendido")
        	time.sleep(0.3)
		aux = 1
	else: 
		if(aux == 1):
	        	GPIO.output(18, GPIO.LOW)
	        	print("Apagado")
	        	time.sleep(0.3)
			aux = 0
GPIO.cleanup()