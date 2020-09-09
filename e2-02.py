import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import *


#x = symbols('x')


a, b = -1, 1

def trapezo(f, h, xs):
    last = len(xs) - 1
    x=xs[0]
    soma=eval(str(f))
    x = xs[last]
    soma+=eval(str(f))
    tem1=0
    for i, x in enumerate(xs):
        if i not in [0,last]:
            soma += 2 * eval(str(f))
    #soma += 2 * sum([f(x) for i, x in enumerate(xs) if i not in [0, last]])
    return (h / 2) * soma



def chebyshev_primeira_ordem(n):
    if n <= 0:
        return '1'
    if n == 1:
        return 'x'
    return '((2*x)*('+chebyshev_primeira_ordem(n-1)+')-('+chebyshev_primeira_ordem(n-2)+'))'
def chebyshev_segunda_ordem(n):
    if n == 0:
        return "1"
    if n == 1:
        return "2*x"
    return "2*x*("+chebyshev_segunda_ordem(n-1)+")-("+chebyshev_segunda_ordem(n-2)+")"




xv = np.linspace(-1,1,200) #lista de pontos de x
n = 7
f1 = "1/(1+x**2)"

coefs = []
comp_str = ""

y1v=[eval(str(f1)) for x in xv]
plt.plot(xv, y1v, '-g')

for i in range(n):
    y1s=chebyshev_primeira_ordem(2*i)
    
    sol = simplify(y1s+"*"+f1)
    #print(str(sol)+"*",end="")

    h = (b - a) / 2 ** n
    xs = [a + k * h for k in range(2 ** n + 1)]

    div_cima = abs(trapezo(sol, h, xs))
    div_baix = abs(trapezo(y1s+"*"+y1s,h,xs))
    div_ = div_cima / div_baix

    coefs.append(div_)

    y1v=[eval(str(sol)+"*"+str(y1s)) for x in xv] 
    plt.plot(xv, y1v, '-r')

    #print(str(div_)+" + ",end="")
    comp_str += str(sol)+"*"+str(div_)+"+"
comp_str += "0"
print(comp_str,end="\n\n")
print(coefs,end="\n\n")
y1v=[eval(str("1/"+comp_str)) for x in xv]
plt.plot(xv, y1v, '-b')
plt.title('grafico')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.grid()
plt.show()