def calculadora():
    print("--- Calculadora Simples ---")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    
    escolha = input("Escolha a operação (1/2/3/4): ")
    
    # Verifica se a opção é válida
    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if escolha == '1':
            print(f"Resultado: {num1 + num2}")
        elif escolha == '2':
            print(f"Resultado: {num1 - num2}")
        elif escolha == '3':
            print(f"Resultado: {num1 * num2}")
        elif escolha == '4':
            # Evita erro de divisão por zero
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Erro: Não é possível dividir por zero.")
    else:
        print("Opção inválida.")

# Executa a calculadora
calculadora()
