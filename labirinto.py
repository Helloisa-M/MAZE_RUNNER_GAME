import csv
import time


def escolher_personagem():
    print("Escolha seu personagem:")
    print("1. Thomas")
    print("2. Newt")
    print("3. Minho")
    print("4. Teresa")
    print("5. Gally")
    
    escolha_p = input("Qual personagem você deseja escolher? ")
    
    personagens = {
        "1": "Thomas",
        "2": "Newt",
        "3": "Minho",
        "4": "Teresa",
        "5": "Gally"
    }

    if escolha_p in personagens:
        print(f"Prepare-se para sua aventura, {personagens[escolha_p]}!")
    else:
        print("Opção inválida!")



def exibir_instrucoes():
    print("-------------------")
    print("\n--- INSTRUÇÕES ---")
    print("Objetivo: Você deve encontrar a saída do labirinto o mais rápido possível!")
    print("Para sair do labirinto, você deve percorrer os corredores até alcançar o ponto de saída.")
    print("Controles de movimento:")
    print(" W > Mover para cima")
    print(" S > Mover para baixo")
    print(" A > Mover para a esquerda")
    print(" D > Mover para a direita")

def exibir_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Jogar")
        print("2. Selecionar Personagem")
        print("3. Instruções")
        print("4. Carregar Jogo")
        print("5. Ranking")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            iniciar_jogo()
        elif opcao == "2":
            escolher_personagem()
        elif opcao == "3":
            exibir_instrucoes()
        elif opcao == "4":
            iniciar_jogo()
        elif opcao == "5":
            exibir_ranking()
        elif opcao == "6":
            print("\nSaindo do jogo...\n")
            break
        else:
            print("Opção inválida!")

exibir_menu()
