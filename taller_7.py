from math import factorial
import os
menu=["Caso 1 ","Caso 2 ","SALIR" ]

#angulo=float(input("Ingrese el angulo en radianes: "))

    
    
   
def verMenu():
    
    os.system('cls')
    print("*****MENU PRINCIPAL*****")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}" )



result=True
num=0.85
errorS=(0.5*(10**-8))*100


anterior=1
signo=-1
factor=0
provisional=0
errorA=100
i=0
anteriorReal=1

while result:
    
    os.system('cls')
    verMenu()
    opc=input("Elija una opcion:")
    if opc=="1":
        anterior=1
        signo=-1
        factor=0
        provisional=0
        errorA=100
        i=0
        
        while errorA>=errorS:
            factor+=1
            provisional=((num**factor)/factorial(factor))*signo
            valor=anterior+provisional
            
            signo*=-1
            errorA=((abs(valor-anterior))/valor)*100
            anterior=valor
            i+=1
        
        print (f"El valor es: {valor} con error de {errorA} y se encontro en {i} iteraciones ")
    elif opc=="2":
        anterior=1
        factor=0
        provisional=0
        errorA=100
        i=0
        anteriorReal=1
        while errorA>=errorS:
            factor+=1
            provisional=(num**factor)/factorial(factor)
            debajo=anterior+provisional
            valor=1/debajo
           
            errorA=((abs(valor-anteriorReal))/valor)*100
            anterior=debajo
            anteriorReal=valor
            i+=1
        print (f"El valor es: {valor} con error de {errorA} y se encontro en {i} iteraciones ")
    
    else:
        print("No es valido")
        os.system('pause')
    
    os.system('pause')

