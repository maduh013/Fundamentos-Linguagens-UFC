Código exemplo em Python:

fila = ["Maria", "João", "Ana", "Carlos", "Luiza"]

print("Sistema de Atendimento")
print("========================")

i = 0
while i < len(fila):
    nome = fila[i]
    print(f"Chamando {nome}...")
    
    resposta = input("Pessoa presente? (s/n): ")
    
    if resposta.lower() == "s":
        print(f"{nome} foi atendido.")
    else:
        print(f"{nome} perdeu a vez. Será chamada novamente no final.")
        fila.append(nome)
    
    i += 1

print("Fila finalizada.")
