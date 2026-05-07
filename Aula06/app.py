lista = ['fulano', 'cicrano', 'beltrano', 'maria', 'pedro']
# print(lista)

# # print(type(lista))
# # for i in lista:


# ##imprimindo valro específico
# print(lista[0])

# #imprimindo o último indice
# print(lista[-1])

# #imprimir intervalo
# print(lista[2:4])

#ordenar lista
#lista.sort()

# for i in range(len(lista)):
#     print(f'{i+1}º valor da lista: {lista[i]}')

# adicionando na lista
lista.append('celly')
             
#inserindo em posição específica
lista.insert(2, 'joao')

# inserindo vários valores
lista.extend(['ana', 'beatriz', 'david', 'roberto'])

# adicionando valores de forma dinamica
numero = []
for i in range(0):
     numero.append(i*2)
print(numero)

# removendo item da lista
print(f'Lista antes de remover{lista}')

# pop - remove pelo indice
# lista.pop(0)

# pop - remove o último pelo indice
lista.pop()

# removendo pelo valor (remove o primeiro que achar)
lista.remove('ana')
print(f'Lista depois de remover{lista}')

lista_numeros = [n for n in range(1,11)]

print(f'Lista antes de remover{lista_numeros}')
# removendo intervalo de valores
del lista_numeros[2:5]

print(f'Lista depois de remover{lista_numeros}')

listanomes = ['gomes', 'fulano', 'cicrano', 'beltrano', 'maria', 'pedro']
#alterando valor de lista
listanomes[1] = 'farias'
print(listanomes)

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
     if numeros[i] > 5:
          numeros[i] = numeros[i] * 2
print(numeros)

numeros2 = [10,20,30,40,50]

# list compreheision
numeros2 = [n * 2 if n > 20 else n for n in numeros2]