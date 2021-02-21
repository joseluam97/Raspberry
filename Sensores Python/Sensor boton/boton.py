import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
while True:
     inputValue = GPIO.input(24)
     if (inputValue == True):
         GPIO.output(18, GPIO.HIGH)
         print("Encendido")
         time.sleep(0.3)
         break
while True:
    inputValue = GPIO.input(24)
    if (inputValue == True):
         GPIO.output(18, GPIO.LOW)
         print("Apagado")
         time.sleep(0.3)
         break
GPIO.cleanup()