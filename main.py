import RPi.GPIO as GPIO
import time
import json

ledPin = 19
motor =12

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(motor, GPIO.OUT)

pwmone = GPIO.PWM(motor, 100)
pwmone.start(0)

while True:
  with open("steppercontrol.txt", 'r') as f:
      data = json.load(f)
  angle = float(data[angle])
  zero = str(data[zero])
  stepper(angle,zero)
  
  if zero == 1:
      pwmthree.stop()
      pwmtwo.stop()
      pwmone.ChangeDutyCycle(dutycycle)
      time.sleep(0.1)