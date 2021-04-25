# Импорт общих библиотек ev3

from ev3dev.ev3 import *
from time import sleep
from subprocess import call
from robotNet import *
# Импорт модуля для Сети


# Импорт модуля для QR (снять комментарий когда будет готов)



#=======================================================#
# Инициализируем общие для всех блоков объекты          #
# И переменные тоже...                                  #
# Так-же в этом файле можно объявить общие функции      #
#=======================================================#


mA = MediumMotor('outA')
mB = LargeMotor('outB')
mC = LargeMotor('outC')
mD = MediumMotor('outD')

btn = Button()
cl1 = LightSensor('in1')
cl2 = LightSensor('in2')
cl3 = LightSensor('in3')
cl4 = LightSensor('in4')
n1 =0
e = 0
u = 0
r=0
k = 2
speed = 170
f = 0
e1 = 0
e2 = 1
n = 0 
m = 0

mailbox = initMailBox()

def motor(speed):
	if speed > 900:
		speed  = 900
	elif speed < -900:
		speed = -900
	return speed


def MotorStop():
	mA.stop(stop_action='hold')
	mB.stop(stop_action='hold')
	mC.stop(stop_action='hold')
	mD.stop(stop_action='hold')

	return

def AMBIENT():
	cl1.mode='AMBIENT'
	cl2.mode='AMBIENT'
	cl3.mode='AMBIENT'
	cl4.mode='AMBIENT'
	return
def REFLECT():
	cl1.mode='REFLECT'
	cl2.mode='REFLECT'
	cl3.mode='REFLECT'
	cl4.mode='REFLECT'
	return 

def Atack_of_Titan():
	while not btn.backspace:
		print('cl1 = ', cl1.value())
		print('cl2 = ', cl2.value())
		print('cl3 = ', cl3.value())
		print('cl4 = ', cl4.value())
	return 

def S():
	Sound.tone(200,200)
	return

def vpered(n):
	REFLECT()
	while not ((cl1.value() < 15 and cl4.value() < 15)or btn.backspace):
		
		e = (cl1.value() - cl4.value())*k

		mB.run_forever(speed_sp=motor(-speed-u))
		mC.run_forever(speed_sp=motor(-speed+u))
#	MotorStop(1)
	Sound.tone(200, 10)
	return n==0



def vpered_led():

	print(cl1.value())
	print(cl4.value())
	while not ((cl1.value() > 350 and cl4.value() > 350) or btn.backspace):
		
		e = (cl1.value()-cl4.value())*0.2

		mB.run_forever(speed_sp=motor(-speed-e))
		mC.run_forever(speed_sp=motor(-speed+e))
		mA.run_forever(speed_sp=-e*0.4)
		mD.run_forever(speed_sp=-e*0.4)
		print(cl1.value())
		print(cl4.value())
	MotorStop()
	return 

def vpravo():
	#AMBIENT(1)
	while not ((cl1.value() > 350 and cl2.value() > 350) or btn.backspace):
		print('cl1=',cl1.value())
		print('cl2=',cl2.value())
		e = (cl1.value()-cl2.value())*0.2
		mA.run_forever(speed_sp=motor(-speed+e))
		mD.run_forever(speed_sp=motor(speed+e))
		mB.run_forever(speed_sp=e*0.4)
		mC.run_forever(speed_sp=-e*0.4)
	MotorStop()
	return 

def vlevo():
	#AMBIENT(1)
	while not ((cl3.value() > 350 and cl4.value() > 350) or btn.backspace):
		print('cl3=',cl3.value())
		print('cl4=',cl4.value())
		e = (cl4.value()-cl3.value())*-0.2
		mA.run_forever(speed_sp=motor(speed+e))
		mD.run_forever(speed_sp=motor(-speed+e))
		mB.run_forever(speed_sp=e*0.4)
		mC.run_forever(speed_sp=-e*0.4)
	MotorStop()
	return 
	
def nazad():
	while not ((cl2.value() > 350 and cl3.value() > 350) or btn.backspace):
		print('cl2=',cl2.value())
		print('cl3=',cl3.value())
		e = (cl2.value()-cl3.value())*-0.2
		mB.run_forever(speed_sp=motor(speed-e))
		mC.run_forever(speed_sp=motor(speed+e))
		mA.run_forever(speed_sp=-e*0.4)
		mD.run_forever(speed_sp=-e*0.4)
	MotorStop()
	return 	
	
