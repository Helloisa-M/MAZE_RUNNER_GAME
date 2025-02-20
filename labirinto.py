
import time
#Digite no terminal pip install rich para instalar a biblioteca
from rich.console import Console


console = Console()

console.print("[bold green]-------------------[bold green]")
print(" MAZE RUNNER GAME ")
console.print("[bold green]-------------------[bold green]")
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
# Loop principal
while True:
    opcao = menu()
    if opcao == 1:

        pass
    elif opcao == 2:
        
        pass
    elif opcao == 3:
        
        pass

    elif opcao == 4:
        console.print("[bold green]Saindo do jogo...[/bold green]")
        break
    else:
        console.print("[bold red]Opção inválida![/bold red]")


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

def escolher_personagem(personagem,numero):
    print("Personagens:")
    print("1. Thomas")
    print("2. Newt")
    print("3. Minho")
    print("4. Teresa")
    











def menu():
    console.print("[bold green]MENU[/bold green]")

    print("1. Jogar")
    print("2. Escolher/Trocar Personagem")
    print("3. Exibir Instruções")
    print("4. Sair")
    
    return int(input("Escolha uma opção: "))
# Loop principal
while True:
    opcao = menu()
    if opcao == 1:
        
        pass
    elif opcao == 2:
        
        pass
    elif opcao == 3:
        
        pass

    elif opcao == 4:
        console.print("[bold green]Saindo do jogo...[/bold green]")
        break
    else:
        console.print("[bold red]Opção inválida![/bold red]")

   
