
##### VARIAVEIS
CONSTANTE_BONUS = 1000

##### SOLICITAÇAO DE DADOS

nm_user = input("Digite seu nome: ")
try:
    while nm_user.isalpha() == False:
        print("Digite somente letras!")
        nm_user = input("\nDigite seu nome: ")
except KeyboardInterrupt:
    print("Interrompido pelo usuario.")

while True:
    try:
        vl_salario = float(input("Digite seu salario: "))
        if vl_salario > 0:
            break
        else:
            print("Salario nao pode ser negativo ou zero!")
    except ValueError:
        print("Digite somente numeros! Em caso de decimais use '.'")
    except KeyboardInterrupt:
        print("Interrompido pelo usuario.")

while True:
    try:
        bonus = float(input("Digite o percentual do bonus: "))
        if bonus >= 0:
            break
        else:
            print("Bonus não pode ser negativo!")
    except ValueError:
        print("Digite somente numeros! Em caso de decimais use '.'")
    except KeyboardInterrupt:
        print("Interrompido pelo usuario.")

##### CALCULO
if bonus == 0:
    vl_total = CONSTANTE_BONUS + vl_salario
else:
    vl_total = CONSTANTE_BONUS + vl_salario * bonus

print("\n")

# print("Seu nome é " + nm_user, "\n")
# print("Seu bonus é = R$" + str(vl_total))

print(f"O seu nome é {nm_user} possui o bonus de {vl_total}")



"""
- float so aceita ponto e nao virgula
- posso digitar valores incompativeis com o uso (text em variavel numerica)
- digitar valores negativos
"""