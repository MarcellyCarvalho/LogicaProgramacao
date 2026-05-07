'''
1. crie um programa que o usuario possa digitar quantos numeros quiser e ao terminar imprima uma lista em ordem crescente

2. crie um programa que o usuario possa digitar a quantidade desejada de notas de um determinado aluno (nota minima 0 e nota maxima 10) e o 
programa calcula a media desse aluno e, ao final, imprima se o aluno está (aprovado >=7, reprovado recuperação)
'''
lista = []
try:
    num = int(input("Digite um número: "))
    lista.append(num)
    while True:
        print("Deseja adicionar outro número? (S/N) ")
        opcao = input().lower().strip()
        if opcao in ("sim", "s"):
            num = int(input("Adicionar outro número: "))
            lista.append(num)
        elif opcao in ("nao","n"):
            lista.sort()
            print(f'{lista} é a sua lista.')
except:
    print("Digite um número!")