Exemplo prático: Processamento de uma lista usando map, filter, reduce e recursão

from functools import reduce

# Função de alta ordem: dobra os números
def dobrar(x):
    return x * 2

# Lista de entrada
numeros = [1, 2, 3, 4, 5]

# map: aplica a função dobrar
dobrados = list(map(dobrar, numeros))
print("Dobrados:", dobrados)

# filter: filtra números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

# reduce: soma os elementos
soma = reduce(lambda x, y: x + y, numeros)
print("Soma:", soma)

# recursão: soma dos elementos
def soma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])

print("Soma recursiva:", soma_recursiva(numeros))
