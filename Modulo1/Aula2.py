#Aula 2 - Escrevendo em Python
#Syntax Python, Indentação, Variáveis, comentários e dicas de boas práticas

if 10 > 5:
    print('Dez é maior que cinco') #exemplo indentação

#erro de indentação------------------------------------
#if 10 > 5:
#print('Dez é maior que cinco') #exemplo indentação
#------------------------------------------------------

numero = 5
Python = 'Melhor linguagem de Programação'
num_pi = 3.14
soma = 5+5

#a função print imprime um resultado
print(numero)
print(Python)
print(num_pi)
print(soma)
# Exemplo de comentário ''' ou """
soma = 5+5 # Criando uma variável de soma
''' 
A partir do momento que coloquei três aspas simples, tudo o que 
eu escrever aqui dentro será considerado comentário. É muito útil 
quando queremos explicar alguma coisa, ou deixar instruções dentro
 ou antes do código.'''

#Declaração de Variáveis

#declaração de variavel string
cidade = 'Sao d\' Paulo'
print (cidade)
#declaração de variavel integer
numcpf = int (123456)
print (numcpf)

#declaração de variavel float
num_pi = 3.14
print (num_pi)

#declaração de variavel dictionary
uf_sud = {'MG':31, 'SP':35, 'RJ':33, 'ES':32}
# Definindo código da capital do Amazonas
cod_manaus = {'Manaus':1302603}
# Definindo o gentílico de quem nasce em Manaus
gentílico = {'Manaus':'manauara'}


