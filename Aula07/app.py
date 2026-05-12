'''
    MANIPULAÇÃO DE ARQUIVOS: percorrer os meus diretórios, encontrar arquivos, passar o comando de abertura de arquivo, passar comando de ação.

    Arquivo = open('arquivo.txt', 'modo')

    modos de ação:
        - "r" : leitura do arquivo
        - "w" : escrita(sobrescreve o conteudo antigo)
        - "a" : adiciona conteudo
        - "x" : criar um arquivo
        - "b" : arquivos binarios
        - "t" : texto
'''
# Criando e escrevendo arquivo
arquivo = open('primeiro_arquivo.txt', 'w')
arquivo.write('Olá mundo! esse é meu primeiro arquivo')
arquivo.close()

#lendo arquivo
arquivo = open('primeiro_arquivo.txt', "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# aplicando boa pratica
with open('primeiro_arquivo.txt','r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# arquivo com multiplas escritas
with open('alunos.txt', 'a') as arquivo:
    arquivo.write('Ana\n')
    arquivo.write('Bruna\n')
    arquivo.write('João\n')
    arquivo.write('Lucas\n')
    arquivo.write('Brenda\n')
    arquivo.write('Maria\n')
    arquivo.write('Ana\n')
    arquivo.write('Bruna\n')
    arquivo.write('João\n')


# lendo linha a linha
with open('alunos.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

# usando lista para escrever no arquivo
frutas = ['pera', 'abacaxi', 'melancia', 'manga', 'caju']

with open('frutas.txt', 'w') as arquivo:
    for f in frutas:
        arquivo.write(f + '\n')

# converter o arquivo 
with open('frutas.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(type(linhas))
    print(linhas)

# Saída:['pera\n', 'abacaxi\n', 'melancia\n', 'manga\n', 'caju\n']

# limpar a quebra de linha
with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())
        
# exemplo para cadastro

while True:
    nome = input('Digite seu nome: ').title()
    with open('cadastro,txt', 'a') as arquivo:
        arquivo.write(nome + '\n')

    sair = input("Deseja sair? s/n ").lower()
    
    if sair == 's':
        break