# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
operacao = input('Digite qual a operação que deseja fazer (+ - * / ** // %): ')

if operacao == '+':
    print(f"A soma dos números é: {numero1 + numero2}")
elif operacao == '-':
    print(f"A subtração dos números é: {numero1 - numero2}")
elif operacao == '*':
    print(f"A multiplicação dos números é: {numero1 * numero2}")
elif operacao == '/':
    print(f"A divisão dos números é: {numero1 / numero2}")
elif operacao == '**':
    print(f"A exponenciação dos números é: {numero1 ** numero2}")
elif operacao == '//':
    print(f"A divisão inteira dos números é: {numero1 // numero2}")
elif operacao == '%':
    print(f"O resto da divisão dos números é: {numero1 % numero2}") 
else:
    print("Operação inválida")