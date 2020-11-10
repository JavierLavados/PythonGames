import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import sys
from PIL import Image

import transformations as tr
import basic_shapes as bs
import easy_shaders as es

class GPUShape:
    def __init__(self):
        self.vao = 0
        self.vbo = 0
        self.ebo = 0
        self.texture = 0
        self.size = 0

# A class to store the application control
class Controller:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.posmouse = (0.0,0.0)
        self.fillPolygon = True

controller = Controller()

def cursor_pos_callback(window, x, y): # da la posición del mouse en pantalla con coordenadas
    global controller
    controller.posmouse = (x,y)
#def mouse_button_callback( window, button, action, mods)


def on_key(window, key, scancode, action, mods):
    
    if action != glfw.PRESS:
        return
    
    global controller
     
    if key == glfw.KEY_SPACE:
        controller.fillPolygon = not controller.fillPolygon

    elif key == glfw.KEY_ESCAPE:
        glfw.set_window_should_close(window, True)
    


##################
import numpy as np
import random as rd

N=30



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
##################
    


        
snake=Snake()
#print("serpiente inicial")
#print(tabla)


#rint("Movimiento")
#snake.Adelante()
#snake.Actualizar()
#print(tabla)

class Celdas:
    def __init__(self):
        self.info=None
        self.Comida=False
        self.Lugar=True
        self.Final=False
        self.gpu=None

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


def main():
    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width = 600
    height = 600

    window = glfw.create_window(width, height, "Snake", None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, on_key)

    glfw.set_cursor_pos_callback(window, cursor_pos_callback)

    # A simple shader program with position and texture coordinates as inputs.
    pipelineTexture = es.SimpleTextureTransformShaderProgram()
    pipelineNoTexture = es.SimpleTransformShaderProgram()
    # Telling OpenGL to use our shader program

    # Setting up the clear screen color
    glClearColor(0.25, 0.25, 0.25, 1.0)

    # Enabling transparencies
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Creating shapes on GPU memory
    #es.toGPUShape(bs.createTextureQuad("Celda.png"), GL_REPEAT, GL_NEAREST)

    gpuCelda= es.toGPUShape(bs.createTextureQuad("Celda.png"), GL_REPEAT, GL_NEAREST)
    gpuSnake= es.toGPUShape(bs.createTextureQuad("snake.png"), GL_REPEAT, GL_NEAREST)


    for i in range(len(Cuadrados)):
       a=Cuadrados[i]
       a.gpu=gpuCelda
        


    t0 = glfw.get_time()

    time=0
    

    
    while not glfw.window_should_close(window):

        t1 = glfw.get_time()
        dt = t1 - t0
        t0 = t1
        
        # Using GLFW to check for input events
        glfw.poll_events()

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)

        x,y =controller.posmouse

        #print(x,y)
        

        glUseProgram(pipelineTexture.shaderProgram)

        for i in range(N):
            for j in range(N):
                if tabla[i,j]==1:
                    med=abs(-1+(1/N))
                    lon=2/N
                    transform=tr.matmul([tr.translate(-med+lon*j,med-lon*i,0),tr.scale(2/N,2/N,2/N)])
                    glUniformMatrix4fv(glGetUniformLocation(pipelineTexture.shaderProgram, "transform"), 1, GL_TRUE,transform)
                    pipelineTexture.drawShape(gpuSnake)
                else:
                    med=abs(-1+(1/N))
                    lon=2/N
                    transform=tr.matmul([tr.translate(-med+lon*j,med-lon*i,0),tr.scale(2/N,2/N,2/N)])
                    glUniformMatrix4fv(glGetUniformLocation(pipelineTexture.shaderProgram, "transform"), 1, GL_TRUE,transform)
                    pipelineTexture.drawShape(gpuCelda)


        time=+dt



        if (glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS):
            
            snake.Izquierda()
            snake.Actualizar()
        if (glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS):
            snake.Derecha()
            snake.Actualizar()
        if (glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS):
            snake.Adelante()
            snake.Actualizar()
        if (glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS):
            snake.Atras()
            snake.Actualizar()
        if (glfw.get_key(window, glfw.KEY_ENTER) == glfw.PRESS):
            snake.comer()
            snake.Actualizar()

                    
                    


       # for i in range(N):
        #    for j in range(N):
         #       med=abs(-1+(1/N))
          #      lon=2/N
           #     transform=tr.matmul([tr.translate(-med+lon*j,med-lon*i,0),tr.scale(2/N,2/N,2/N)])
            #    glUniformMatrix4fv(glGetUniformLocation(pipelineTexture.shaderProgram, "transform"), 1, GL_TRUE,transform)
             #   k=getK(i,j)
              #  quad=Cuadrados[k]
               # pipelineTexture.drawShape(quad.gpu)
      
     
            
        if (controller.fillPolygon):
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)



        glfw.swap_buffers(window)
    glfw.terminate()

main()
    
  