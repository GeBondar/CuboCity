from robotLibs import *

def runCode(code):
	i = 0
	code.append(0)
	
	while code[i] != 0:
		print('code[',i,']=',code[i],'  code[',i+1,']',code[i+1])
		i += runOperation(code[i-1],code[i],code[i+1])
		if i>=1:
			n1 = code[i-1]
		i += 1
		print('i=',i)
	print("END")

def runOperation(n1,c,n):
	print('c=',c,' n=',n)
	if c == 0:
		print("OOPS: zero!")
		return -1
		
	elif c == 1:
		print("back")
		print(c)
		nazad()
		pr1(65, 200)
		nazad()
		pr1(65, 200)
		nazad()
		return 0
		
	elif c == 2:
		print("forvard_led")
		print(c)
		print(n)
		if n==1:
			vpered_led()
			pr1(-65, 200)
			vpered_led()
			pr1(-65, 200)
			pr1(-600, 150)
		else:
			vpered_led()
			pr1(-65, 200)
			vpered_led()
			pr1(-65,200)
			vpered_led()
		return 0
		
	elif c == 3:
		print("Left")
		print(c)
		vlevo()
		pr2(60, 150)
		vlevo()
		pr2(60, 150)
		vlevo()
		return 0
		
	elif c == 4:
		print("Right")
		vpravo()
		pr2(-65, 150)
		vpravo()
		pr2(-65, 150)
		vpravo()
		return 0
		
	elif c == 5:
		print("ot_nazad")
		print("n1 = ", n1)
		if n1==1:
			pr1(-40, 150)
		elif n1==2:
			pr1(40, 150)	
		elif n1==3:
			pr2(-45, 150)
		elif n1==4:
			pr2(45, 150)
		return 0
	
	elif c == 6:
		print('V_lift', "n = ", n)
		if n==1:
			pr1(600, 150)
			lin_black2_3()
		elif n==2:
			pr1(-600, 150)
			lin_black1_4()
		elif n==3:
			pr2(600, 150)
			lin_black3_4()
		elif n==4:
			pr2(-600, 150)
			lin_black1_2()
		return 1

	
	elif c == 7:
		print("iz_lifta")
		print("n = ", n)
		if n==1:
			pr1(650, 150)
		elif n==2:
			pr1(650, 150)
		elif n==3:
			pr2(650, 150)
		elif n==4:
			pr2(-650, 150)
		return 1

	elif c == 8:
		print("LIFT")
		m1=perevod(n)
		if e2==1:
			m = 1
		if e2==2:
			m = 2
		lift1(m, m1)
		print('lift_m = ', m)
		print("lift_m1 = ", m1)
		return 1
		
	elif c == 9:
		print("Rotation")
		print(n)
		m=perevod(n)
		print(m)
		Rotation(m)
		return 1
	
	elif c == 10:
		print('ot/ezd')
		pr1(100, 150)

	else:
		print("OOPS: Wrong code!!")
		return 0

