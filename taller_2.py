import os 

#funciones


# B=set()
# A=set()
x=0

A={6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
B={0,2,4,6,8,10,14,12,16,18,20,24,22}
C={1,4,8,10,12,18,20}
D={2,3,5,7,11,13,17,19,23,29,31,37,41,43}
# x=1

menu=["Operacion A","Operacion B","Operacion C", "Operacion D","SALIR" ]
def noValida():

    os.system('cls')
    print("Opcion no valida, intente nuevamente")
    os.system('pause')

def tryInt(txt:str):#metodo para leer datos enteros
    isTry=True
    while isTry:
        try:
            x=int(input(txt))
        except:
            print("No es valido, ingrese nuevamente el dato")
            os.system('pause')
        else:
            isTry=False
            return x
    

    
def verMenu():
    
    os.system('cls')
    print("*****MENU PRINCIPAL*****")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}" )

def opcionElegida(opc):
    os.system('cls')
    result=True
    
    
    if opc=="1":
       s=simetrica(C,D)
       r=interseccion(s,B)
       print("Resulta: ",r)

    elif opc=="2":
        i=interseccion(A,C)
        u=union(i,B)
        print("El resultado es: ",u)

    elif opc=="3":

        u=union(B,D)
        d=diferenciaAB(u,C)
        print("El resultado es: ", d)

    elif opc=="4":
        d=diferenciaAB(A,B)
        i=interseccion(A,D)
        s=simetrica(d,i)
        print("El resultado es:", s)

    
    elif opc=="5":
        result=not(bool(input("S para salir, ENTER para no salir\n")))
    else:
        noValida()
    
    return result   


#operaciones



def union(A:set,B:set):
    c=set()
    for i in A:
        c.add(i)
    for i in B:
        c.add(i)
    
    return c

def interseccion(A:set,B:set):
    c=set()
    for i in A:
        if i in B:
            c.add(i)
    
    return c

def diferenciaAB(A:set,B:set):
    c=set()
    for i in A:
        if not(i in B):
            c.add(i)
    
    return c



def simetrica(A:set,B:set):
    c=set()
    e=union(A,B)
    d=interseccion(A,B)
    for i in e:
        if not(i in d):
            c.add(i)
    return c

#main




isActive=True
while isActive:
    verMenu()
    isActive=opcionElegida(input(":)"))
    os.system('pause')