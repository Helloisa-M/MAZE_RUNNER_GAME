import time
from rich.console import Console

console = Console()

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
    console.print("\n✨ [bold cyan]Escolha seu personagem[/bold cyan] ✨")
    personagens = {
        "1": ("Thomas", "T", "red"),
        "2": ("Newt", "N", "green"),
        "3": ("Minho", "M", "blue"),
        "4": ("Teresa", "T", "cyan"),
        "5": ("Gally", "G", "magenta"),
    }

    for num, (nome, _, cor) in personagens.items():
        console.print(f"[bold {cor}] {num}. {nome}[/bold {cor}]")

    escolha_p = input("\n🎮 Escolha um personagem: ")

    if escolha_p in personagens:
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
    while True:
        console.print("\n🎮 [bold cyan]--- MENU ---[/bold cyan] 🎮")
        console.print("⿡ 1. Jogar")
        console.print("⿢ 2. Selecionar Personagem")
        console.print("⿣ 3. Instruções")
        console.print("⿤ 4. Carregar Jogo")
        console.print("⿥ 5. Sair 🚪")

        opcao = input("\n📌 Escolha uma opção: ")

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
            console.print("\n👋 [bold red]Saindo do jogo...[/bold red] ✨\n")
            break
        else:
            console.print("[bold red]❌ Opção inválida! Tente novamente.[/bold red]")

def imprimir_labirinto(labirinto, jogador):
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

def movimento_valido(labirinto, nova_posicao):
    i, j = nova_posicao
    return 0 <= i < len(labirinto) and 0 <= j < len(labirinto[0]) and labirinto[i][j] != '#'

def jogo_labirinto():
    console.print("\n🏃‍♂ [bold blue]Você entrou no labirinto! Encontre a saída antes que as portas se fechem![/bold blue] 🌫")
    
   labirinto = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#'],
    ['#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', 'S'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

    jogador = (1, 1)
    while True:
        imprimir_labirinto(labirinto, jogador)
        movimento = input("\n🎯 Use W A S D para mover: ").strip().upper()
        i, j = jogador
        nova_posicao = (i - 1, j) if movimento == 'W' else (i + 1, j) if movimento == 'S' else (i, j - 1) if movimento == 'A' else (i, j + 1) if movimento == 'D' else jogador
        if movimento_valido(labirinto, nova_posicao):
            jogador = nova_posicao
        if labirinto[jogador[0]][jogador[1]] == 'S':
            imprimir_labirinto(labirinto, jogador)
            console.print("🎉 [bold gold]Parabéns! Você encontrou a saída![/bold gold] 🎊")
            break

if __name__ == "__main__":

    introducao()
    exibir_menu()
