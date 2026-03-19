import random

numero_secreto = random.randint(1, 10)

tentativas = 5

while tentativas > 0:

    palpite = int(input(f"Você tem {tentativas} tentativas restantes. Adivinhe o número entre 1 e 10: "))

    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    else:
        
        tentativas -= 1

        
        if abs(palpite - numero_secreto) == 1:
            print("Você está MUITO perto! Aqui está uma tentativa extra!")
            tentativas += 1  # Bônus de tentativa extra

        
        if palpite < numero_secreto:
            print("O número secreto é maior que o seu palpite.")
        else:
            print("O número secreto é menor que o seu palpite.")


if tentativas == 0:
    print(f"Você perdeu! O número secreto era {numero_secreto}.")
