notas = [2, 2, 3, 5]

notas.remove(2)          # Remove a primeira ocorrência do número 2

print("Lista de notas atualizada:", notas)


# Dados fornecidos
agencia = (10, 22, 33, 44)      # tupla - imutável
saldo   = [1000, 2000, 3000, 4000]  # lista - mutável

print("Agências:", agencia)
print("Saldos:", saldo)

# Alterando o saldo (lista permite)
saldo[0] = 1500
print("Saldo atualizado:", saldo)

# Tente alterar a agência (tupla NÃO permite - vai dar erro)
# agencia[0] = 99   # Descomente para ver o erro



import array as arr

# Cria um array do tipo inteiro ('i')
notas = arr.array('i', [5, 7, 8, 9])

print("Notas armazenadas:", notas)

# Adicionando uma nova nota
notas.append(10)
print("Notas atualizadas:", notas)



class ContaCorrente:
    def __init__(self, numero):
        self.numero = numero

# Criando duas contas com o mesmo número
conta_do_gui = ContaCorrente(15)
conta_da_dani = ContaCorrente(15)

if conta_do_gui == conta_da_dani:
    print('São iguais')
else:
    print('São diferentes')   # Vai imprimir "São diferentes"




class ContaCorrente:
    def __init__(self, numero):
        self.numero = numero

    def __eq__(self, other):
        return self.numero == other.numero

# Criando duas contas
conta_do_gui = ContaCorrente(15)
conta_da_dani = ContaCorrente(15)

if conta_do_gui == conta_da_dani:
    print('São iguais')      # Agora vai imprimir "São iguais"
else:
    print('São diferentes')



idades = [15, 87, 37, 45, 56, 32, 49, 37]

print("Versão 1 - usando range:")
for i in range(len(idades)):
    print(i, idades[i])

print("\nVersão 2 - usando enumerate (melhor):")
for indice, valor in enumerate(idades):
    print(indice, valor)



def calcular_media(numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma / len(numeros)

# Lista de números
numeros = [10, 20, 30, 40, 50]

media = calcular_media(numeros)
print(f"A média é: {media:.2f}")
