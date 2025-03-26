import os
import subprocess
import sys
from pathlib import Path

def criar_icone():
    print("Criando ícone...")
    subprocess.run([sys.executable, "criar_icone.py"], check=True)

def criar_executavel():
    print("Criando executável...")
    subprocess.run([sys.executable, "criar_executavel.py"], check=True)

def criar_instalador():
    print("Criando instalador...")
    # Verifica se o Inno Setup está instalado
    inno_compiler = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
    
    if not os.path.exists(inno_compiler):
        print("Erro: Inno Setup não encontrado!")
        print("Por favor, instale o Inno Setup 6 em: https://jrsoftware.org/isdl.php")
        print("E tente novamente.")
        return False
    
    # Cria o diretório do instalador se não existir
    os.makedirs("installer", exist_ok=True)
    
    # Compila o script do Inno Setup
    subprocess.run([inno_compiler, "installer.iss"], check=True)
    return True

def main():
    try:
        # Cria o ícone
        criar_icone()
        
        # Cria o executável
        criar_executavel()
        
        # Cria o instalador
        if criar_instalador():
            print("\nInstalador criado com sucesso!")
            print("O arquivo de instalação está na pasta 'installer'")
            print("Nome do arquivo: Gerador_Banco_Dados_Setup.exe")
        else:
            print("\nErro ao criar o instalador!")
            
    except subprocess.CalledProcessError as e:
        print(f"\nErro durante o processo: {e}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    main() 