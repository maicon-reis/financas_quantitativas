# Inicializando as bibliotecas
import numpy as np
from scipy.stats import norm

def conf(r, S, X, T, sigma):
    d1 = (np.log(S/X) + (r+sigma**2/2)*T)/(sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    x_e = np.exp(-r * (T))
    return d1, d2, x_e

 