def vpered_black():
	REFLECT()
	print(cl1.value())
	print(cl4.value())
	while not ((cl1.value() < 470 and cl4.value() < 470) or btn.backspace):
		
		e = (cl1.value()-cl4.value())*0.37

		mB.run_forever(speed_sp=motor(-speed-e))
		mC.run_forever(speed_sp=motor(-speed+e))
		mA.run_forever(speed_sp=-e*0.4)
		mD.run_forever(speed_sp=-e*0.4)
		print(cl1.value())
		print(cl4.value())
	MotorStop()
	return 
	
def vlevo_black():
	REFLECT()
	while not ((cl3.value() < 470 and cl4.value() < 470) or btn.backspace):
		print('cl3=',cl3.value())
		print('cl4=',cl4.value())
		e = (cl4.value()-cl3.value())*-0.37
		mA.run_forever(speed_sp=motor(speed+e))
		mD.run_forever(speed_sp=motor(-speed+e))
		mB.run_forever(speed_sp=e*0.4)
		mC.run_forever(speed_sp=-e*0.4)
	MotorStop()
	return 
	
def vpravo_black():
	REFLECT()
	while not ((cl1.value() < 520 and cl2.value() < 520) or btn.backspace):
		print('cl2=',cl2.value())
		print('cl1=',cl1.value())
		e = (cl1.value()-cl2.value())*-0.3
		mA.run_forever(speed_sp=motor(-speed+e))
		mD.run_forever(speed_sp=motor(speed+e))
		mB.run_forever(speed_sp=-e*0.4)
		mC.run_forever(speed_sp=e*0.4)
	MotorStop()
	return 
	
def nazad_black():
	REFLECT()
	while not ((cl2.value() < 470 and cl3.value() < 470) or btn.backspace):
		print('cl2=',cl2.value())
		print('cl3=',cl3.value())
		e = (cl2.value()-cl3.value())*-0.37
		mB.run_forever(speed_sp=motor(speed-e))
		mC.run_forever(speed_sp=motor(speed+e))
		mA.run_forever(speed_sp=-e*0.4)
		mD.run_forever(speed_sp=-e*0.4)
	MotorStop()
	return 	
		

def pr1(m, e):
	
	mB.reset()
	mC.reset()
	mB.run_to_rel_pos(position_sp=m, speed_sp=e)
	mC.run_to_rel_pos(position_sp=m, speed_sp=e)
	e1 = abs(m*e*0.00007)
	sleep(e1)
	print("e1=",e1)
	MotorStop()
	return m,e

def pr2(m, n):
	mA.reset()
	mD.reset()
	mA.run_to_rel_pos(position_sp=m, speed_sp=n)
	mD.run_to_rel_pos(position_sp=-m, speed_sp=n)
	e1=abs(m*n*0.00007)
	print(e1)
	sleep(e1)
	MotorStop()
	return m==0, e==0

def Rotation(n):
	e1=316*n
	print(e1)
	mB.run_to_rel_pos(position_sp=e1, speed_sp=300)
	mC.run_to_rel_pos(position_sp=-e1, speed_sp=300)
	mA.run_to_rel_pos(position_sp=e1, speed_sp=300)
	mD.run_to_rel_pos(position_sp=e1, speed_sp=300)
	print(e1)
	sleep(e1*300*0.000015)
	MotorStop()
	return n==0

def lin1_4():
	m = 0
	while not btn.backspace:
		e=(470-cl1.value())*0.5
		e1=(470-cl4.value())*0.5
		mB.run_forever(speed_sp=-e)
		mC.run_forever(speed_sp=-e1)
		print(e)
		m = m+1
		if m >= 100:
			break
	MotorStop()
	Sound.tone(200, 200)
	return

def lin2_3():
	m = 0
	while not btn.backspace:
		e=(470-cl2.value())*0.5
		e1=(470-cl3.value())*0.5
		mB.run_forever(speed_sp=e)
		mC.run_forever(speed_sp=e1)
		print(e)
		m = m+1
		if m >= 100:
			break
	MotorStop()
	Sound.tone(200, 200)
	return

