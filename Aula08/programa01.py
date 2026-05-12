import modulo as ma

def main():
    while True:
        print("Calculadora")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Limpar terminal")

        opcao = input("Digite a opção desejada: ")
        match opcao:
            case '1':
                print('-----SOMA-----')
                num1 = int(input("Digite um número para somar: "))
                num2 = int(input("Digite outro número: "))
                resultado = ma.soma(num1,num2)
                print(f'Resultado: {resultado}')
                break
            case '2':
                print('-----SUBTRAÇÃO-----')
                num1 = int(input("Digite um número para subtrair: "))
                num2 = int(input("Digite outro número: "))
                resultado = ma.sub(num1,num2)
                print(f'Resultado: {resultado}')
                break
            case '3':
                print('-----MULTIPLICAÇÃO-----')
                num1 = int(input("Digite um número para multiplicar: "))
                num2 = int(input("Digite outro número: "))
                resultado = ma.mult(num1,num2)
                print(f'Resultado: {resultado}')
                break
            case '4':
                print('-----DIVISÃO-----')
                num1 = int(input("Digite um número para dividir: "))
                num2 = int(input("Digite outro número: "))
                resultado = ma.sub(num1,num2)
                print(f'Resultado: {resultado}')
                break
            case '5':
                ma.limpa_terminal
                break
            case _:
                print("Opção inválida!")


if __name__ == "__main__":
    main()