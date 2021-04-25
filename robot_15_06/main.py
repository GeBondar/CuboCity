#!/usr/bin/python3

from robotVM import *
mbox = initMailBox()
RobotName = "R1"
AMBIENT()
#Sound.tone(200, 200)
#while not btn.backspace:
	#code = getMessage(mbox)
	
	#if code!=0:
#code = [2,5,3,7,1,6,4,8,9,4,9,2]
#code = [2,5,18]
#code = [19,20,9,2,2,5]
#code = [4,8,2,5,9,1,2,5,18]
code = [2,2,2]
#code = [21,6,9,1,4,8,2]
print(code)
runCode(code)
#break
REFLECT()
#Atack_of_Titan()


