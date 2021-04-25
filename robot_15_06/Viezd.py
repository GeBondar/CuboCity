#!/usr/bin/python3
from ev3dev.ev3 import *
from time import sleep
from subprocess import call

from robotNet import *
from robotLibs import *




mB = LargeMotor('outB')
mC = LargeMotor('outC')
mA = MediumMotor('outA')
mD = MediumMotor('outD')

btn = Button()
e1 = 0
e = 0
n = 0
Sred = 0
floor = 0
speed = 200



def MotorStop(m):
	if m==1:
		mC.stop(stop_action='hold')
		mB.stop(stop_action='hold')
	if m==2:
		mA.stop(stop_action='hold')
		mD.stop(stop_action='hold')
	return m==0
	
mB.run_to_rel_pos(position_sp=540, speed_sp=300)
mC.run_to_rel_pos(position_sp=540, speed_sp=300)
sleep(2)
Motorstop(1)	
	


sleep(2)
