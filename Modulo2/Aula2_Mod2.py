#Indexação de Arrays
#acessar dados do array
import numpy as np

a = np.array([1,2,3])
print('Posicao 1 do array', a[1])

b = np.array([[1,2,3],[4,5,6]])
print('Array b', b)
print('Posicao 1 da Linha e 2 da coluna do array', b[1,2])

c = np.array([22,35,45,19,55])
print('Array c', c[1:3])

print ('A: ')
A = np.array([[1,2,3,4],[5,6,7,8],[9,1,11,12]])
print(A)

print('B:')
B = A[:2,1:3]
print(B)

x = np.linspace(start=10,stop=100,num=10)
print('x: ', x)
print('x: ', x.shape)

print('Primeiro elemento: ', x[0])
print('Segundo elemento: ', x[1])
print('Ultimo elemento: ', x[9])
print('Ultimo elemento: ', x[-1])

#Slicing - retorna varios valores
print('x: ', x)

print('dois primeiro elemento: ', x[0:2])
print('dois primeiro elemento: ', x[:2])
print('dois ultimo elemento: ', x[-2:])

#slicing 2D

x = x.reshape(2,5)
print('x: \n', x)
print('primeira linha, segunda coluna: ', x[0,1])
print('segunda linha, penultima coluna: ', x[1, -2])
print('ultima linha, ultima coluna: ', x[1, 4])
print('ultima linha, ultima coluna: ', x[-1, -1])

#slicing extração de subarrays
print(x)
print('x: \n', x)
print('primeira linha inteira: ', x[0, :])
print('primiera linha, segunda e quarta coluna: ', x[0, 1:4])
print('ultima coluna inteira: ', x[:, -1])
print('ultima coluna inteira: ', x[:, [-1]])

#Atenção compartilhamento de de memoria em subarrays

z = np.array([1,2,3])
print('z antes:', z)

y = z[:2]
y[0] = -100 # alteração do valor em y altera o valor de z

print('z depois:', z)
#como evitar isso
print('Como eveitat a alteração no array z')
z = np.array([1,2,3])
print('z antes:', z)
y = z[:2].copy()  # copia z
y[0] = -100 # alteração do valor em y altera o valor de z
print('z depois:', z)






