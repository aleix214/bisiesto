# coding: utf­8

def bisiesto(num):
	if(num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
		print("Si es bisiesto")
	else:
		print("No es bisiesto")

bisiesto(2004)
bisiesto(2300)
bisiesto(1995)


