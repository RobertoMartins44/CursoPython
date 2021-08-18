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
