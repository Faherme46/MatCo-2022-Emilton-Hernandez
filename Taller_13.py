from math import factorial
import os


menu=["Caso 1 ","Caso 2 ","SALIR" ]

def noValida():

    
    print("Ingreso no valido, intente nuevamente")
    os.system('pause')

def tryInt(txt:str):#metodo para leer datos enteros
    isTry=True
    while isTry:
        try:
            x=int(input(txt))
        except:
            noValida()
        else:
            isTry=False
            return x

    
def imprimirMatriz(z):
    for i in z:
            mensaje=""
            for j in i:
                x=str(j)+"  "
                mensaje+=x
            print(mensaje)   
   
def verMenu():
    
    os.system('cls')
    print("*****MENU PRINCIPAL*****")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}" )



result=True

while result:
    
    os.system('cls')
    verMenu()
    opc=input("Elija una opcion: ")
    if opc=="1":
        os.system('cls')
        print("****Producto de vectores****\n")
        l1=tryInt("Ingrese la longitud de los vectores: ")
        

        vector1=[]
        print("Ingrese uno a uno los elementos del vector 1")
        for i in range(l1):
            x=tryInt(": ")
            vector1.append(x)
        
        vector2=[]
        print("\nIngrese uno a uno los elementos del vector 2")
        for i in range(l1):
            x=tryInt(": ")
            vector2.append(x)

        suma=0
        for i in range(l1):
            suma+=vector1[i]*vector2[i]

        os.system('cls')
        print("El producto escalar de los vectores es: ",suma)

    elif opc=="2":
        os.system('cls')
        print("****Operaciones con matrices****")
        # Af=2
        # Ac=2
        # Bf=3
        # Bc=2
        
        Af=tryInt("Ingrese el numero de FILAS de A: ")
        Ac=tryInt("Ingrese el numero de COLUMNAS de A: ")
        Bf=tryInt("Ingrese el numero de FILAS de B: ")
        Bc=tryInt("Ingrese el numero de COLUMNAS de B: ")
        

    

        # B=[[1, 2], [2, 1],[3,2]]
        # A=[[2,4],[4,2]]

        #crear matriz A
        os.system('cls')
        print(f"Ingrese los datos para A ({Af}x{Ac})\n")
        A=[]
        for i in range(Af):
            f=[]
            for j in range(Ac):
                f.append(tryInt(f"a{i}{j}: "))
            A.append(f)

        os.system('cls')
        print("La matriz A queda asi: ")
        imprimirMatriz(A)
        
        os.system('pause')
        #Crear matriz B
        os.system('cls')
        print(f"Ingrese los datos para B ({Bf}x{Bc})\n")
        B=[]
        for i in range(Bf):
            f=[]
            for j in range(Bc):
                f.append(tryInt(f"b{i}{j}: "))
            B.append(f)

        os.system('cls')
        print("La matriz B queda asi: ")
        imprimirMatriz(B)
        
        
        
        
        menu2=["Operacion a","Operacion b","Operacion c","Operacion d","Salir"]
        bandera=True
        while bandera:
            os.system('pause')
            os.system('cls')
            for i in range(len(menu2)):
                print(f"{i+1}. {menu2[i]}" )
            
            opcion=input("Ingrese la operacion que desea:")
            os.system('cls')
            if opcion=="1":
                A3=A
                for i in range(len(A3)):
                    for j in range(len(A3[i])):
                        A3[i][j]*=3

                print("El resuyltado de la matriz 3A es: ")
                imprimirMatriz(A3)
                
            
            elif opcion=="2":
                B4=B
                for i in range(len(B4)):
                    for j in range(len(B4[i])):
                        B4[i][j]*=3

                print("El resuyltado de la matriz 3A es: ")
                imprimirMatriz(B4)
                
            
            elif opcion=="3":
                #A+B
                suma=[]
                if Ac!=Bc or Af!=Bf:
                    print("Las matrices no se pueden sumar")
                else:
                    for i in range(len(A)):
                        fila=[]
                        for j in range(len(A[i])):
                            x=A[i][j]+B[i][j]
                            fila.append(x)
                        suma.append(fila)
                    print("A+B resulta: ")
                    imprimirMatriz(suma)

            elif opcion=="4":
                #BxA
                suma=[]
                if Af!=Bc:
                    print("Las matrices no se pueden multiplicar")
                else:
                    for i in range(Bf):
                        fila=[]
                        for k in range(Ac):
                            s=0
                            for j in range(Af):
                                x=(B[i][j]*A[j][k])
                                s+=x
                                
                                
                            fila.append(s)
                        suma.append(fila)
                    print("AXB resulta: ")
                    imprimirMatriz(suma)
            elif opcion=="5":
                bandera=False    
            else: 
                noValida()

            
        

        


    else:
        noValida()
    
    os.system('pause')

