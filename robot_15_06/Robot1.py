#!/usr/bin/python3

from ev3dev.ev3 import *
from time import sleep
from socket import *
from subprocess import call

mA = MediumMotor('outA')
mB = LargeMotor('outB')
mC = LargeMotor('outC')
mD = MediumMotor('outD')

btn = Button()
cl3 = ColorSensor('in3')
cl4 = ColorSensor('in4')
e = 0
u = 0
k = 2
speed = 150

e1 = 0
n = 0 
m = 0

def time1(e):
	e = m*n*0.00005
	return e==0
def motor(speed):
	if speed > 900:
		speed  = 900
	elif speed < -900:
		speed = -900
	return speed

def MotorStop(m):
	mA.stop(stop_action='hold')
	mB.stop(stop_action='hold')
	mC.stop(stop_action='hold')
	mD.stop(stop_action='hold')

	return m==0

def AMBIENT(m):
	cl3.mode='COL-AMBIENT'
	cl4.mode='COL-AMBIENT'
	return m==0
def REFLECT(m):
	cl3.mode='COL-REFLECT'
	cl4.mode='COL-REFLECT'
	return m==0

def vpered(n):
	REFLECT(1)
	while not ((cl3.value() < 15 and cl4.value() < 15)or btn.backspace):
		
		e = (cl3.value() - cl4.value())*k

		mB.run_forever(speed_sp=motor(speed-u))
		mC.run_forever(speed_sp=motor(speed+u))
	MotorStop(1)
	Sound.tone(200, 10)
	return n==0

def vpered_led(n):
	AMBIENT(1)
	Sound.tone(200, 200)
	while not ((cl3.value() > 35 and cl4.value() > 35) or btn.backspace):
		
		e = (cl3.value()-cl4.value())*-4

		mB.run_forever(speed_sp=motor(speed-e))
		mC.run_forever(speed_sp=motor(speed+e))
		print(cl3.value())
		print(cl4.value())
	MotorStop(1)
	Sound.tone(200, 500)
	return n==0

def pr1(m, n):
	
	mB.reset()
	mC.reset()
	mB.run_to_rel_pos(position_sp=m, speed_sp=n)
	mC.run_to_rel_pos(position_sp=m, speed_sp=n)
	e1 = abs(m*n*0.00005)
	sleep(e1)
	print(e1)
	MotorStop(1)
	return m==0, n==0

def pr2(m, n):
	mA.reset()
	mD.reset()
	mA.run_to_rel_pos(position_sp=m, speed_sp=n)
	mD.run_to_rel_pos(position_sp=-m, speed_sp=n)
	e1=abs(m*n*0.00005)
	print(e1)
	sleep(e1)
	MotorStop(1)
	return m==0, n==0

def vpravo(m):
	AMBIENT(1)
	while not (cl3.value() > 30 or btn.backspace):
		
                e = 32  - cl3.value()
                u = e*-3
                mB.run_forever(speed_sp=motor(u))
                mC.run_forever(speed_sp=motor(u))
                mA.run_forever(speed_sp=m)
                print("u = ", u)
                print(btn.backspace)

	MotorStop(1)
	return m==0

def vlevo(m):
	AMBIENT(1)
	while not (cl4.value() < 15 or btn.backspace):
		
		e = 32 - cl4.value()
		u = e*-3
		mB.run_forever(speed_sp=motor(u))
		mC.run_forever(speed_sp=motor(u))
		mA.run_to_rel_pos(position_sp=m, speed_sp=m)
	MotorStop(1)
	return m==0

def lin(m, e):
	REFLECT(1)
	while not btn.backspace:
		mB.run_forever(speed_sp=(12 - cl3.value())*-3)
		mC.run_forever(speed_sp=(12 - cl4.value())*-3)
		e = e+1
		print(n)
		if e >= 170:
			break
	MotorStop(1)
	Sound.tone(200, 200)
	return m==0, e==0

def initMailbox():
	mbx = socket(AF_INET, SOCK_DGRAM)
	mbx.bind(('255.255.255.255', 12345))
	return mbx

def sendMessage(message):
	s=socket(AF_INET, SOCK_DGRAM)
	s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	s.sendto(message.encode('utf-8'),('255.255.255.255', 12345))
	return message == 0

mailbox = initMailbox()
#m = mailbox.recv(1024).decode('utf-8')


def lift1(e, n):
	
	while not btn.backspace:
		
		if e==1:
			sendMessage('floor_1')
		if e==2:
			sendMessage('floor_2')
		if e==3:
			sendMessage('floor_3')
		if e==4:
			sendMessage('floor_4')
		print('e = ',e)
		m = mailbox.recv(1024).decode('utf-8')
		print('m = ',m)
		if m=='stop':
			break
	Sound.tone(200, 400)
	while not btn.backspace:
		
		if n==1:
			sendMessage('lift_1')
		if n==2:
			sendMessage('lift_2')
		if n==3:
			sendMessage('lift_3')
		if n==4:
			sendMessage('lift_4')
		m = mailbox.recv(1024).decode('utf-8')
		print('m = ',m)
		print('n = ',n)
		if m=='lift_stoped':
			#pr1(-650, 450)
			break
	print(n)
	print(m)
	print(e)
	return n==0,e==0


#Sound.tone(400, 200)
#lift1(2, 3)
#Sound.tone(400, 200)
#pr2(150, 150)
#pr1(150, 150)
#vpered_led(1)
#vpered(1)
#pr1(170, 150)
#vpered(1)
#pr1(-30, 150)
#lin(1, 0)
#pr1(450, 400)

