from cmath import sqrt
import imp
import math


import os

def tryInt(txt:str):#metodo para leer datos enteros

    isTry=True
    while isTry:
        try:
            x=int(input(txt))
            if x==0:
                return -1
            if x<0:
                x*=-1
        except:
            print("No es valido, ingrese nuevamente el dato")
            os.system('pause')
        else:
            isTry=False
            return x



primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,97]

def determinarRaiz(num):
    numeros=[]
    temp=num
    while temp!=1:
        for i in primos:
            
            while temp%i==0:
                temp/=i
                numeros.append(i)
            if i==97 and temp!=1:
                print("El numero probablemente sea primo")
                return
    fuera=1
    dentro=1
    salen=0
    
    for i in primos:
        x=numeros.count(i)
        parejas=x//2
        solo=x%2
        if parejas!=0: 
            salen=i**parejas
            fuera*=salen
        if solo==1:
            dentro*=i

    if fuera!=1:
        mensaje=f"Respuesta: {fuera} Raiz({dentro}) "    
        
    else:
        mensaje="No puede simplificarse por descomposicion factorial "
    
    if dentro==1:
        mensaje=f"Respuesta por descomposicion: {fuera}  "
    print(mensaje)
        

numero=0
while numero!=-1:

    os.system('cls')
    print("*****RAIZ POR DESCOMPOSICION FACTORIAL*****")
    numero=tryInt("Ingrese el numero para hallar su raiz (0 para salir): \n")
    if numero!=-1:
        print("\nRespuesta exacta: ",round(math.sqrt(numero),2)) 
    if numero in primos:
        print("El numero es primo, no se puede simplificar la raiz")
    elif numero !=-1:
        determinarRaiz(numero)
        
    os.system('pause')

