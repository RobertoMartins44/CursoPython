#Operações Aritiméticas - numpy array

# criar dois arrays
import numpy as np

x = np.ones((2, 2)) # função vista na aula 2
y = np.eye(2)       # função vista na aula 2
print('x\n', x)
print('x\n', y)

#soma de arrays
print('Soma Array x + Array y:\n', x + y)
#soma de arrays com broadcasting
print('Soma Array x + Array y:\n', x + 2)

#subtração arrays
print('subtração Array x - Array y:\n', x - y)
#subtração de arrays com broadcasting
print('subtração Array x - Array y:\n', x - 2)

#Divisão de arrays

#print('Divisão Array x / Array y:\n', x / y) #Observei que aqui vamor ter retorno 'inf' 9Valor divido por 0
#Divisão de arrays com broadcasting

print('Divisão Array x / Array y:\n', x / 2)

#Quando brodcasting não funciona
#np.array([1,2,3]) + np.array([1,2]) # dados inconsistentes
#ValueError: operands could not be broadcast together with shapes (3,) (2,)
np.array([1,2,3]) + np.array([1]) # ok

#Soma, Subtração e divisão

print('Combinação de operações', (x+y) / (x-2))


#multiplicação de array

#multiplicação arrays
print('multiplicação Array x * Array y:\n', x * y)
#multiplicação de arrays com broadcasting
print('multiplicação Array x * Array y:\n', x * 2)

#x = 10 * np.ones((5, 5))
#print(x)

#multiplicação Matricial np.dot, @ e .dot
print('Multiplicação Matricial (np.dot): \n', np.dot(x, y))
print('Multiplicação Matricial (@: \n', x @ y)
print('Multiplicação Matricial (.dot: \n', x.dot(y))


''' Exemplo solução de um sistema de equação
    a +2b = 7
    3a - 2b = -11
    Solução análitica>: (a, b) = (-1, 4)

    Matricialmente, este problema tem a seguinte forma:
    Ax = c. onde,
    x = [a,b]
    A = [1,2], [3,2]
    c = [7,-11]
    solução numerica: x = inv(A) @ c 
        
'''
#definição do problema

A = np.array([[1, 2],[3, -2]])
c = np.array([[7], [-11]])
print('A: \n ',A)
print('c: \n ',c)
#Solução:

x = np.dot(np.linalg.inv(A), c)  # ou
x = np.linalg.inv(A) @ c#
print('a, b', x.ravel())





















