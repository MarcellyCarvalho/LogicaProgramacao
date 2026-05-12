'''
Desenvolva um sistema de gerenciamento de veículos, permita cadastrar o veiculo pegando do usuário os seguintes dados: modelo, marca e preço

	- os dados devem ser armazenados em um arquivo.
	- o usuário deve poder cadastrar quantos carros quiser sem ter que rodar o sistema novamente.
	- deve ter a opção de ler carros existentes
	- devem ser cadastrados em um arquivo .txt e usar dicionário
'''
import os
carros = []

os.system('cls')
while True:
    print("\nSistema de Carros >_<")
    print('1. - Cadastrar carro')
    print('2. - Listar carros')
    print('0. - Sair do sistema')
    
    opcao = input("Escolha uma opção: ")
    
    #criar
    if opcao == '1':
        modelo = input("Digite o modelo do carro: ").title()
        preco = float(input('Digite o preço do carro: '))
        marca = input("Digite a marca: ").title()

        carro = {
            "modelo": modelo,
            "preço": preco,
            "marca": marca
        }
        carros.append(carro)
        with open('carros.txt', 'w') as arquivo:
            for c in carros:
                linha = f"{c['modelo']}, {c['preço']}, {c['marca']}\n"
                arquivo.write(linha)
        

        novo_carro = input('Deseja cadastrar outro carro? s/n :'  ).lower()
        if novo_carro in ('n','nao'):
            print("✅Carro cadastro com sucesso!")

    #read
    elif opcao == '2':
        os.system('cls')
        if not carros:
            print('⚠️Nenhum carro cadastrado.')
        else:
            print('\n📋Lista de carros')
            for carro in carros:
                print(f'| Modelo: {carro['modelo']} | Preço: {carro['preço']} | Marca: {carro['marca']}')

    #sair
    elif opcao == '0':
        print('Programa encerrado.')
        break
   
    else: print('❌Opção inválida.')