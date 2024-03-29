#manual setup implementation. See ShiftRegister.py for the class implementation
import  RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

PIN_DATA = 16
PIN_LATCH = 20
PIN_CLOCK = 21

GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

ledpattern = "01010101"

GPIO.output(PIN_LATCH, 0)

for x in range(8):
	GPIO.output(PIN_DATA, int(ledpattern[x-1]))
	GPIO.output(PIN_CLOCK, 1)
	GPIO.output(PIN_CLOCK, 0)

GPIO.output(PIN_LATCH, 1)

