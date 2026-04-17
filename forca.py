import random

# Lista de palavras para o jogo (pode adicionar mais)
palavras = ['python', 'computador', 'forca', 'programacao', 'desenvolvedor', 
            'inteligencia', 'artificial', 'algoritmo', 'variavel', 'funcao']

# Desenhos da forca - 7 estágios (0 erros até 6 erros)
desenhos_forca = [
    # 0 erros
    """
    +---+
    |   |
        |
        |
        |
        |
    =========""",
    
    # 1 erro - cabeça
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========""",
    
    # 2 erros - corpo
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========""",
    
    # 3 erros - braço esquerdo
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========""",
    
    # 4 erros - braço direito
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========""",
    
    # 5 erros - perna esquerda
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========""",
    
    # 6 erros - perna direita (game over)
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    ========="""
]

def escolher_palavra():
    palavra = random.choice(palavras)
    return palavra.upper()

def exibir_forca(erros):
    print(desenhos_forca[erros])

def exibir_palavra_secreta(palavra, letras_corretas):
    # Usa list comprehension + join para mostrar a palavra com _ ou letras
    exibicao = ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])
    print(exibicao)

def jogar():
    palavra_secreta = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    max_erros = 6
    erros = 0
    
    print("=== BEM-VINDO AO JOGO DA FORCA ===\n")
    
    while erros < max_erros:
        exibir_forca(erros)
        exibir_palavra_secreta(palavra_secreta, letras_corretas)
        
        print(f"\nLetras erradas: {', '.join(sorted(letras_erradas)) if letras_erradas else 'Nenhuma'}")
        
        # Pede uma letra e normaliza para maiúscula
        try:
            palpite = input("\nDigite uma letra: ").strip().upper()
        except:
            print("Entrada inválida!")
            continue
        
        # Validações usando métodos de string
        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas UMA letra!")
            continue
        
        if palpite in letras_corretas or palpite in letras_erradas:
            print("Você já tentou essa letra. Tente outra!")
            continue
        
        # Verifica se a letra está na palavra (usando count ou in)
        if palpite in palavra_secreta:
            letras_corretas.add(palpite)
            print(f"Boa! A letra '{palpite}' está na palavra.")
            
            # Verifica vitória usando replace ou join
            if all(letra in letras_corretas for letra in palavra_secreta):
                exibir_forca(erros)
                exibir_palavra_secreta(palavra_secreta, letras_corretas)
                print(f"\n🎉 PARABÉNS! Você venceu! A palavra era: {palavra_secreta}")
                break
        else:
            letras_erradas.add(palpite)
            erros += 1
            print(f"Que pena! A letra '{palpite}' não está na palavra.")
    
    # Fim do jogo - derrota
    if erros == max_erros:
        exibir_forca(erros)
        exibir_palavra_secreta(palavra_secreta, letras_corretas)
        print(f"\n💀 GAME OVER! Você foi enforcado. A palavra era: {palavra_secreta}")

# Inicia o jogo
if __name__ == "__main__":
    jogar()
    
    while True:
        jogar_novamente = input("\nQuer jogar novamente? (S/N): ").strip().upper()
        if jogar_novamente == 'S':
            jogar()
        elif jogar_novamente == 'N':
            print("Obrigado por jogar! Até a próxima.")
            break
        else:
            print("Responda apenas com S ou N.")
