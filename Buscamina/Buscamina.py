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
    else:
        print('Unknown key')

class celda:
    def __init__(self):
        self.valor=0
        self.Bomba=False

import numpy as np
import random as rd
class celda:
    def __init__(self):
        self.valor=0
        self.Bomba=False


############################## Parametros #################################333
N=6
B=6

############################## Codigo ###################


celdas=[]
for k in range(N*N):
    celdas.append(celda())
tablero=np.zeros((N,N),dtype=int) 
cord=[]
for i in range(N):
    for j in range(N):
        cord.append((i,j))

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

#print("Tablero de Bombas")            
#print(tablero)
#print("Tableros de Cant de Bombas")
#print(tablero2)
#print("Buscamina")
#print(tablero3)


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

print("")
final=[]
for i in range(N):
    for j in range(N):
        a=inte[j]+inte[i]
        final.append(a)

print("")
for i in range(N):
    for j in range(N):
        Data=tablero3[i,j]
        k=getK(i,j)
        
        det=Cuadrados[k]
        det.info=Data
        det.area=final[k]
        Cuadrados[k]=det

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
    global cordinate
    vec=Vecinos(i,j)
    cordinate.append((i,j))
  
    for cor in vec:

        x,y=cor

        #print(tablero3[x,y],cor)

        if tablero3[x,y]>0 and tablero3[x,y]<9 and ((x,y) not in cordinate):
            #print("entre1:"+str(x)+","+str(y))
            cordinate.append((x,y))

        elif tablero3[x,y]==0 and ((x,y) not in cordinate ):
            #print("entre2:"+str(x)+","+str(y))
            Isla(x,y)


