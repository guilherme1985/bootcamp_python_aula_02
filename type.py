"""
# Exemplo que causa TypeError
try:
    resultado = len(5)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro
"""
#####
# TYPE ERROR
#####
"""
try:
    num1 = int(input("Digite um valor inteiro: "))
    num2 = int(input("Digite outro valor inteiro: "))
    resultado = num1 // num2
    print(resultado)
except ZeroDivisionError as z:
    print(z) # Imprime mensagem de erro
except KeyboardInterrupt:
    print("Vc interrompeu o programa")
except TypeError as e:
    print(e)
else:
    print("se nao tiver falhas imprime")
finally:
    print("sempre imprime")
"""
    
#####
# TYPE CHECK
#####
# numero = int(input("digite um numero: "))
# if isinstance(numero, int):
#     print("A variável é um inteiro.")
# else:
#     print("A variável não é um inteiro.")

idade = 17

IDADE_MINIMA = 16
IDADE_MIN_CARTEIRA = 18

if idade <= IDADE_MINIMA:
    print("Não pode dirigir")
else:
    print("Pode dirigir")

if idade <= IDADE_MIN_CARTEIRA:
    print("Não pode tirar a carteira")
else:
    print("Pode tirar a carteira")
