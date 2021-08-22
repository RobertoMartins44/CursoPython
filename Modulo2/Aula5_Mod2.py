#Aula 5 Outra operações utéis no numpy
#Matriz para vetor
import numpy as np
x = np.array([[1, 3, 7],[4, 11, 21],[42, 8, 9]])
#reshape: transforma matriz em um vetor coluna
#(3, 3) para (9, 1) 3*3 = 9 --> 9 * 1 = 9
print('Matriz para um vetor coluna: \n', x.reshape(1, 9))  #Erro se   x.reshape(1, 8)
#print('Matriz para um vetor coluna: \n', x.reshape(9, 1))

#Transformação de Matirz (Linha para coluna)
print("x transporta: \n ", x.T)

#np.sum
print('X: \n', x)
print('Soma de todos elemento do array x: \n', np.sum(x))
print('X: \n', x)
print('Soma de x por linhas x: \n', np.sum(x, axis=0))
print('X: \n', x)
print('Soma de x por Coluna x: \n', np.sum(x, axis=1))

#np.mean
print('X: \n', x)
print('média de todos elemento do array x: \n', np.mean(x))
print('X: \n', x)
print('média de x por linhas x: \n', np.mean(x, axis=0))
print('X: \n', x)
print('média de x por Coluna x: \n', np.mean(x, axis=1))


#np.where - indentificação dos indices onde uma data condição
#é atendida. Uso conjunto com indexação booleana

cond = x % 2 == 0 # numeros pares
print('Condição: \n', cond)
i, j = np.where(cond) #indices x[i,j] = x[cond]
print('Indice i (linha) x: \n', i)
print('Indice j (coluna) x: \n', j)

#indexação booleana e slicing: selecionar linhas de x que possuem algum numero par

print('X: \n', x)

cond = x % 2 == 0 # numeros pares
print('Condição: \n', cond)
#se houver alguma condição TRUE na linha, a soma será > 0
i_row = np.where(np.sum(cond, axis=1))[0]
print('Indices das linhas que possuem numeros pares: \n', i_row)
print('Indices das linhas que possuem numeros pares: \n', x[i_row, :])

