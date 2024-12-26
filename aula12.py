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

'''primeiro_numero = int(input('Digite o primeiro número:'))
segundo_numero = int(input('Digite o segundo numero:'))
if primeiro_numero > segundo_numero:
    print(f"o número {primeiro_numero} é maior que o {segundo_numero}.")
elif segundo_numero > primeiro_numero:
    print(f'O número {segundo_numero} é maior que o {primeiro_numero}.')    
else:
    print('Os dois números são iguais.')'''

#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

'''from datetime import date
year = date.today().year
ano = int(input('Qual o seu ano de nascimento?'))
idade = year - ano
print(f'Você nasceu em {ano} e tem {idade} anos de idade')
if idade <= 17: 
    resultado = 17 - idade
    print('Você ainda não está no periodo de alistamento, faltam {resultado} para se alistar.')
elif idade == 18:
    print('Você deve ser alistar.')
elif idade >= 19:
    resultado = idade - 19
    print(f'Seu prazo de alistamento já passou {resultado} anos.')'''

#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
#final, de acordo com a média atingida:
#–Média abaixo de 5.0: REPROVADO
#–Média entre 5.0 e 6.9: RECUPERAÇÃO
#–Média 7.0 ou superior: APROVADO
