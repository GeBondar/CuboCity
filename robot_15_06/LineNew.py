#!/usr/bin/python3

from ev3dev.ev3 import *
from time import sleep
from subprocess import call
from robotNet import *
from robotLibs import *


def vpered_new():
	print('4 = ', cl4.value())
	print('2 = ', cl2.value())
	while not ((cl4.value() > 750 and cl2.value() > 750) or btn.backspace):
		
		e = (cl4.value()-cl2.value())*0.25

		mB.run_forever(speed_sp=motor(-speed-e))
		mC.run_forever(speed_sp=motor(-speed+e))
#		mA.run_forever(speed_sp=-e*0.4)
#		mD.run_forever(speed_sp=-e*0.4)
		print('4 = ', cl4.value())
		print('2 = ', cl2.value())
	MotorStop()
	return 

while not btn.backspace:
	vpered_new()

