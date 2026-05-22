import array as arr

notas = arr.array('i', [5, 7, 8, 9])

print("Notas armazenadas:", list(notas))  # convertendo para lista na exibição

notas.append(10)

print("Notas atualizadas:", list(notas))
