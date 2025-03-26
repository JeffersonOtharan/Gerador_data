# Gerador de Banco de Dados

Um gerador de banco de dados com interface gráfica que permite criar bancos de dados SQLite com dados aleatórios para testes.

## Download

Você pode baixar o instalador do programa na seção [Releases](https://github.com/seu-usuario/gerador-banco-dados/releases) deste repositório.

### Requisitos do Sistema
- Windows 10 ou superior
- Não requer Python instalado

## Funcionalidades

- Interface gráfica intuitiva
- Geração de dados aleatórios realistas
- Suporte a múltiplos tipos de dados:
  - Texto
  - Números inteiros e decimais
  - Datas e horas
  - Valores booleanos
  - Emails
  - Nomes
  - Telefones
  - Endereços
  - CPF
  - CNPJ
  - RG
- Configurações personalizáveis para cada coluna
- Salvamento e carregamento de configurações
- Geração de arquivo de credenciais
- Interface em português

## Instalação

1. Baixe o arquivo `Gerador_Banco_Dados_Setup.exe` da seção [Releases](https://github.com/seu-usuario/gerador-banco-dados/releases)
2. Execute o instalador
3. Siga as instruções na tela
4. O programa será instalado em "Arquivos de Programas" e criará atalhos no menu Iniciar

## Desenvolvimento

Se você quiser desenvolver ou modificar o programa, siga estas instruções:

### Requisitos de Desenvolvimento
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação do Ambiente de Desenvolvimento

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/gerador-banco-dados.git
cd gerador-banco-dados
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o programa:
```bash
python database_generator.py
```

### Criando um Executável

Para criar um executável do programa:

1. Instale o Inno Setup 6 (https://jrsoftware.org/isdl.php)
2. Execute o script de criação do instalador:
```bash
python criar_instalador.py
```

O instalador será criado na pasta `installer`.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Saída

O aplicativo irá:
1. Criar um banco de dados SQLite na pasta `bancos_dados`