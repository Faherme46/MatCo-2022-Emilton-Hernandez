
import decimal
from math import factorial
from math import e
import os
from decimal import *

#angulo=float(input("Ingrese el angulo en radianes: "))

    
    






os.system('cls')
xi_1=0.555
xi=0.55
h=0.005
funcion=1/(e**xi)

provisional=0
anterior=0

signo=1
factor=0

errorA=0



for i in range(0,16):
    
    provisional=decimal.Decimal(((decimal.Decimal(funcion)*decimal.Decimal(h**factor))/factorial(factor)))*signo

    
    
    signo*=-1
    factor+=1
    
   
    anterior+=decimal.Decimal(provisional)
    if i==0:
        errorA=1
    else:
        errorA=decimal.Decimal(abs((decimal.Decimal(ant)-decimal.Decimal(anterior))/decimal.Decimal(ant)))
    ant=decimal.Decimal(anterior)
    
    
    print (f"Orden {i}: valor: {anterior} error: {decimal.Decimal(errorA)}")

print(f"\n\n\nEl valor final es {anterior} con error de {errorA}")