def lin3_4():
	m = 0
	while not btn.backspace:
		e=(470-cl3.value())*0.5
		e1=(470-cl4.value())*0.5
		mA.run_forever(speed_sp=e)
		mD.run_forever(speed_sp=e1)
		print(e)
		m = m+1
		if m >= 100:
			break
	MotorStop()
	Sound.tone(200, 200)
	return

def lin1_2():
	m = 0
	while not btn.backspace:
		e=(630-cl1.value())*0.5
		e1=(635-cl2.value())*0.5
		mD.run_forever(speed_sp=e)
		mA.run_forever(speed_sp=-e1)
		print(e)
		print(e1)
		m = m+1
		if m >= 100:
			break
	MotorStop()
	Sound.tone(200, 200)
	return

def lin_black1_4():
	REFLECT()
	sleep(1)
	m = 0
	while not btn.backspace:
		e=(384-cl1.value())*0.5
		e1=(423-cl4.value())*0.5
		mB.run_forever(speed_sp=e)
		mC.run_forever(speed_sp=e1)
		print("e = ", e, "e1 = ", e1)
		m = m +1
		if m>=100:
			break
	MotorStop()
	AMBIENT()
	Sound.tone(1000, 200)
	return

def lin_black2_3():
	REFLECT()
	sleep(1)
	m = 0
	while not btn.backspace:
		e=(486-cl2.value())*0.5
		e1=(471-cl3.value())*0.5
		mB.run_forever(speed_sp=-e)
		mC.run_forever(speed_sp=-e1)
		print("e = ", e, "e1 = ", e1)
		m = m +1
		if m>=100:
			break
	MotorStop()
	AMBIENT()
	Sound.tone(1000, 200)
	return
	
def lin_black1_2():
	REFLECT()
	sleep(1)
	m = 0
	while not btn.backspace:
		e=(460-cl1.value())*0.5
		e1=(460-cl2.value())*0.5
		mA.run_forever(speed_sp=+e1)
		mD.run_forever(speed_sp=-e)
		print("e = ", e, "e1 = ", -(e1))
		m = m +1
		if m>=100:
			break
	MotorStop()
	AMBIENT()
	Sound.tone(1000, 200)
	return
	
def lin_black3_4():
	REFLECT()
	sleep(1)
	m = 0
	while not btn.backspace:
		e=(471-cl3.value())*0.5
		e1=(423-cl4.value())*0.5
		mA.run_forever(speed_sp=-e1)
		mD.run_forever(speed_sp=e)
		print("e = ", e, "e1 = ", e1)
		m = m +1
		if m>=100:
			break
	MotorStop()
	AMBIENT()
	Sound.tone(1000, 200)
	return
	
def lift1(e2, n1):
	d=0
	while not btn.backspace:
		
		if e2==1:
			sendMessage('floor_1')
		if e2==2:
			sendMessage('floor_2')
		if e2==3:
			sendMessage('floor_3')
		if e2==4:
			sendMessage('floor_4')
		print('e2 = ',e2)
		d = getMessage(mailbox)
		#print('m = ',m)
		if d=='stop':
			break
	Sound.tone(200, 400)
	while not btn.backspace:
		
		if n1==1:
			sendMessage('lift_1')
		if n1==2:
			sendMessage('lift_2')
		if n1==3:
			sendMessage('lift_3')
		if n1==4:
			sendMessage('lift_4')
		d = getMessage(mailbox)
		print('m = ',m)
		print('n1 = ',n1)
		if d =='lift_stoped':
			e2 = n1
			break
	print('n1 = ',n1)
	print('d = ',d)
	print('e2 = ',e2)
	return n1,e2

def perevod(r):
	if r=="1":
		f=1
	if r=="2":
		f=2
	if r=="3":
		f=3
	if r=="4":
		f=4
	if r=="5":
		f=5
	if r==-1:
		f=-1
	if r==-2:
		f=-2
	if r==-3:
		f=-3
	if r==-4:
		f=-4
	return r

def Pauza(m):
	sleep(m)
	return

def perevod1(m):
	n = []
	for i in m:
		if i==' ' or i==',' or i=='[' or i==']':
			print('-')
		else:
			n.append(int(i))
	print("n = ", n)
	return n
