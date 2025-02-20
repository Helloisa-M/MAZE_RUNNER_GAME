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
