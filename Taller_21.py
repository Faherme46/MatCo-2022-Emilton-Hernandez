
import math
import os
import numpy as np

sumaX1=0
sumaX2=0
sumaY=0
sumaX1y=0
sumaX2y=0
sumaX1_X2=0
sumaX1_2=0
sumaX2_2=0

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


def valores(x1,x2,y):
    global sumaX1
    global sumaX2
    global sumaY
    global sumaX1y
    global sumaX2y
    global sumaX1_X2
    global sumaX1_2
    global sumaX2_2
    
    for i in range(len(x1)):
        sumaX1+=x1[i]
        sumaX2+=x2[i]
        sumaY+=y[i]
        sumaX1_2+=x1[i]**2
        sumaX2_2+=x2[i]**2
        sumaX1y+=x1[i]*y[i]
        sumaX1_X2+=x1[i]*x2[i]
        sumaX2y+=x2[i]*y[i]


x1=[1,1,2,3,1,2,3,3]
y=[1.6,3,1.1,1.2,3.2,3.3,1.7,0.1]
x2=[-1,0,0,1,1,2,2,0]

valores(x1,x2,y)
values={"sumax1":sumaX1,"sumax2":sumaX2,"sumaY":sumaY,"sumax1y":sumaX1y,
"sumax2y":sumaX2y,"sumax1_x2":sumaX1_X2,"sumax1_2":sumaX1_2,"sumax2_2":sumaX2_2}


l1=[len(x1),sumaX1,sumaX2]
l2=[sumaX1,sumaX1_2,sumaX1_X2]
l3=[sumaX2,sumaX1_X2,sumaX2_2]

A=np.array([l1,l2,l3])
B=np.array([[sumaY],[sumaX1y],[sumaX2y]])

aLista=resolver3x3(A,B)
print(aLista)
os.system('pause')
a0=aLista[0]
a1=aLista[1]
a2=aLista[2]

sumaSt=0
sumaSr=0
pY=sumaY/len(y)

for i in range(len(y)):
    sumaSt+=(y[i]-pY)**2
    sumaSr+=(y[i]-a0-a1*x1[i]-a2*x2[i])**2

r=math.sqrt((sumaSt-sumaSr)/sumaSt)*100

os.system('cls')
print("La funcion quedaria: \n",
f"Z= {round(a0,4)} +{round(a1,4)}X + {round(a2,4)} Y\n",
"Coeficiente de correlacion: ", round(r,4))