def criar_labirinto():
    """
    Labirinto com caminho livre até a saída (posição (4, 5)).
    """
    labirinto = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0],  # Ajustei o labirinto para permitir passagem até a saída
        [1, 1, 1, 1, 0, 1]
    ]
    return labirinto

def imprimir_labirinto(labirinto, pos_jogador, pos_saida):
    """
    Exibe o labirinto com a posição do jogador representada por "P"
    e a posição de saída representada por "S".
    """
    for i in range(len(labirinto)):
        linha = []
        for j in range(len(labirinto[i])):
            # Se a célula for a posição do jogador, colocamos um 'P'
            if (i, j) == pos_jogador:
                linha.append('P')
            # Se a célula for a posição da saída, colocamos um 'S'
            elif (i, j) == pos_saida:
                linha.append('S')
            else:
                # Exibe 0 para caminho livre e 1 para parede
                linha.append(str(labirinto[i][j]))
        print(' '.join(linha))

def mover_jogador(labirinto, pos_jogador, direcao):
    """
    Atualiza a posição do jogador com base na direção fornecida.
    Retorna a nova posição do jogador.
    """
    x, y = pos_jogador
    if direcao == 'cima' and x > 0 and labirinto[x-1][y] == 0:
        return (x-1, y)
    elif direcao == 'baixo' and x < len(labirinto)-1 and labirinto[x+1][y] == 0:
        return (x+1, y)
    elif direcao == 'esquerda' and y > 0 and labirinto[x][y-1] == 0:
        return (x, y-1)
    elif direcao == 'direita' and y < len(labirinto[0])-1 and labirinto[x][y+1] == 0:
        return (x, y+1)
    else:
        return pos_jogador

def verificar_vitoria(pos_jogador, pos_saida):
    """
    Verifica se o jogador chegou à saída.
    """
    return pos_jogador == pos_saida

def obter_movimento():
    """
    Solicita que o jogador escolha uma direção.
    """
    movimento = input("Escolha uma direção (cima, baixo, esquerda, direita): ").lower()
    while movimento not in ['cima', 'baixo', 'esquerda', 'direita']:
        movimento = input("Movimento inválido. Escolha (cima, baixo, esquerda, direita): ").lower()
    return movimento

def jogar():
    """
    Função principal para rodar o jogo.
    """
    labirinto = criar_labirinto()  # Criando o labirinto
    pos_jogador = (1, 1)  # Posição inicial do jogador (segunda linha e segunda coluna)
    pos_saida = (4, 5)    # Posição de saída (última linha da direita)

    while True:
        imprimir_labirinto(labirinto, pos_jogador, pos_saida)  # Imprime o labirinto com a posição do jogador e a saída
        print(f"Posição do jogador: {pos_jogador}")

        movimento = obter_movimento()  # Obtém o movimento desejado
        pos_jogador = mover_jogador(labirinto, pos_jogador, movimento)  # Atualiza a posição do jogador
        
        if verificar_vitoria(pos_jogador, pos_saida):
            imprimir_labirinto(labirinto, pos_jogador, pos_saida)  # Imprime o labirinto final com a vitória
            print("Você venceu!")
            break  # O jogador venceu, então o jogo acaba

if __name__ == "__main__":
    jogar()
