import datetime as dt

def criaRelatorio(ativo, X, S, preco, delta, gama, theta, vega, rho, moneyness, vi, ve, tipo):
    date = dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        
    print('#' * 50)
    print('#', f'Resultado para o Strike R$ {X}'.center(46), '#')
    print('#' * 50)
    print('#',' ' * 46, '#')
    print('#',f" Ativo: {ativo.upper()}.SA".ljust(46, ' '), '#')
    print('#',f" Preço Atual: {S}".ljust(46, ' '), '#')
    print('#',' ' * 46, '#')
    if tipo == 'c':
        print('#',f" CALL".ljust(46, ' '), '#')
    elif tipo == 'p':
        print('#',f" PUT".ljust(46, ' '), '#')
    print('#',f" Preço Teórico: R$ {preco}".ljust(46, ' '), '#')
    print('#',' ' * 46, '#')
    print('#',f" Delta: {delta}".ljust(46, ' '), '#')
    print('#',f' Gama: {gama}%'.ljust(46, ' '), '#')
    print('#',f' Theta (R$): {theta}'.ljust(46, ' '), '#')
    print('#',f' Vega: {vega}'.ljust(46, ' '), '#')
    print('#',f' Rho: {rho}'.ljust(46, ' '), '#')
    print('#',' ' * 46, '#')
    print('#',f' Moneyness: {moneyness}'.ljust(46, ' '), '#')
    print('#',f' Valor Intrínseco: R$ {round(vi, 2)}'.ljust(46, ' '), '#')
    print('#',f' Valor Extrínseco: R$ {round(ve, 2)} ({round(ve/S * 100, 1)}%)'.ljust(46, ' '), '#')
    print('#',' ' * 46, '#')
    print('#',f'Data: {date} '.rjust(46, ' '), '#')
    print('#',' ' * 46, '#')
    print('#','by k4k0_r3i5'.center(46), '#')
    print('#' * 50)