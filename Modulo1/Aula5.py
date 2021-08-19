#Condições e Loops

#if elif else-----------------------------------------------

#1---------------------------
a = 50
b = 100
c = 50

if a == c:
    print ('A igual a C')
else:
    print ('A não é igual C')

#2---------------------------
idade = int(input('Digite sua idade: '))

if idade >= 18:
  print ('Aulas de Habilitação liberadas')
elif idade < 18:
  print ('Aulas de Habilitação não permitido')

#3---------------------------
exercicio = int(input("Quantas minutos você se exercita por dia: "))
if exercicio < 30:
  print ('Você deveriar malhar mais!')
elif exercicio >= 30 and exercicio <= 60:
  print ('Você esta no caminho certo')
elif exercicio > 60 and exercicio <= 120:
  print ('Você é um atleta')
else:
  print ('Muito exercicio. Diminua seu ritmo')

#4---------------------------
print('A soma dos dois numero é metade de 120')
num1 = int(input('Digite o primero numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 + num2 == 60:
  print('Acertou')
else:
  print('Errouuu!!!')

#5---------------------------
trabalho = input ('Você deve trabalhar hoje? ')
dia = input ('O dia esta bonito? ')
preguica = input ('Você esta com preguisa? ')

if trabalho == 'sim':
  print ('É uma pena!')
elif trabalho == 'não':
  print('Aproveite o dia!')

if dia == 'sim' and trabalho == 'não':
  print ('Aproveite para caminhar')
elif dia == 'não' and trabalho == 'não':
  print('Aproveita e assite um filme')

if preguica == 'sim' and trabalho == 'não':
  print('Aproveita e dorme mais')
elif preguica == 'não'  and trabalho == 'não':
  print('Que tal estudar Python?')

#6---------------------------
idade = 18
if idade < 12:
 print('crianca')
elif idade < 18:
 print('adolescente')
elif idade < 60:
 print('adulto')
else:
 print('idoso')




#For-----------------------------------------------
#1---------------------------
numeros = (1,2,3,4,5,6,7,8,9,10)
for i in numeros:
  print (i)
for i in range(1,5):
 print(i)

 nomes = ['João', 'Maria', 'José', 'Geraldo', 'Sebastião']
for i in nomes:
 print(i)

#2---------------------------
cor = ['verde','amarelo','azul','cinza','vermelho']
for x in cor:
  print(x)

for i in 'lerletraporletraemostrar':
  print(i)

# FOR Break

numeros = (1,2,3,4,5,6,7,8,9,10)
for x in numeros:
  print(x)

numeros1 = (1,2,3,4,5,6,7,8,9,10)
for x in numeros1:
  print(x)
  if x == 7:
    break

numeros1 = (1,2,3,4,5,6,7,8,9,10)
for x in numeros1:
  if x == 7:
      print(x)
      break

#3---------------------------
for i in range(1,5):
 print(i)

#4---------------------------
 nomes = ['João', 'Maria', 'José', 'Geraldo', 'Sebastião']
for i in nomes:
 print(i)


 #While----------------------------------------------------
 numero = 0
 while numero <= 10:
     numero += 1
     print(numero)

ligar = 'true'
while (ligar):
    print('Motor ligado')
    ligar = 'false'
    break
else:
    print('Desligado')

conta = 0
while(conta <= 10):
    conta += 1
    print(conta)
else:
    print("Valor da variável conta é: ", conta)



