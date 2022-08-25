from math import factorial


#angulo=float(input("Ingrese el angulo en radianes: "))
angulo=1.047197551

errorS=(0.5*(10**-8))*100


anterior=1
signo=-1
factor=0
provisional=0
errorA=100
i=0
while errorA>=errorS:
    factor+=2
    provisional=((angulo**factor)/factorial(factor))*signo
    valor=anterior+provisional
    
    signo*=-1
    errorA=((abs(valor-anterior))/valor)*100
    anterior=valor
    i+=1
    

print("El coseno es: ",valor," fue hallado en ",i," iteraciones")
