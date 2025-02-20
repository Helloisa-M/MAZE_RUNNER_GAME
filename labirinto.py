import time
# Digite no terminal pip install rich para instalar a biblioteca
from rich.console import Console

console = Console()

console.print("[bold green]-------------------[/bold green]")
print(" MAZE RUNNER GAME ")
console.print("[bold green]-------------------[/bold green]")
time.sleep(2)
console.print("[bold green]BEM-VINDO(A) AO LABIRINTO![/bold green]")
input("Pressione Enter para continuar...")


def menu():
    console.print("[bold green]MENU[/bold green]")
    print("1. Jogar")
    print("2. Escolher/Trocar Personagem")
    print("3. Exibir Instruções")
    print("4. Sair")
    
    return int(input("Escolha uma opção: "))  


def criar_labirinto():
    labirinto = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0],  
        [1, 1, 1, 1, 0, 1]
    ]
    return labirinto


def escolher_personagem():
    print("Personagens:")
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
        console.print("[bold red]Opção inválida![/bold red]")



while True:
    opcao = menu()
    
    if opcao == 1:
        console.print("[bold green]Iniciando o jogo...[/bold green]")
        pass  # Implementação do jogo aqui

    elif opcao == 2:
        escolher_personagem()
    
    elif opcao == 3:
        console.print("[bold cyan]Instruções do jogo:[/bold cyan]")
        print("O objetivo do jogo é escapar do labirinto evitando obstáculos e perigos.")
    
    elif opcao == 4:
        console.print("[bold green]Saindo do jogo...[/bold green]")
        break

    else:
        console.print("[bold red]Opção inválida![/bold red]")
   


    












