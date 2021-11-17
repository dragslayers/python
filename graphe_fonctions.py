import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return -x**2 + 5*x

def g(x):
    return (x-7)**2-15

#on veut tracer les courbes de ces fonctions
x=np.linspace(0,5,10)
    
plt.plot(x,f(x),"bx-",label="f(x)")
plt.plot(x,g(x),"ro-",label="g(x)")
plt.legend()

plt.show()

