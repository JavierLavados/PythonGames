import numpy as np
import random as rd

N=5



class NodoLista:
    def __init__(self,info,sgte=None):
        self.info=info
        self.sgte=sgte
class Cola:
    def __init__(self):
        self.primero=None
        self.ultimo=None
    def enq(self,x):
        p=NodoLista(x)
        if self.ultimo is not None: # cola no vacía, agregamos al final
            self.ultimo.sgte=p
            self.ultimo=p
        else: # la cola estaba vacía
            self.primero=p
            self.ultimo=p
    def deq(self):
        assert self.primero is not None
        x=self.primero.info
        if self.primero is not self.ultimo: # hay más de 1 elemento
            self.primero=self.primero.sgte
        else: # hay solo 1 elemento, el deq deja la cola vacía
            self.primero=None
            self.ultimo=None
        return x
    def is_empty(self):
        return self.primero is None
    def datos(self):
        if self.ultimo is not None: # cola no vacía
            p=self.primero
            lista=[p.info]
            while p is not self.ultimo:
                lista.append(p.sgte.info)
                p=p.sgte
            return lista
        else: # la cola estaba vacía
            return None
tabla=np.zeros((N,N),dtype=int)
tabla[N-1,0]=1
tabla[N-2,0]=1
tabla[N-3,0]=1
class Snake:
    def __init__(self):
        a=Cola()
        a=Cola()
        a.enq((N-1,0))
        a.enq((N-2,0))
        a.enq((N-3,0))
        self.Body=a
        self.Life=True
        self.Right=False
        self.Left=False
        self.Up=True
        self.Down=False
        self.Head=(N-3,0)
        self.ExCola=(0,0)
    def Datos(self):
        return self.Body.datos()

    def Adelante(self):
        self.ExCola=self.Body.deq()
        x,y=self.Head
        NewHead=((x-1)%N,y)
        self.Body.enq(NewHead)
        self.Head=NewHead

        self.Up=True
        self.down=False
        self.Right=False
        self.Left=False

    def Atras(self):
        self.ExCola=self.Body.deq()
        x,y=self.Head
        NewHead=((x+1)%N,y)
        self.Body.enq(NewHead)
        self.Head=NewHead

        self.Up=False
        self.down=True
        self.Right=False
        self.Left=False
    
    def Derecha(self):
        self.ExCola=self.Body.deq()
        x,y=self.Head
        NewHead=(x,(y+1)%N)
        self.Body.enq(NewHead)
        self.Head=NewHead

        self.Up=False
        self.down=False
        self.Right=True
        self.Left=False
    
    def Izquierda(self):
        self.ExCola=self.Body.deq()
        x,y=self.Head
        NewHead=(x,(y-1)%N)
        self.Body.enq(NewHead)
        self.Head=NewHead

        self.Up=False
        self.down=False
        self.Right=False
        self.Left=True

    def Actualizar(self):
        a=self.Datos()
        for cor in a:
            x,y=cor
            tabla[x,y]=1
        x, y=self.ExCola
        tabla[x,y]=0
    def comer(self):
        x,y=self.Head
        if self.Up==True:
            cor=((x-1)%N,y)
            self.Body.enq(cor)
            self.Head=cor
        elif self.Down==True:
            cor=((x+1)%N,y)
            self.Body.enq(cor)
            self.Head=cor
        elif self.Left==True:
            cor=(x,(y-1)%N)
            self.Body.enq(cor)
            self.Head=cor
        if self.Right==True:
            cor=(x,(y+1)%N)
            self.Body.enq(cor)
            self.Head=cor
    
def Fruta():
    lista=[]
    for i in range(N):
        for j in range(N):
            if tabla[i,j]!=1:
                lista.append((i,j))
    x,y=rd.choice(lista)
    tabla[x,y]=2

        
snake=Snake()
print(snake.Datos())
#Fruta()
print("serpiente inicial")
print(tabla)


print("Movimiento")
snake.comer()
print(snake.Datos())
print(snake.Head)
print(snake.ExCola)
snake.Adelante()
snake.Actualizar()
print(tabla)









