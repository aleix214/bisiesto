# coding: utf­8

num=int(input("Dime un año:   "))
if(num % 4 == 0 and num % 100 != 0 or num % 400 == 0):
 print("Si es bisiesto")
else:
 print("No es bisiesto")

