#Aula 3 Tipos de Dados
#string
rua = 'Rua do Catete '
numero = ('123 ')
bairro = ' - Catete '
cidade = 'Rio de janeiro '
estado = 'RJ'
cep = ' 22220-000'

print(rua)
print(type(rua))
endereco = rua + numero + bairro + cidade + estado + cep
print(endereco)


#Integer-------------------------------------------------------------------------
x = 1
print(x)
print(type(x))
y = -30
print(y)
z = +404
print(z)

numero_alunos = int (50)
print(numero_alunos)
print(type(numero_alunos))

#Divisão int + int = float
divisao = 50 / 2
print(divisao)
print(type(divisao))

divisao = int(50 / 2)
print(divisao)
print(type(divisao))

#Float---------------------------------------------------------------------------
a = 2.5  #para seperar as casas decimais é utilizado o ponto 3.5 padrão americano
print(type(a))
b = 2,5
print(type(b))

d = 35e3 #o tipo é float
print(type(d))


#Boolean-------------------------------------------------------------------------
5 == 5 #true
3 > 25 #false
'python' == 'java' #true

'python' > 'java'


#Convertendo os tipos de dados
num_end = 500
num_end_2 = '200'

num_end_x = str(num_end)
print(type(num_end))
print(type(num_end_x))

num_end_y = int(num_end_2)
print(type(num_end_y))



