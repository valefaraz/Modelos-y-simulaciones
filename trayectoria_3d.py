from time import time
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
import math
from mpl_toolkits.mplot3d import Axes3D
import numpy

plt.style.use('ggplot')
x_data=[0]
y_data=[0]
z_data=[100]

figure = pyplot.figure()
ax = figure.add_subplot(projection='3d')

global x
global y
global z
global t
t = 0
global contador
contador=0

def viento():
    None


def grafica(frame):
    v0=40 #m/s
    alpha=45 #grados ° angulo de lanzamiento
    b=0
    h=100
    g=9.8
    globals()['t'] = globals()['t'] +0.05

    x=v0*math.cos(alpha)**math.cos(b)*globals()['t']
    y=v0*math.cos(alpha)**math.sin(b)*globals()['t']
    z=h+v0*math.sin(alpha)*globals()['t']-(1/2*g*(globals()['t'])**2)
    if z<=0:    
        x=v0*math.cos(alpha)**math.cos(b)*globals()['t']
        
        y=v0*math.cos(alpha)**math.sin(b)*globals()['t']
        animacion.pause()
    y_data.append(y)
    x_data.append(x)
    z_data.append(z)


    ax.plot(x_data, y_data, z_data, label='parametric curve')

plt.ylabel("Y")
plt.xlabel("X")
plt.title("Pelota desde un edificio")
#plt.xlim(-10,300)
#lt.ylim(-5,200)
animacion = FuncAnimation(figure,grafica, interval=1)
pyplot.show()