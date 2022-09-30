




from tempfile import tempdir


def imprimirMatriz(z):
    for i in z:
            mensaje=""
            for j in i:

                x=str(round(j,2))+"  "
                # if j==-0:
                    
                #     x=str(round(-j,2))+"  "
                # else:
                #     x=str(round(-j,2))+"  "
                mensaje+=x
            
            print(mensaje)
    return ''   


def matInv(A):
    F=len(A)
    
    ident=[]
    for i in range(F):
        temp=[]
        for j in range(F):
            temp.append(0)
        temp.insert(i,1)
        temp.pop()
        ident.append(temp)
  
        
    
        
    
    for i in range(F):
        A[i].extend(ident[i])
    
    C=len(A[0])
    
    for i in range(F):
        pivot=A[i][i]
        for j in range(C):
            A[i][j]/=pivot
        
        
        for l in range(F):
            if l!=i:
                factorM=A[l][i]
                for k in range(C):
                    a=A[i][k]
                    next=factorM*a*-1
                    A[l][k]+=next

    for i in range(F):
        for j in range(F):
            A[i].pop(0)



    return A




A=[ [3,2,2],
    [4,1,-3],
    [1,0,-2]]

B=[[ 1, 2, 0, 4],
   [ 2, 0,-1,-2],
   [ 1, 1,-1, 0],
   [ 0, 4, 1, 0]]

print("La inversa de la matriz A es:")
print(imprimirMatriz(matInv(A)))


print("La inversa de la matriz B es:")
print(imprimirMatriz(matInv(B)))


    
