def por_valor(x):
    x = x + 10
    print(f"Dentro de por_valor: {x}")

def por_referencia(lista):
    lista[0] = lista[0] + 10
    print(f"Dentro de por_referencia: {lista[0]}")

a = 5
por_valor(a)
print(f"Após por_valor: {a}")

b = [5]
por_referencia(b)
print(f"Após por_referencia: {b[0]}")
