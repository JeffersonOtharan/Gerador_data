import PyInstaller.__main__
import os

# Obtém o diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Configura os parâmetros do PyInstaller
parametros = [
    'database_generator.py',  # Script principal
    '--name=GeradorBancoDados',  # Nome do executável
    '--onefile',  # Criar um único arquivo executável
    '--windowed',  # Não mostrar console
    '--icon=icon.ico',  # Ícone do executável (se existir)
    '--add-data=README.md;.',  # Incluir arquivo README
    '--clean',  # Limpar arquivos temporários
    '--noconfirm',  # Não pedir confirmação
    f'--distpath={os.path.join(diretorio_atual, "dist")}',  # Pasta de saída
    f'--workpath={os.path.join(diretorio_atual, "build")}',  # Pasta de trabalho
    f'--specpath={diretorio_atual}',  # Pasta para o arquivo spec
]

# Executa o PyInstaller
PyInstaller.__main__.run(parametros)

print("Executável criado com sucesso!")
print(f"Localização: {os.path.join(diretorio_atual, 'dist', 'GeradorBancoDados.exe')}") 