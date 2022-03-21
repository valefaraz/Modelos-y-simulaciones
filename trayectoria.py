from time import time
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
import math


plt.style.use('ggplot')
x_data=[0]
y_data=[100]


figure = pyplot.figure()
line, = pyplot.plot_date(x_data,y_data, '-')

global x
x=0
global y
y=0
global t
t = 0

def grafica(frame,x=0):
    v0=40 #m/s
    alpha=45 #grados ° angulo de lanzamiento

    h=100
    g=9.8
    globals()['t'] = globals()['t'] +0.1

    
    #globals()['x'] = globals()['x'] +1
    #globals()['y'] = a*globals()['x']**2+b*globals()['x']+c
    #x_data.append(globals()['x'])
    #y_data.append(globals()['y'])
    
    x= v0*math.cos(alpha)*globals()['t']
    y= h+v0*math.sin(alpha)*globals()['t']-(1/2*g*(globals()['t'])**2)
    
    if y<=0:
        y=0
        x= v0*math.cos(alpha)*globals()['t']
        animacion.pause()
    y_data.append(y)
    #x=round(int(x),0)
    x_data.append(round(x,2))

    #print(round(int(x),0))

    line.set_data(x_data, y_data)
    
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,


plt.xlim(-10,300)
plt.ylim(-5,200)
animacion = FuncAnimation(figure,grafica,interval= 10)
pyplot.show()

