while True:
    import random
    

    print("=== ROLETA RUSSA DA PROGRAMAÇÃO ===")
    print('''Tente adivinhar o número entre 1 e 100.
    ou seu System32 será excluido.''')
    print(
        '''=== ESCOLHA A DIFICULDADE ===
        1 - Difícil (4 tentativas e número entre 0 e 200)
        2 - Normal (10 tentativas e número entre 0 e 100)
        3 - Fácil (15 tentativas e número entre 0 e 50)''')
    
    while True:        
        dificuldade = input("Escolha uma dificuldade: ")
        if dificuldade == "1":
            minimo = 0
            maximo = 200
            max_tentativas = 4
            print('Dificuldade selecionada: Dificil. Está no treino do Saitama?')
            print('Tem certeza? Deseja manter nesta dificuldade?') 
            input("s/n : ").lower()
            if input == 's':
                break
            else:
                dificuldade = input("Escolha uma dificuldade: ")
                if dificuldade != "1" and dificuldade != "2" and dificuldade != "3":   
                    print("Opção inválida. Tente novamente.")
                    dificuldade = input("Escolha uma dificuldade: ")
                else:
                    break
            break
        elif dificuldade == "2":
            minimo = 0
            maximo = 100
            max_tentativas = 10
            print('Dificuldade selecionada: Normal. Nem nisso tu é capaz de querer uma dificuldade.')
            print('Deseja manter nesta dificuldade?') 
            input("s/n : ")
            if input == 's':
                break
            else:
                dificuldade = input("Escolha uma dificuldade: ")
                if dificuldade != "1" and dificuldade != "2" and dificuldade != "3":   
                    print("Opção inválida. Tente novamente.")
                    dificuldade = input("Escolha uma dificuldade: ")
                else:
                    break
            break
        elif dificuldade == "3":
            max_tentativas = 15
            minimo = 0
            maximo = 50
            print('Dificuldade selecionada: Fácil. A vida não é mole, pelo visto você nâo chegaria aos pés do Saitama') 
            print('Deseja manter nesta dificuldade?') 
            input("s/n : ")
            if input == 's':
                break
            else:
                dificuldade = input("Escolha uma dificuldade: ")
                if dificuldade != "1" and dificuldade != "2" and dificuldade != "3":   
                    print("Opção inválida. Tente novamente.")
                    dificuldade = input("Escolha uma dificuldade: ")
                else:
                    break
            break
        else:
            print("Opção inválida. Tente novamente.")
    numeroAleatorio = random.randint(minimo, maximo)
    acertou = False
    print(f"Você terá {max_tentativas} tentativas.")
    for tentativa in range(1, max_tentativas + 1):
        palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))
        if palpite == numeroAleatorio:
            print(f"Parabéns! Você acertou o número {numeroAleatorio}!")
            print(f"Você precisou de {tentativa} tentativa(s).")
            acertou = True
            break
        elif palpite < numeroAleatorio:
            print("O número secreto é MAIOR.")
            print(f"Você tem {max_tentativas - tentativa} tentativas restantes.")
        else:
            print("O número secreto é MENOR.")
            print(f"Você tem {max_tentativas - tentativa}tentativas restantes.")
    if not acertou:
        print(f"Suas tentativas acabaram! O número era {numeroAleatorio}. Você é gay")
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        print("Obrigado por jogar!")
        break