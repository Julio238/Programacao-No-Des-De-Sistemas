# Programa que verifica se um número x pertence a uma lista de n números

n = int(input("Digite o número de elementos (n): "))

lista = []

print(f"Digite agora {n} números inteiros:")

for i in range(n):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)

x = int(input("\nDigite o número x que deseja verificar: "))

# Verifica se x pertence à lista
if x in lista:
    print(f"O número {x} pertence à lista.")
else:
    print(f"O número {x} NÃO pertence à lista.")

# Opcional: mostrar a lista completa
print(f"\nLista completa: {lista}")
