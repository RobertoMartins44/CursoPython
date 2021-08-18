#Aula 4 - List; Tuple; Sets e Dictionary

#List------------------------------------------------------
frutas = ['banana', 'abacate','laranja','melancia']
print(frutas)

print(frutas[3])

saldo_alunos = [500.00,1000.00,600.00,450.00,6000.00]
print(saldo_alunos)
print(saldo_alunos[0])

num_paciente = [25, 36, 50, 45, 22, 33]
print(num_paciente)
print(num_paciente[5])

variados = [10,5.6,'python']
print(variados)

#Adiconar um item na lista

frutas.append('melao')
print(frutas)

#Juntas Listas

saldo_alunos.extend(num_paciente)
print(saldo_alunos)

#Tuple-----------------------------------------------------

carros = ('Gol','Palio','X-terra','Hilux','Fusca')
print(carros[0])
#intervalo
print(carros[1:5])

times = ('SAO PAULO','PALMEIRAS','SANTOS','VASCO')
print(times)

#Juntas tuples

tuples_junto = carros + times
print(tuples_junto)

#Sets------------------------------------------------------
cidade = {'Manaus','Fortaleza','Natal','Rio de Janeiro'}
cidade2 = {'Curitiba','Porto Alegre','Salvador','Aracaju'}

print(type(cidade))
print(cidade)
print('Manaus' in cidade)

ling_pro = {'Python','Java','C++','Cobol'}
print(ling_pro)

#Adicionar um item no Set

ling_pro.add('PHP')
print(ling_pro)

#Juntar Sets

cidade.update(cidade2)
print(cidade)

#Dictinary-------------------------------------------------

cod_uf  = {21 : 'Maranhão',
           22 : 'Manaus',
           23 : 'Tocantins',
           24 : 'São Paulo',
           25 : 'Belo Horizonte',
           26 : 'Brasilia',
           27 : 'Rio de Janeiro'}
print(cod_uf)