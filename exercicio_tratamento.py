

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
"""
import math

try:
    c = float(input("Digite a temperatura em Celsius: "))
except ValueError as ve:
    print("\nDigite um numero valido. Ex. 25.5")
    print(ve)
except KeyboardInterrupt as ki:
    print("\nOperação cancelada pelo usuário.")
    print(ki)
except InterruptedError as i:
    print("\nA operação foi interrompida.")
    print(i)
except Exception as e:
    print("\nDeu ruim no numero digitado")
    print(e)

try: 
    f = (c * 9/5) + 32
except MemoryError as me:
    print("\nErro de memória.")
    print(me)
except OverflowError as oe:
    print("\nErro de estouro.")
    print(oe)
except Exception as e:
    print("\nDeu ruim no calculo")
    print(e)

if math.isinf(f) == False:
    print(f"\nA temperatura em Fahrenheit é {f}°")
else:
    print("\nO calculo de temperatura retornou valor infinito.")

"""

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

## referencia: https://docs.python.org/3/library/stdtypes.html
# txt1 = "texto"
# txt2 = "texto2"
# txt3 = "1234"

# print("alnum", txt1.isalnum()) # True
# print("alnum", txt2.isalnum()) # True
# print("alnum", txt3.isalnum()) # True

# print("alpha", txt1.isalpha()) # True
# print("alpha", isalpha()) # False
# print("alpha", txt3.isalpha()) # False

# print("numeric", txt1.isnumeric()) # False
# print("numeric", txt2.isnumeric()) # False
# print("numeric", txt3.isnumeric()) # True
"""
texto = str(input("Digite um palindromo: "))
if texto.isalpha() == False:
    raise TypeError("A entrada deve conter somente letras.")
else:
    palin = texto.strip()[::-1]
    if texto == palin:
        print(f"{texto} é um palindromo")
    else:
        print(f"{texto} não é um palindromo") 
"""

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

# referencia: https://docs.python.org/pt-br/3.13/tutorial/introduction.html

# a, b = 0, 1
# while a < 10:
#     print(a, end=',')
#     a, b = b, a + b

"""
while True:
    num1 = None
    num2 = None
    op = None

    while True: 
        n = input("digite um numero: ")
        try:
            num1 = float(n)
            break
        except ValueError as ve:
            print("Digite apenas numeros. Ex 25.5")
    
    while True: 
        n = input("digite outro numero: ")
        try:
            num2 = float(n)
            break
        except ValueError as ve:
            print("Digite apenas numeros. Ex 25.5")
    
    while True: 
        op = input("digite o operador (+, -, / ou *): ")
        if op in['+', '-', '*', '/']:
            break
        else:
            print("digite um operador valido! (+, -, / ou *)")
    
    if op == '+':
        print(f"Resultado: {num1 + num2}")
    elif op == '-':
        print(f"Resultado: {num1 - num2}")
    elif op == '*':
        print(f"Resultado: {num1 * num2}")
    elif op == '/':
        try: 
                print(f"Resultado: {num1 / num2}")
        except ZeroDivisionError as zde:
                print("Divisao por zero!")
                print(zde)
    break
"""
    
# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

# i = 3 % 2
# p = 6 % 2
# print(f"par: {p} / impar: {i}")


while True:
    try:
          num = float(input("Digite um numero: "))
    except ValueError as ve:
         print("Digite apenas numeros. Ex. 25.5 ou -25.5")
         print(ve)
         continue
    if num > 0:
        sinal = "positivo"
    elif num < 0:
        sinal = "negativo"
    else:
        sinal = "zero"

    resto = num % 2
    if resto == 0 and num != 0:
        print(f"O valor {num} é {sinal} e é par")
    elif resto != 0:
        print(f"O valor {num} é {sinal} e é impar")
    else:
        print(f"O valor {num} não tem sinal e é par")
    break

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
