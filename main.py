def exibir_menu():
    print("===== Calculadora de Números Complexos =====")
    print("Selecione a operação desejada:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def adicionar(num1, num2):
    resultado = num1 + num2
    return resultado

def subtrair(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

def dividir(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida!")
        return None

def main():
    sair = False

    while not sair:
        exibir_menu()
        escolha = input("Digite o número da operação desejada: ")

        if escolha == "1":
            real1 = float(input("Digite a parte real do primeiro número complexo: "))
            imag1 = float(input("Digite a parte imaginária do primeiro número complexo: "))
            num1 = complex(real1, imag1)

            real2 = float(input("Digite a parte real do segundo número complexo: "))
            imag2 = float(input("Digite a parte imaginária do segundo número complexo: "))
            num2 = complex(real2, imag2)

            resultado = adicionar(num1, num2)
            print("Resultado da adição:", resultado)

        elif escolha == "2":
            real1 = float(input("Digite a parte real do primeiro número complexo: "))
            imag1 = float(input("Digite a parte imaginária do primeiro número complexo: "))
            num1 = complex(real1, imag1)

            real2 = float(input("Digite a parte real do segundo número complexo: "))
            imag2 = float(input("Digite a parte imaginária do segundo número complexo: "))
            num2 = complex(real2, imag2)

            resultado = subtrair(num1, num2)
            print("Resultado da subtração:", resultado)

        elif escolha == "3":
            real1 = float(input("Digite a parte real do primeiro número complexo: "))
            imag1 = float(input("Digite a parte imaginária do primeiro número complexo: "))
            num1 = complex(real1, imag1)

            real2 = float(input("Digite a parte real do segundo número complexo: "))
            imag2 = float(input("Digite a parte imaginária do segundo número complexo: "))
            num2 = complex(real2, imag2)

            resultado = multiplicar(num1, num2)
            print("Resultado da multiplicação:", resultado)

        elif escolha == "4":
            real1 = float(input("Digite a parte real do primeiro número complexo: "))
            imag1 = float(input("Digite a parte imaginária do primeiro número complexo: "))
            num1 = complex(real1, imag1)

            real2 = float(input("Digite a parte real do segundo número complexo: "))
            imag2 = float(input("Digite a parte imaginária do segundo número complexo: "))
            num2 = complex(real2, imag2)

            # Cálculo da divisão
            denominador_conjugado = num2.conjugate()
            numerador = num1 * denominador_conjugado
            denominador = num2 * denominador_conjugado

            resultado = numerador / denominador
            print("Resultado da divisão:", resultado)

        elif escolha == "5":
            sair = True
            print("Obrigado por usar a calculadora de números complexos!")

        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()
