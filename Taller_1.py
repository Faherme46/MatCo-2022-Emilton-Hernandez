import os 

#funciones


B=set()
A=set()
x=0

# A={1,3,5,4,6}
# B={2,4,6}
# x=1

menu=["Registrar los conjuntos", "Union","Interseccion","Diferencia A entre B","Diferencia B entre A" , "Diferencia simetrica","SALIR" ]
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

def Reescribir():
    global A
    global B
    global x
    x=1
    B=set()
    A=set()
    cA=tryInt("Registre la cardinalidad del conjunto A: ")
    print(f"Registre los elementos: ({cA})")
    for i in range(cA):
        A.add(tryInt(":"))
    
    os.system('cls')
    
    cB=tryInt("Registre la cardinalidad del conjunto B: ")
    print(f"Registre los elementos: ({cB})")
    for i in range(cB):
        B.add(tryInt(":"))
    
    return ("Conjuntos registrados")
    
def verMenu():
    
    os.system('cls')
    print("*****MENU PRINCIPAL*****")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}" )

def opcionElegida(opc):
    os.system('cls')
    result=True
    global x
    
    if opc=="1":
        print(Reescribir())

    elif opc=="2":
        if x==0:
            print("No se han agregado conjuntos")
            return result
        u=union(A,B)
        print("La union resultante es: ",u," Su cardinalidad es: ",len(u))
    elif opc=="3":
        if x==0:
            print("No se han agregado conjuntos")
            return result
        inter=interseccion(A,B)
        print("La interseccion resultante es:", inter," Su cardinalidad es: ",len(inter))
    elif opc=="4":
        if x==0:
            print("No se han agregado conjuntos")
            return result
        d=diferenciaAB(A,B)
        print("La diferencia resultante es:", d," Su cardinalidad es: ",len(d))
    elif opc=="5":
        if x==0:
            print("No se han agregado conjuntos")
            return result
        d=diferenciaBA(A,B)
        print("La diferencia resultante es:", d," Su cardinalidad es: ",len(d))
    elif opc=="6":
        if x==0:
            print("No se han agregado conjuntos")
            return result
        d=simetrica(A,B)
        print("La diferencia resultante es:", d," Su cardinalidad es: ",len(d))    
    
    elif opc=="7":
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

def diferenciaBA(A:set,B:set):
    c=set()
    for i in B:
        if not(i in A):
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

B=set()
A=set()


isActive=True
while isActive:
    verMenu()
    isActive=opcionElegida(input(":)"))
    os.system('pause')
