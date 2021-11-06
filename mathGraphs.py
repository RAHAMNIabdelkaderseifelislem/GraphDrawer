#pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

def draw(x,y):        
    plt.plot(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('THE GRAPH')
    plt.show()

def inter(x,z,t):

    a = []
    b = []
    while(x<z):
        a.append(x)
        y = eval(t)
        b.append(y)
        x = x + 0.1
    
    a.append(x)
    b.append(eval(t))

    draw(a,b)


x0 = int(input("Enter first x : "))
x1 = int(input("Enter last x : "))
equation = input("your equation y = f(x) :  y = ")
inter(x0,x1,equation)
