# Implementation of Black-Scholes formula in Python
import numpy as np
from scipy.stats import norm
from confInit import conf


# Calculando o Preço Teórico
def bs(r, S, X, T, sigma, tipo="c"):
    '''Calcula o Preço Justo pelo modelo de Black-Scholes da Call e da Put.
        Parâmetros:
            r: taxa de juros
            S: Preço atual do ativo-objeto
            K: Strike (Preço de Exercício)
            T: Tempo (em dias)
            sigma: Volatilidade
            tip: c - Call ou p - Put
    '''
    d1, d2, x_e = conf(r, S, X, T, sigma)
    try:
        if tipo == "c":
            price = S * norm.cdf(d1, 0, 1) - X * x_e * norm.cdf(d2, 0, 1)
        elif tipo == "p":
            price = X * x_e * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1)
        return round(price, 3)
    except:
        print("Por favor, confirme o tipo da opção, 'c' - Call 'p' - Put.")


# Delta 
def delta(r, S, X, T, sigma, tipo="c"):
    '''Calcula o Delta de uma Opção
        Parâmetros:
            r: taxa de juros
            S: Preço atual do ativo-objeto
            K: Strike (Preço de Exercício)
            T: Tempo (em dias)
            sigma: Volatilidade
            tip: c - Call ou p - Put
    '''
    d1, __, __ = conf(r, S, X, T, sigma)
    try:
        if tipo == "c":
            delta_calc = norm.cdf(d1, 0, 1)
        elif tipo == "p":
            delta_calc = -norm.cdf(-d1, 0, 1)
        return round(delta_calc, 3)
    except:
        print("Por favor, confirme o tipo da opção, 'c' - Call 'p' - Put.")


# Gamma    
def gama(r, S, X, T, sigma, tipo="c"):
    '''Calcula o Gama de uma Opção.
        Parâmetros:
            r: taxa de juros
            S: Preço atual do ativo-objeto
            K: Strike (Preço de Exercício)
            T: Tempo (em dias)
            sigma: Volatilidade
            tip: c - Call ou p - Put
    '''
    d1, __, __ = conf(r, S, X, T, sigma)
    try:
        gamma_calc = norm.pdf(d1, 0, 1) / (S*sigma*np.sqrt(T))
        return round(gamma_calc, 3)
    except:
        print("Por favor, confirme o tipo da opção, 'c' - Call 'p' - Put.")

# Vega
def vega(r, S, X, T, sigma, tipo="c"):
    '''Calcula o Vega de uma Opção.
        Parâmetros:
            r: taxa de juros
            S: Preço atual do ativo-objeto
            K: Strike (Preço de Exercício)
            T: Tempo (em dias)
            sigma: Volatilidade
            tip: c - Call ou p - Put
    '''
    d1, __, __ = conf(r, S, X, T, sigma)
    try:
        vega_calc = S * norm.pdf(d1, 0, 1) * np.sqrt(T)
        return round(vega_calc, 3)
    except:
        print("Por favor, confirme o tipo da opção, 'c' - Call 'p' - Put.")

# Theta
def theta(r, S, X, T, sigma, tipo="c"):
    '''Calcula o Theta de uma Opção.
        Parâmetros:
            r: taxa de juros
            S: Preço atual do ativo-objeto
            K: Strike (Preço de Exercício)
            T: Tempo (em dias)
            sigma: Volatilidade
            tip: c - Call ou p - Put
    '''
    d1, d2, __ = conf(r, S, X, T, sigma)
    try:
        if tipo == "c":
            theta_calc = -S * norm.pdf(d1, 0, 1) * sigma / (2 * np.sqrt(T)) - r * X * np.exp(-r * T ) * norm.cdf(d2, 0, 1)
        elif tipo == "p":
            theta_calc = -S * norm.pdf(d1, 0, 1) * sigma / (2 * np.sqrt(T)) + r * X * np.exp(-r * T) * norm.cdf(-d2, 0, 1)
        return round(theta_calc/252, 3)
    except:
        print("Por favor, confirme o tipo da opção, 'c' - Call 'p' - Put.")

# Rho
def rho(r, S, X, T, sigma, tipo="c"):
    '''Calcula o Rho de uma Opção.
        Parâmetros:
            r: taxa de juros
            S: Preço atual do ativo-objeto
            K: Strike (Preço de Exercício)
            T: Tempo (em dias)
            sigma: Volatilidade
            tip: c - Call ou p - Put
    '''
    d1, d2, __ = conf(r, S, X, T, sigma)
    try:
        if tipo == "c":
            rho_calc = X * T* np.exp(-r * T) * norm.cdf(d2, 0, 1)
        elif tipo == "p":
            rho_calc =-K * T * np.exp(-r * T) * norm.cdf(-d2, 0, 1)
        return round(rho_calc * 0.01, 3)
    except:
        print("Por favor, confirme o tipo da opção, 'c' - Call 'p' - Put.")

# moneyness
def moneyness(S, X, preco, tipo):
    '''Calcula o Rho de uma Opção.
        Parâmetros:
            S: Preço atual do ativo-objeto
            X: Strike (Preço de Exercício)
            preco: Preço Teórico
            tip: c - Call ou p - Put
    '''
    try:
        if tipo == 'c':
            if X > S:
                moneyness_calc = 'OTM'
            elif X < S:
                moneyness_calc = 'ITM'
            else:
                moneyness_calc = 'ATM'
            if moneyness_calc == 'ITM':
                vi = S - X
                ve = preco - vi
            else:
                vi = 0
                ve = preco - vi
        elif tipo == 'p':
            if X > S:
                moneyness_calc = 'ITM'
            elif X < S:
                moneyness_calc = 'OTM'
            else:
                moneyness_calc = 'ATM'
            if moneyness_calc == 'ITM':
                vi = X - S
                ve = preco - vi
            else:
                vi = 0
                ve = preco - vi
            
        return moneyness_calc, vi, ve
    except:
        print("Por favor, confirme o tipo da opção, 'c' - Call 'p' - Put.")