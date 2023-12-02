import random

def exibir_tabuleiro(tabuleiro):
    for i in range(0, 9, 3):
        print(tabuleiro[i], "|", tabuleiro[i + 1], "|", tabuleiro[i + 2])
        if i < 6:
            print("---------")

def converter_jogada(jogada):
    if jogada.lower() == 'x':
        return 1
    elif jogada.lower() == 'o':
        return -1
    elif jogada.lower() == 'b':
        return 0

def jogar_jogo_da_velha():
    tabuleiro = [str(i+1) for i in range(9)]  # Preenchendo com os números de 1 a 9 no início
    print("Bem-vindo ao Jogo da Velha!")
    print("Você irá jogar como 'X' e o computador como 'O'.")
    print("Para jogar, escolha um número de 1 a 9 para indicar a posição no tabuleiro.")
    
    for rodada in range(9):
        exibir_tabuleiro(tabuleiro)
        if rodada % 2 == 0:
            jogada = input("Escolha a posição para jogar (1-9) ou digite 'acabou' para encerrar: ")
            if jogada.lower() == 'acabou':
                break
            while not jogada.isdigit() or int(jogada) < 1 or int(jogada) > 9 or tabuleiro[int(jogada) - 1] != str(int(jogada)):
                print("Jogada inválida! Escolha uma posição válida.")
                jogada = input("Escolha a posição para jogar (1-9) ou digite 'acabou' para encerrar: ")
            tabuleiro[int(jogada) - 1] = 'X'
        else:
            jogada_computador = random.choice([i for i, v in enumerate(tabuleiro) if v == str(i+1)])
            tabuleiro[jogada_computador] = 'O'
            print("Rodada da CPU:")
            exibir_tabuleiro(tabuleiro)
            if rodada < 8:
                print("\n-------------------------\n")
    
    valores_convertidos = [converter_jogada(valor) for valor in tabuleiro]
    return valores_convertidos

# Chamando a função para jogar
resultado = jogar_jogo_da_velha()
print("Valores convertidos:", resultado)

