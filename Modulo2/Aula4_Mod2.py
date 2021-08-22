# Aula 4 - Comparações e indexação booleana

#comparação booleana

import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 0, 2])
s = 3

#menor
print('Comparação menor')
print(a < b)
print(a < s)

print('Comparação menor igual')
print(a <= b)
print(a <= s)

print('Comparação igual')
print(a == b)
print(a == s)

#Indexação booleana

cond = a <= 2
d = a[cond]
print('A: ', a)
print('Condição:', cond)
print('D: ', d)

#------------------------------------------------------------

#ciração de array
x = np.array([[1, 2],[3, 4]])
y = np.array([1.5, 3.5])
print('x: \n', x)
print('y: \n', y)

'''print('Comparação de um array com uma escala (>): \n', x > 2)
print('Comparação de um array com uma escala (>=): \n', x >= 2)
print('Comparação de um array com uma escala (<): \n', x < 2)
print('Comparação de um array com uma escala (<=): \n', x <= 2)'''

print('Comparação entre array (==): \n', x == x)
print('Comparação entre arrays (>): \n', x > x)
print('Comparação entre arrays x e y (>): \n', x == y)


x = np.array([[1, 3, 7],[4, 11, 21],[42, 8, 9]])
#indexação booleana retorna os valores de K
k = 10
cond = x > k
print('Condição: \n', cond)
print(f'Elementos maiores que {k}:', x[cond])
print(f'Numero elementos maiores que {k}:', len(x[cond]))

cond = x % 2 == 0 # Numero que divido por 2 o resto é zero. Numeros pares
print('Condição: \n', cond)
print('Numeros pares: \n', x[cond])

#cond = x % 2 != 0 # Numero que divido por 2 o resto diferente zero. Numeros inpares
cond = x % 2 == 1 #  Numero que divido por 2 o resto 1. Numeros inpares
print('Condição: \n', cond)
print('Numeros impares: \n', x[cond])

