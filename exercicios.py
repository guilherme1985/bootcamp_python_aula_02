import math

###Exercícios
##Inteiros (int)
#1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
"""
num1 = int(input("Digite um valor inteiro: "))
num2 = int(input("Digite outro valor inteiro: "))

print(f"A soma é {num1 + num2}")
"""
#2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
"""
num = int(input("Digite um numero: "))
resto = int((num % 5))

print(f"O resto da divisao por 5 é {resto}")
"""
#3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
"""
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))

print(f"A multiplicação é {num1 * num2}")
"""
#4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
"""
num1 = int(input("Digite um valor inteiro: "))
num2 = int(input("Digite outro valor inteiro: "))

print(f"A sua divisao sem resto é {num1 // num2}")

"""
#5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
"""
num = int(input("Digite um numero: "))
quadrado = (num ** 2)

print(f"O quadrado de {num} é {quadrado}")
"""
##Números de Ponto Flutuante (float)
#6. Escreva um programa que receba dois números flutuantes e realize sua adição.
"""
num1 = float(input("Digite um valor flutuante: "))
num2 = float(input("Digite outro valor flutuante: "))

print(f"A soma é {num1 + num2}")
"""
#7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
"""
num1 = float(input("Digite um valor flutuante: "))
num2 = float(input("Digite outro valor flutuante: "))
media = ((num1 + num2) / 2)

print(f"A média é {media}")
"""
#8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
"""
num = float(input("Digite um numero: "))
pot = float(input("Digite a potencia: "))
calculo = (num ** pot)

print(f"O resultado de {num} elevado a {pot} é {calculo}")
"""
#9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
"""
c = float(input("Digite a temperatura em Celsius: "))
f = (c * 9/5) + 32

print(f"A temperatura em Fahrenheit é {f}°")
"""
#10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
"""
raio = float(input("Digite o raio do circulo: "))
area = 3.14 * (raio ** 2)

# melhorando de acordo com o video da aula
area2 = math.pi * (math.pow(raio, 2))

print(f"A área do circulo é {area}")
print(f"A área do circulo de outra forma {area2:.2f}")
"""
##Strings (str)
#11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
"""
texto = str.lower(input("Digite em minusculo: "))

print(f"Texto em maiusculo: {str.upper(texto)}")
"""
#12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
"""
nome = input("Digite seu nome completo: ")
print(f"Nome em minusculo: {str.lower(nome)}")
print(f"outra forma: {nome.lower()}")
"""
#13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
"""
texto = input("Digite uma frase: ")
print(f"Frase sem espaços: {texto.strip()}")
"""
#14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
"""

#data = input("Digite a data no formato ""dd/mm/aaaa: ")
#dia,mes,ano = data.split('/')

##outra forma conforme aula, com criaçao de variavel
data = "21/08/2025"
data.split("/")
dia = data.split("/")[0]
mes = data.split("/")[1]
ano = data.split("/")[2]

print(f"Dia {dia}, Mes {mes}, Ano {ano}")
"""
#15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
"""
texto1 = str(input("Digite algo: "))
texto2 = str(input("Digite outro algo: "))
concat = texto1 + texto2

print(f"Concatenação {texto1 + texto2}")
print(f"outra forma {concat}")
print("outra outra forma de juntar ", texto1 + texto2)
"""

##Booleanos (bool)
#16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
"""
bl1 = True
bl2 = False
res = bl1 and bl2

print(f"resultado do AND: {res}")
"""
#17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
"""
bl1 = True
bl2 = False
res = bl1 or bl2

print(f"resultado do OR: {res}")
"""
#18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
"""
bl = False
inverso = not bl

print(f"Resultado do NOT: {inverso}")
"""
#19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
"""
num1 = float(input("Digite um valor: "))
num2 = float(input("Digite outro valor: "))
comp = num1 == num2

print(f"Os numeros sao iguais? {comp}")
"""
#20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

num1 = float(input("Digite um valor: "))
num2 = float(input("Digite outro valor: "))
comp = num1 != num2

print(f"Os numeros sao diferentes? {comp}")
