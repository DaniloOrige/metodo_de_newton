#import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

def func(x):
    return (x**3 - 5*x**2 + 17*x + 21)
def dfunc(x):
    return (3*x**2 - 10*x + 17)


#def func(x): 
#    return (x*np.e(-x) - 0.2)

#def dfunc(x):
#    return (np.e(-x)*(1-x))

def newton(x0, e= 1e-6, max_iters= 50):
    k = 0
    
    xk_vec = []
    iter_vec = []
    func_vec = []
    dfunc_vec = []
    xk = x0
    while (abs(func(xk)) > e) or (k > max_iters):

        xp = xk - func(xk)/dfunc(xk)
        k += 1
        xk = xp

        xk_vec.append(xk)
        iter_vec.append(k)
        func_vec.append(func(xk))
        dfunc_vec.append(dfunc(xk))


    return xk_vec, iter_vec, func_vec, dfunc_vec

resultado = newton(x0=-1)


tabela = pd.DataFrame(
    {
        'iteração': resultado[1],
        'xk': resultado[0],
        'função(xk)': resultado[2],
        'dfunção(xk)': resultado[3]
    }
)
tabela = tabela.set_index('iteração')
print(tabela)

