#Uso de condições aninhadas: if, elif, else:


#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor 
# da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou 
# então o empréstimo será negado.
'''print('~' * 50)
print('... Calculadora de prestrações de imóveis ...')
print('~' * 50)

casa = int(input("Qual o valor da casa que você deseja comprar em R$:"))
salario = int(input('Qaul o seu salário em R$:'))
tempo = int(input('Em quantos anos você deseja pagar a casa?'))
parcela = salario * 0.3
prestração = casa / (tempo * 12)
if prestração <= parcela:
    print('\033[1;32;47m Parabéns seu emprestimo foi aprovado!\033[m')
else:
    print('\033[1;31;47m Tente adicionar outra renda a sua solicitação.\033[m')'''


#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de 
#conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

'''numero = int(input('Digite um número inteiro qualquer:'))
print( Escolha qual a converão do seu número:
      [1] para binário
      [2] para octal
      [3] para hexadecimal )
escolha= int(input("Qual a sua escolha:"))
if escolha == 1:
    print(f'Seu número em binário fica: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'Seu número em octal fica: {oct(numero)[:2]}')
elif escolha == 3:
    print(f'Seu número em hexadecimal fica: {hex(numero)[:2]}')
else:
    print('Dados incorretos, reinicie o programa')'''


#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# -O primeiro valor é maior
# –O segundo valor é maior
#–Não existe valor maior, os dois são iguais

