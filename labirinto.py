import time
import csv
import random
import os
from rich.console import Console

console = Console()


def carregar_labirinto(labirinto):
    with open(labirinto, newline='') as arquivo:
        leitor = csv.reader(arquivo)
        return [list(linha[0]) for linha in leitor]
    
def gerar_saida(labirinto, colunas, linhas):
    while True:
      posicao_c =  random.randint(0, colunas)
      posicao_l =  random.randint(0, linhas)
      if labirinto[posicao_l][posicao_c] == " " and (posicao_l != 1 and posicao_c != 1):
          labirinto[posicao_l][posicao_c] = "🚪"
          break

def introducao():
    console.print("\n🌿 [bold green]BEM-VINDO À CLAREIRA[/bold green] 🌿")
    console.print(
        "Você desperta em um elevador em movimento...\n"
        "As portas se abrem e um grupo de garotos te encara.\n"
        "Você está na Clareira, um lugar cercado por um labirinto mortal.\n"
        "Ninguém sabe como chegou aqui. Sua única saída é encontrar um caminho para a liberdade.\n"
    )
    time.sleep(2)

def escolher_personagem():
    os.system('cls')
    console.print("\n✨ [bold cyan]Escolha seu personagem[/bold cyan] ✨")
    personagens = {
        "1": ("Thomas", "T", "red"),
        "2": ("Newt", "N", "green"),
        "3": ("Minho", "M", "blue"),
        "4": ("Teresa", "T", "cyan"),
        "5": ("Gally", "G", "magenta"),
    }
    
    for num, (nome, _, cor) in personagens.items():
        console.print(f"[bold {cor}] {num}. {nome}[/bold {cor}]")o
    
    escolha_p = input("\n🎮 Escolha um personagem: ")

    if escolha_p in personagens:
        os.system('cls')
        personagem = personagens[escolha_p]
        console.print(f"\n🚀 [bold yellow]Prepare-se para sua aventura, {personagem[0]}![/bold yellow] 🎉")
        return personagem[1], personagem[2]
        
    else:
        console.print("[bold red]❌ Opção inválida! Tente novamente.[/bold red]")
        return None, None
    

def exibir_instrucoes():
    console.print("\n📜 [bold yellow]--- INSTRUÇÕES ---[/bold yellow] 📜")
    console.print("🎯 [bold]Objetivo:[/bold] Encontre a saída do labirinto antes que anoiteça!")
    console.print("🕹 [bold]Controles de movimento:[/bold]")
    console.print("   🔼 W > Mover para cima")
    console.print("   🔽 S > Mover para baixo")
    console.print("   ◀ A > Mover para a esquerda")
    console.print("   ▶ D > Mover para a direita")
    

def exibir_menu():
    personagem = None
    while True:
        console.print("\n🎮 [bold cyan]--- MENU ---[/bold cyan] 🎮")
        console.print("⿡ 1. Jogar")
        console.print("⿢ 2. Selecionar Personagem")
        console.print("⿣ 3. Instruções")
        console.print("⿤ 4. Sair 🚪")

        opcao = input("\n📌 Escolha uma opção: ")
        

        if opcao == "1":
            os.system('cls')
            if personagem:
                jogo_labirinto(personagem)
            else:
                console.print("[bold red]❌ Você precisa escolher um personagem primeiro![/bold red]")
        elif opcao == "2":
            os.system('cls')
            personagem = escolher_personagem()
        elif opcao == "3":
            os.system('cls')
            exibir_instrucoes()
        elif opcao == "4":
            os.system('cls')
            console.print("\n👋 [bold red]Saindo do jogo...[/bold red] ✨\n")
            break
        else:
            console.print("[bold red]❌ Opção inválida! Tente novamente.[/bold red]")


def movimento_valido(labirinto, nova_posicao):
    i, j = nova_posicao
    return 0 <= i < len(labirinto) and 0 <= j < len(labirinto[0]) and labirinto[i][j] != '#'

def imprimir_labirinto(labirinto, jogador, inicial_personagem, cor_personagem):
    os.system('cls')

    for i, linha in enumerate(labirinto):
        linha_formatada = ""
        for j, celula in enumerate(linha):
            if (i, j) == jogador:
                linha_formatada += f"[bold {cor_personagem}]{inicial_personagem}[/bold {cor_personagem}] "
            elif celula == '#':
                linha_formatada += "[bold green]#[/bold green] "
            else:
                linha_formatada += f"{celula} "
        console.print(linha_formatada)


def jogo_labirinto(personagem):
    inicial_personagem, cor_personagem = personagem
    console.print("\n🏃‍♂ [bold blue]Você entrou no labirinto! Encontre a saída antes que as portas se fechem![/bold blue] 🏃‍♂")

    labirinto = carregar_labirinto('labirinto.csv')
    gerar_saida(labirinto, 20, 22)

    jogador = (1, 1)  
    tempo_inicio = time.time()  
    while True:
        tempo_decorrido = time.time() - tempo_inicio
        tempo_restante = 60 - tempo_decorrido

        if tempo_restante <= 0:
            imprimir_labirinto(labirinto, jogador, inicial_personagem, cor_personagem)
            console.print("\n[bold red]💥 O tempo acabou! Você não conseguiu sair a tempo![/bold red] 💥")
            break

        imprimir_labirinto(labirinto, jogador, inicial_personagem, cor_personagem)
        console.print(f"\n⏰ [bold yellow]Tempo restante: {int(tempo_restante)} segundos[/bold yellow]")
        movimento = input("\n🎯 Use W A S D para mover ou 'sair' para encerrar o jogo: ").strip().upper()
        
        i, j = jogador 
        
        if movimento == 'W': 
            nova_posicao = (i - 1, j)
        elif movimento == 'S': 
            nova_posicao = (i + 1, j)
        elif movimento == 'A':  
            nova_posicao = (i, j - 1)
        elif movimento == 'D': 
            nova_posicao = (i, j + 1)
        elif movimento == "SAIR":
            console.print("\n👋 [bold red]Saindo do jogo...[/bold red] ✨\n")
            break
        else:
            console.print("[bold red]❌ Movimento inválido! Use apenas W, A, S ou D.[/bold red]")
            continue
            
        if movimento_valido(labirinto, nova_posicao):
            jogador = nova_posicao

        if labirinto[jogador[0]][jogador[1]] == '🚪':
            imprimir_labirinto(labirinto, jogador, inicial_personagem, cor_personagem)
            console.print("🎉 [bold gold]Parabéns! Você encontrou a saída![/bold gold] 🎊")
            break

if __name__ == "__main__":
    introducao()
    exibir_menu()
    
