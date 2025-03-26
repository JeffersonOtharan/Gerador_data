import PyInstaller.__main__
import os

# Obtém o diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define os argumentos para o PyInstaller
PyInstaller.__main__.run([
    'database_generator.py',  # Script principal
    '--name=Gerador_Banco_Dados',  # Nome do executável
    '--onefile',  # Criar um único arquivo executável
    '--windowed',  # Não mostrar console
    '--clean',  # Limpar arquivos temporários
    '--noconfirm',  # Não pedir confirmação
    f'--distpath={os.path.join(current_dir, "dist")}',  # Diretório de saída
    f'--workpath={os.path.join(current_dir, "build")}',  # Diretório de trabalho
    f'--specpath={current_dir}',  # Diretório para o arquivo spec
]) 