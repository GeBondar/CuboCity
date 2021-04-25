#!/usr/bin/python3

from robotLibs import *
from robotNet import *
from robotVM import *

robotName = "2"

mailbox = initMailBox()
AMBIENT()

m1 = getMessage(mailbox)
while not btn.backspace:
	#Sound.tone(1000, 200)
	m1 = getMessage(mailbox)
	print(m1[0])
	if m1[0]=='1':
		break

Sound.tone(200, 200)
sleep(5)
code = [2]
runCode(code)
pr1(-50, 150)

#while not btn.backspace:
#	Sound.tone(1000, 200)
#	m1 = getMessage(mailbox)
#	print("m1 = ", m1[0])
#	if m1[0]=='2':
#		break

while not btn.backspace:
	m1 = getMessage(mailbox)
	print(m1)
	print(len(m1))
	print("0 =", m1[0])
	if len(m1) > 0:
		if m1[0] == robotName:
			nazad()
			pr1(-30,150)
			print('')
			sendMessage(robotName)
			code = m1[1:len(m1)]
			print("code = ",code)
			n = perevod1(code)
			runCode(n)
			break
		elif m == "free":
			print('')
			sendMessage(robotName)

