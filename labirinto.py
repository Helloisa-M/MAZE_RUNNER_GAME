
import time
#Digite no terminal pip install rich para instalar a biblioteca
from rich.console import Console

console = Console()

print("-------------------")
print(" MAZE RUNNER GAME ")
print("-------------------")
time.sleep(2)

def menu():
    console.print("[bold green]MENU[/bold green]")

    print("1. Jogar")
    print("Escolher Personagem")
    print("1 - Thomas")
    print("2 - Minho")
    print("3 - Newt")
    print("4 - Teresa")
    print("5 - Gally")
    print("6. Exibir Instruções")
    print("0 - Sair") 
    
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

def imprimir_labirinto():
   

def mover_jogador():
    
def verificar_vitoria():
   

def obter_movimento():
    
def jogar():
   

   
