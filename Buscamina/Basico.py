import numpy as np
import random as rd
class celda:
    def __init__(self):
        self.valor=0
        self.Bomba=False

N=4
celdas=[]
for k in range(N*N):
    celdas.append(celda())
tablero=np.zeros((N,N),dtype=int) 
cord=[]
for i in range(N):
    for j in range(N):
        cord.append((i,j))
B=3
Bombas=[]
i=0
while i <B:
    A=rd.choice(cord)
    if A not in Bombas:
        Bombas.append(A)
        i+=1
for i in range(N):
    for j in range(N):
        if (i,j) in Bombas:
            tablero[i,j]=1


tablero2=np.zeros((N,N),dtype=int) 

for i in range(N):
    for j in range(N):
        if i<N-1 and i>0 and j<N-1 and j>0:
            n=tablero[i+1,j]+tablero[i-1,j]+tablero[i,j+1]+tablero[i,j-1]+tablero[i+1,j+1]+tablero[i+1,j-1]+tablero[i-1,j-1]+tablero[i-1,j+1]
            tablero2[i,j]=n 

        elif i==0 and j==0:
            n=tablero[i+1,j]+tablero[i+1,j+1]+tablero[i,j+1]
            tablero2[i,j]=n 

        elif i==N-1 and j==0:
            n=tablero[i-1,j]+tablero[i-1,j+1]+tablero[i,j+1]
            tablero2[i,j]=n
        
        elif i==0 and j==N-1:
            n=tablero[i+1,j]+tablero[i,j-1]+tablero[i+1,j-1]
            tablero2[i,j]=n

        elif i==N-1 and j==N-1:
            n=tablero[i-1,j]+tablero[i-1,j-1]+tablero[i,j-1]
            tablero2[i,j]=n

        elif i==0 and j>0 and j<N-1:
            n=tablero[i+1,j]+tablero[i,j+1]+tablero[i,j-1]+tablero[i+1,j+1]+tablero[i+1,j-1]
            tablero2[i,j]=n 
        
        elif i==N-1 and j>0 and j<N-1:
            n=tablero[i-1,j]+tablero[i,j+1]+tablero[i,j-1]+tablero[i-1,j-1]+tablero[i-1,j+1]
            tablero2[i,j]=n 

        elif i>0 and i<N-1 and j==0:
            n=tablero[i+1,j]+tablero[i-1,j]+tablero[i,j+1]+tablero[i+1,j+1]+tablero[i-1,j+1]
            tablero2[i,j]=n 
        
        elif i>0 and i<N-1 and j==N-1:
            n=tablero[i+1,j]+tablero[i-1,j]+tablero[i,j-1]+tablero[i+1,j-1]+tablero[i-1,j-1]
            tablero2[i,j]=n 

tablero3=np.zeros((N,N),dtype=int) 
for i in range(N):
    for j in range(N):
        if tablero[i,j]==1:
            tablero3[i,j] = 666
        else:
            tablero3[i,j]=tablero2[i,j]

print("Tablero de Bombas")            
print(tablero)
print("Tableros de Cant de Bombas")
print(tablero2)
print("Buscamina")
print(tablero3)


class Celdas:
    def __init__(self):
        self.info=None
        self.Celda=True
        self.Bandera=False
        self.Garfio=False
        self.Final=False
        self.area=[0,0,0,0] # x1,x2,y1,y2
    def Dentro(self,x,y):
        xi,xf,yi,yf=self.area
        if x>xi and x<xf and y>yi and y<yf :
            return True 
        else:
            return False

def getK(i,j):
    return i * N + j

def getIJ(k):
    i = k // N
    j = k % N
    return (i, j)

Cuadrados=[]
for n in range(N*N):
    celda=Celdas()
    Cuadrados.append(celda)



intervalo=600/N
inte=[]
for i in range(0,N):
    a=[intervalo*i,intervalo*(i+1)]
    inte.append(a)
#print(inte)
print("")
final=[]
for i in range(N):
    for j in range(N):
        a=inte[j]+inte[i]
        final.append(a)
#print(final)
print("")
for i in range(N):
    for j in range(N):
        Data=tablero3[i,j]
        k=getK(i,j)
        #print("k: "+str(k))
        #print("Data: "+str(Data))
        #print("Pos: "+ str(i)+","+str(j))
        det=Cuadrados[k]
        det.info=Data
        det.area=final[k]
        Cuadrados[k]=det
#print([c.area for c in Cuadrados])


#print(Cuadrados[2].Dentro(400,75))

def Vecinos(i,j):

    if i<N-1 and i>0 and j<N-1 and j>0:
        n=[(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i+1,j-1),(i-1,j-1),(i-1,j+1)]
        return n

    elif i==0 and j==0:
        n=[(i+1,j),(i+1,j+1),(i,j+1)]
        return n

    elif i==N-1 and j==0:
        n=[(i-1,j),(i-1,j+1),(i,j+1)]
        return n
        
    elif i==0 and j==N-1:
        n=[(i+1,j),(i,j-1),(i+1,j-1)]
        return n

    elif i==N-1 and j==N-1:
        n=[(i-1,j),(i-1,j-1),(i,j-1)]
        return n

    elif i==0 and j>0 and j<N-1:
        n=[(i+1,j),(i,j+1),(i,j-1),(i+1,j+1),(i+1,j-1)]
        return n
        
    elif i==N-1 and j>0 and j<N-1:
        n=[(i-1,j),(i,j+1),(i,j-1),(i-1,j-1),(i-1,j+1)]
        return n

    elif i>0 and i<N-1 and j==0:
        n=[(i+1,j),(i-1,j),(i,j+1),(i+1,j+1),(i-1,j+1)]
        return n 
        
    elif i>0 and i<N-1 and j==N-1:
        n=[(i+1,j),(i-1,j),(i,j-1),(i+1,j-1),(i-1,j-1)]
        return n


cordinate=[]
def Isla (i,j):
    vec=Vecinos(i,j)
    cordinate.append((i,j))
    print("recursion")
    print(i,j)
    print(vec)
    for cor in vec:
        x,y=cor
        if tablero3[x,y]>0 and tablero3[x,y]<9 and ((x,y) not in cordinate):       
            cordinate.append((x,y))
        elif tablero3[x,y]==0 and ((x,y) not in cordinate ):     
               
            Isla(x,y)



print("weveo")

Isla(0,0)
for cor in cordinate:
    tablero3[cor[0],cor[1]]=20
print(tablero3) 

#tablero4=np.zeros((N,N),dtype=tuple) 
#for i in range(N):
 #   for j in range(N):
  #      tablero4[i,j]=(i,j)
   #     vec=Vecinos(i,j)
    #    print(str(i)+" , "+ str(j))
     #   print(vec)
#print(tablero4)


