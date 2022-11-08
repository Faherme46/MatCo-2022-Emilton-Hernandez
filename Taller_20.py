
import math
import os
import numpy as np

sumaX4=0
sumaXy=0
sumaX2=0
sumaX3=0
sumaX=0
sumaY=0
sumaX2Y=0

def resolver3x3(A,B):
    casicero = 1e-15 


    A = np.array(A,dtype=float) 


    AB = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)


    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]


    for i in range(0,n-1,1):
        
        columna = abs(AB[i:,i])
        dondemax = np.argmax(columna)
        
        
        if (dondemax !=0):
            
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
            
    AB1 = np.copy(AB)


    for i in range(0,n-1,1):
        pivote = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB2 = np.copy(AB)


    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila,0-1,-1):
        pivote = AB[i,i]
        atras = i-1 
        for k in range(atras,0-1,-1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
        
        AB[i,:] = AB[i,:]/AB[i,i]
    X = np.copy(AB[:,ultcolumna])
    X = np.transpose([X])
    X=X.tolist()
    l=list()
    
    for i in X:
        
        l.append(i[0])
        
    return l


def valores(x,y):
    global sumaX4
    global sumaXy
    global sumaX2
    global sumaX3
    global sumaX
    global sumaY
    global sumaX2Y

    for i in x:
        sumaX2+=i**2
        sumaX+=i
        sumaX3+=i**3
        sumaX4+=i**4
    
    for i in range(len(x)):
        sumaXy+=x[i]*y[i]
        sumaX2Y+=y[i]*x[i]**2
        sumaY+=y[i]


x=[0,1,2,3,4,5,6]
y=[-0.9,0,2,4.5,8.3,13,18]

valores(x,y)

l1=[len(x),sumaX,sumaX2]
l2=[sumaX,sumaX2,sumaX3]
l3=[sumaX2,sumaX3,sumaX4]

A=np.array([l1,l2,l3])
B=np.array([[sumaY],[sumaXy],[sumaX2Y]])

aLista=resolver3x3(A,B)

a0=aLista[0]
a1=aLista[1]
a2=aLista[2]

sumaSt=0
sumaSr=0
pY=sumaY/len(y)

for i in range(len(y)):
    sumaSt+=(y[i]-pY)**2
    sumaSr+=(y[i]-a0-a1*x[i]-a2*x[i]**2)**2

r=math.sqrt((sumaSt-sumaSr)/sumaSt)*100

os.system('cls')
print("La funcion quedaria: \n",
f"Y= {round(a0,4)} +{round(a1,4)}x + {round(a2,4)} x^2\n",
"Coeficiente de correlacion: ", round(r,4))