def main():
    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width = 600
    height = 600

    window = glfw.create_window(width, height, "Buscamina", None, None)

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
    gpuBandera= es.toGPUShape(bs.createTextureQuad("Bandera.png"), GL_REPEAT, GL_NEAREST)
    gpuGarfio= es.toGPUShape(bs.createTextureQuad("Garfio.png"), GL_REPEAT, GL_NEAREST)
    gpuBomba= es.toGPUShape(bs.createTextureQuad("Bomba.png"), GL_REPEAT, GL_NEAREST)
    gpuCero= es.toGPUShape(bs.createTextureQuad("Cero.png"), GL_REPEAT, GL_NEAREST)
    gpuUno= es.toGPUShape(bs.createTextureQuad("Uno.png"), GL_REPEAT, GL_NEAREST)
    gpuDos= es.toGPUShape(bs.createTextureQuad("Dos.png"), GL_REPEAT, GL_NEAREST)
    gpuTres= es.toGPUShape(bs.createTextureQuad("Tres.png"), GL_REPEAT, GL_NEAREST)
    gpuCuatro= es.toGPUShape(bs.createTextureQuad("Cuatro.png"), GL_REPEAT, GL_NEAREST)
    gpuCinco= es.toGPUShape(bs.createTextureQuad("Cinco.png"), GL_REPEAT, GL_NEAREST)
    gpuSeis= es.toGPUShape(bs.createTextureQuad("Seis.png"), GL_REPEAT, GL_NEAREST)
    gpuSiete= es.toGPUShape(bs.createTextureQuad("Siete.png"), GL_REPEAT, GL_NEAREST)
    gpuOcho= es.toGPUShape(bs.createTextureQuad("Ocho.png"), GL_REPEAT, GL_NEAREST)
 
    gpuMuerte= es.toGPUShape(bs.createTextureQuad("YouAreDead.png"), GL_REPEAT, GL_NEAREST)
    gpuWin= es.toGPUShape(bs.createTextureQuad("Win.png"), GL_REPEAT, GL_NEAREST)
    gpuLose= es.toGPUShape(bs.createTextureQuad("Lose.png"), GL_REPEAT, GL_NEAREST)

    for i in range(len(Cuadrados)):
        a=Cuadrados[i]
        a.gpu=gpuCelda
        


    t0 = glfw.get_time()
    t=0

    Press=False
    Press2=False
    Muerte=False
    cant=0
    Win=False
    end=False
    
    while not glfw.window_should_close(window):

        t1 = glfw.get_time()
        dt = t1 - t0
        t0 = t1
        t+=dt
        # Using GLFW to check for input events
        glfw.poll_events()

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)

        x,y =controller.posmouse

        #print(x,y)
        

        glUseProgram(pipelineTexture.shaderProgram)

        for i in range(N):
            for j in range(N):
                med=abs(-1+(1/N))
                lon=2/N
                transform=tr.matmul([tr.translate(-med+lon*j,med-lon*i,0),tr.scale(2/N,2/N,2/N)])
                glUniformMatrix4fv(glGetUniformLocation(pipelineTexture.shaderProgram, "transform"), 1, GL_TRUE,transform)
                k=getK(i,j)
                quad=Cuadrados[k]
                pipelineTexture.drawShape(quad.gpu)
      
        
        F=glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_RIGHT)==glfw.PRESS

        for cuad in Cuadrados:
            if cuad.Dentro(x,y)==True and end==False:
                if  F==True and cuad.Celda==True and Press==False and cuad.Final==False:
                    cuad.Celda=False
                    cuad.Bandera=True
                    cuad.gpu=gpuBandera
                elif  F==True and  cuad.Bandera==True and Press==False and cuad.Final==False:
                    cuad.Bandera=False
                    cuad.Garfio=True
                    cuad.gpu=gpuGarfio
               
                elif  F==True and  cuad.Garfio==True and Press==False and cuad.Final==False:
                    cuad.Garfio=False
                    cuad.Celda=True
                    cuad.gpu=gpuCelda

        Press=F


        F=glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT)==glfw.PRESS
        
        for cuad in Cuadrados:
            if cuad.Dentro(x,y)==True and end==False:
                if  F==True :
                    cuad.Final=True
                    n=cuad.info
                   
                    if n==666:
                        cuad.gpu=gpuBomba
                        Muerte=True
                        end=True
                    elif n==0:
                        global cordinate
                        cuad.gpu=gpuCero
                        k=Cuadrados.index(cuad)
                        i,j=getIJ(k)
                        Isla(i,j)
                        for cor in cordinate:
                            X,Y=cor
                            k=getK(X,Y)
                            inf=Cuadrados[k].info
                            Cuadrados[k].Final=True
                            if inf==0:
                                Cuadrados[k].gpu=gpuCero
                            elif inf==1:
                                Cuadrados[k].gpu=gpuUno
                            elif inf==2:
                                Cuadrados[k].gpu=gpuDos
                            elif inf==3:
                                Cuadrados[k].gpu=gpuTres
                            elif inf==4:
                                Cuadrados[k].gpu=gpuCuatro
                            elif inf==5:
                                Cuadrados[k].gpu=gpuCinco
                            elif inf==6:
                                Cuadrados[k].gpu=gpuSeis
                            elif inf==7:
                                Cuadrados[k].gpu=gpuSiete
                            elif inf==8:
                                Cuadrados[k].gpu=gpuOcho
                        cordinate=[] 
                    elif n==1:
                        cuad.gpu=gpuUno
                    elif n==2:
                        cuad.gpu=gpuDos
                    elif n==3:
                        cuad.gpu=gpuTres
                    elif n==4:
                        cuad.gpu=gpuCuatro
                    elif n==5:
                        cuad.gpu=gpuCinco
                    elif n==6:
                        cuad.gpu=gpuSeis
                    elif n==7:
                        cuad.gpu=gpuSiete
                    else:
                        cuad.gpu=gpuOcho

        Press2=F

        for cuad in Cuadrados:
            if cuad.Final==True :
                cant+=1
                if not Muerte and cant==N*N-B:
                    Win=True
                    end=True
        cant=0

        if Win:
            transform=tr.matmul([tr.scale(1.5,1.5,1.5)])
            glUniformMatrix4fv(glGetUniformLocation(pipelineTexture.shaderProgram, "transform"), 1, GL_TRUE,transform)
            pipelineTexture.drawShape(gpuWin)

            
            
       
        if Muerte:
            transform=tr.matmul([tr.scale(1.5,1.5,1.5)])
            glUniformMatrix4fv(glGetUniformLocation(pipelineTexture.shaderProgram, "transform"), 1, GL_TRUE,transform)
            pipelineTexture.drawShape(gpuMuerte)

            transform=tr.matmul([tr.scale(1,1,1)])
            glUniformMatrix4fv(glGetUniformLocation(pipelineTexture.shaderProgram, "transform"), 1, GL_TRUE,transform)
            pipelineTexture.drawShape(gpuLose)

            
        if (controller.fillPolygon):
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)



        glfw.swap_buffers(window)
    glfw.terminate()

main()
    
  