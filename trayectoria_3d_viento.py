import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
import math
import random as r
import numpy as np

plt.style.use('ggplot')

x_data=[0]
y_data=[0]
z_data=[100]
x_data2=[0]
y_data2=[0]
z_data2=[100]
x_data3=[0]
y_data3=[0]
z_data3=[100]
x_data4=[0]
y_data4=[0]
z_data4=[100]
x_data5=[0]
y_data5=[0]
z_data5=[100]
x_data6=[0]
y_data6=[0]
z_data6=[100]


figure = pyplot.figure()
ax = figure.add_subplot(projection='3d')

global x
global y
global z
global t
global contador
global contador2
global flag
global velocidad_viento
global duracion_viento
global angulo
t = 0
flag=False
contador=0
contador2=0


def viento():

#calculamos las variables estocasticas del viento
    for n in range(5):
        globals()['velocidad_viento'+str(n)]=r.uniform(10.0, 30.0)         #m/s
        globals()['duracion_viento'+str(n)]=r.random()                     #segundos de 0 a 1
        globals()['angulo_viento'+str(n)]=r.randrange(361)                 # de 0° a 360°


def grafica(frame):
    global x0
    global y0
    global z0
    global z
    global x
    global y
    v0=40                   #m/s
    alpha=45                #grados ° angulo de lanzamiento
    b=0
    h=100
    g=9.8
    h_max=60

    globals()['t'] = globals()['t'] +0.05   #tiempo tics de 0.05
    
    #sin influencia del viento
    if globals()['flag']==False:
        x=v0*math.cos(alpha)**math.cos(b)*globals()['t']
        y=v0*math.cos(alpha)**math.sin(b)*globals()['t']
        z=h+(v0*math.sin(alpha)*globals()['t']-(1/2*g*(globals()['t'])**2))
        y_data.append(y)
        x_data.append(x)
        z_data.append(z)
        y_data2.append(y)
        x_data2.append(x)
        z_data2.append(z)
        y_data3.append(y)
        x_data3.append(x)
        z_data3.append(z)
        y_data4.append(y)
        x_data4.append(x)
        z_data4.append(z)
        y_data5.append(y)
        x_data5.append(x)
        z_data5.append(z)
        y_data6.append(y)
        x_data6.append(x)
        z_data6.append(z)
    
    # con influencia del viento   
    
    if z > ((2/3)*h_max)+100 and z>0 or globals()['flag']== True :
            globals()['flag']=True
            
            #puntos de la trayectoria con la influencia de viento
            
            x=v0*math.cos(alpha)**math.cos(b)*globals()['t']- math.cos(globals()['angulo_viento2'])*globals()['velocidad_viento2']*globals()['duracion_viento2']
            y=v0*math.cos(alpha)**math.sin(b)*globals()['t']- math.sin(globals()['angulo_viento2'])*globals()['velocidad_viento2']*globals()['duracion_viento2']
            z=h+(v0*math.sin(alpha)*globals()['t']-(1/2*g*(globals()['t'])**2))
            y_data.append(y)
            x_data.append(x)
            z_data.append(z)

            x=v0*math.cos(alpha)**math.cos(b)*globals()['t']- math.cos(globals()['angulo_viento1'])*globals()['velocidad_viento1']*globals()['duracion_viento1']
            y=v0*math.cos(alpha)**math.sin(b)*globals()['t']- math.sin(globals()['angulo_viento1'])*globals()['velocidad_viento1']*globals()['duracion_viento1']    
            y_data2.append(y)
            x_data2.append(x)
            z_data2.append(z)

            x=v0*math.cos(alpha)**math.cos(b)*globals()['t']- math.cos(globals()['angulo_viento0'])*globals()['velocidad_viento0']*globals()['duracion_viento0']
            y=v0*math.cos(alpha)**math.sin(b)*globals()['t']- math.sin(globals()['angulo_viento0'])*globals()['velocidad_viento0']*globals()['duracion_viento0']
            
            y_data3.append(y)
            x_data3.append(x)
            z_data3.append(z)

            x=v0*math.cos(alpha)**math.cos(b)*globals()['t']- math.cos(globals()['angulo_viento3'])*globals()['velocidad_viento3']*globals()['duracion_viento3']
            y=v0*math.cos(alpha)**math.sin(b)*globals()['t']- math.sin(globals()['angulo_viento3'])*globals()['velocidad_viento3']*globals()['duracion_viento3']
            
            y_data4.append(y)
            x_data4.append(x)
            z_data4.append(z)
            x=v0*math.cos(alpha)**math.cos(b)*globals()['t']- math.cos(globals()['angulo_viento4'])*globals()['velocidad_viento4']*globals()['duracion_viento4']
            y=v0*math.cos(alpha)**math.sin(b)*globals()['t']- math.sin(globals()['angulo_viento4'])*globals()['velocidad_viento4']*globals()['duracion_viento4']
            
            y_data5.append(y)
            x_data5.append(x)
            z_data5.append(z)
            
    if z<=0:    
        animacion.pause()

    ax.plot(x_data, y_data, z_data, label='parametric curve',color="blue")
    ax.plot(x_data2, y_data2, z_data2, label='parametric curve',color="red")
    ax.plot(x_data3, y_data3, z_data3, label='parametric curve',color="yellow")
    ax.plot(x_data4, y_data4, z_data4, label='parametric curve',color="green")
    ax.plot(x_data5, y_data5, z_data5, label='parametric curve',color="black")

if __name__ == "__main__":
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.title("Pelota desde un edificio")
    viento()
    animacion = FuncAnimation(figure,grafica, interval=1)
    pyplot.show()