import os
os.system("cls")

print("Boletim escolar")

lista_notas = []
nome = input("Digite o nome do aluno: ").title()
curso = input("Digite o curso do aluno: ").upper()

while True:
    nota = float(input("Digite a nota do aluno: "))    
    lista_notas.append(nota)
    print(lista_notas)

    opcao = input("Deseja adicionar mais notas? (Enter - continue | n - não)").lower()
 
    if opcao == "n":
        media = sum(lista_notas) / len(lista_notas)
        print("A média do aluno é: ", media)
        break
    