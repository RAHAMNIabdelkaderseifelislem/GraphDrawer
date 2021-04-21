import matplotlib.pyplot as plt

def draw(x,y):        
    plt.plot(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('THE GRAPH')
    plt.show()

x0 = int(input("Enter first x : "))
x1 = int(input("Enter last x : "))
equation = input("your equation y = f(x) :  y = ")
y = []
z = []
for x in range(x0,x1,1):
    y.append(eval(equation))
    z.append(x)
draw(z,y)