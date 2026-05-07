import os
import time
os.system('cls')
listanotas = []
nome = input("Digite o nome do aluno: ")

try:    
    
    entrada = input("Digite a nota do aluno: ").replace(",", ".")
    nota = float(entrada)

    if nota > 10 or nota < 0:
        print("Erro! Digite uma nota entre 0-10.")
    else:
        listanotas.append(nota)

        while True:
            opcao = input("Deseja adicionar mais uma nota? (S/N): ").lower().strip()
            
            if opcao in ("sim", "s"):
               
                entrada2 = input("Adicione outro número: ").replace(",", ".")
                nova_nota = float(entrada2)

                if 0 <= nova_nota <= 10:
                    listanotas.append(nova_nota)
                else:
                    print("Erro! Digite uma nota entre 0-10.")

            elif opcao in ("nao", "n"):
                if len(listanotas) > 0:
                    media = sum(listanotas) / len(listanotas)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'A média das notas de {nome} é {media:.2f}')
                    time.sleep(2)
                break
            else:
                print("Opção inválida! Digite S ou N.")
except ValueError:
    print("Erro: Digite um número válido!")
