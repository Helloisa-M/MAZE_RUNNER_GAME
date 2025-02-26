import os
import time
from colorama import Fore, Style

def escolher_personagem():
    print("\n✨ Escolha seu personagem ✨")
    print(f"{Fore.RED}❤️  1. Thomas {Style.RESET_ALL}")
    print(f"{Fore.GREEN}💚 2. Newt {Style.RESET_ALL}")
    print(f"{Fore.BLUE}💙 3. Minho {Style.RESET_ALL}")
    print(f"{Fore.CYAN}💎 4. Teresa {Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}💜 5. Gally {Style.RESET_ALL}")
    
    escolha_p = input("🎮 Escolha um personagem: ")
    
    personagens = {
        "1": ("Thomas", "T", Fore.RED),
        "2": ("Newt", "N", Fore.GREEN),
        "3": ("Minho", "M", Fore.BLUE),
        "4": ("Teresa", "T", Fore.CYAN),
        "5": ("Gally", "G", Fore.MAGENTA)
    }

    if escolha_p in personagens:
        personagem = personagens[escolha_p]
        print(f"🚀 Prepare-se para sua aventura, {personagem[0]}! 🎉")
        return personagem[1], personagem[2]
    else:
        print("❌ Opção inválida! Tente novamente.")
        return None, None

def exibir_instrucoes():
    print("\n📜 --- INSTRUÇÕES --- 📜")
    print("🎯 Objetivo: Encontre a saída do labirinto o mais rápido possível!")
    print("🕹️ Controles de movimento:")
    print("   🔼 W > Mover para cima")
    print("   🔽 S > Mover para baixo")
    print("   ◀️ A > Mover para a esquerda")
    print("   ▶️ D > Mover para a direita")

def exibir_menu():
    while True:
        print("\n🎮 --- MENU --- 🎮")
        print("1️⃣  Jogar")
        print("2️⃣  Selecionar Personagem")
        print("3️⃣  Instruções")
        print("4️⃣  Carregar Jogo")
        print("5️⃣  Sair 🚪")

        opcao = input("📌 Escolha uma opção: ")

        if opcao == "1":
            jogo_labirinto()
        elif opcao == "2":
            global inicial_personagem, cor_personagem
            inicial_personagem, cor_personagem = escolher_personagem()
        elif opcao == "3":
            exibir_instrucoes()
        elif opcao == "4":
            jogo_labirinto()
        elif opcao == "5":
            print("\n👋 Saindo do jogo... Até a próxima! ✨\n")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

def imprimir_labirinto(labirinto, jogador):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if (i, j) == jogador:
                print(f"{cor_personagem}{inicial_personagem}{Style.RESET_ALL}", end=' ')
            elif celula == '#':
                print(f"{Fore.GREEN}{celula}{Style.RESET_ALL}", end=' ')
            else:
                print(celula, end=' ')
        print()

def movimento_valido(labirinto, nova_posicao):
    i, j = nova_posicao
    return 0 <= i < len(labirinto) and 0 <= j < len(labirinto[0]) and labirinto[i][j] != '#'

def jogo_labirinto():
    labirinto = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', 'S', ' ', '#'],
        ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]
    jogador = (1, 1)
    while True:
        imprimir_labirinto(labirinto, jogador)
        movimento = input("🎯 Use W A S D para mover: ").strip().upper()
        i, j = jogador
        nova_posicao = (i - 1, j) if movimento == 'W' else (i + 1, j) if movimento == 'S' else (i, j - 1) if movimento == 'A' else (i, j + 1) if movimento == 'D' else jogador
        if movimento_valido(labirinto, nova_posicao):
            jogador = nova_posicao
        if labirinto[jogador[0]][jogador[1]] == 'S':
            imprimir_labirinto(labirinto, jogador)
            print("🎉 Parabéns! Você encontrou a saída! 🎊")
            break

if __name__ == "__main__":
    exibir_menu()
