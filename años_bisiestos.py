# coding: utf­8

a=int(input("Dime un año:   "))
if(a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
 print("Si es bisiesto")
else:
 print("No es bisiesto")

