#Aula 1 Modulo 2
#Introdução de Array - Biblioteca de computação Científca Numpy

import numpy as np

#criar um Array de 1D - 1 dimensão

l = [1, 2 ,3]
x = np.array(l)
print('x:', x)
print('Shape x: ', x.shape)
type(x)

#criar um Array 2D -  2 dimensões :matrix 3 X 3
z = [1, 2, 3], [2,3,4]
y = np.array(z)
print('x:', y)
print('Shape x: ', y.shape)
type(y)

a = np.array([[1,2],[2,3,4],[3,4,5]])
print('Array criado:\n', a)
print('Shape:', a.shape)

#criar um Array 2D -  3 dimensões :matrix 3 X 3
b =  np.array([[1,2,3],[2,3,4],[3,4,5]])
print('Array criado:\n', b)
print('Shape:', b.shape)


#Array contendo apenas zeros - np.zeros
dim = (2,2)
c = np.zeros(dim)
print('C:\n ',c)
print('Shape:\n ',c.shape)

help(np.zeros) #modo de funcionamento da função np.zeros

#Array contendo apenas 1 - np.ones

size = (2,2)
x = np.ones(size)
print('C:\n ',x)
print('Shape:\n ',x.shape)


#criação de valow denrto do intervalo - np.linspace
#valores uniformes entr 5 e 15
x_min, x_max = 5, 15
x = np.linspace(start=x_min,stop=x_max,num=6)
print('x:\n ', x)
print('Shape:\n ', x.shape)

#criação de matriz indentidade - np.eye

n = 4
x = np.eye(n)
print('x:\n ',x)
print('Shape:\n ',x.shape)

#criando valores aleatórios - np.random
x = np.random.random(size=(2, 3))
print('x:\n ', x)
print('Shape:\n ', x.shape)













