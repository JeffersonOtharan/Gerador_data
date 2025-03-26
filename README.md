# Gerador de Banco de Dados

![Status do Build](https://github.com/JeffersonOtharan/Gerador_data/workflows/CI/CD/badge.svg)
![Versão](https://img.shields.io/badge/versão-1.0.0-blue.svg)
![Licença](https://img.shields.io/badge/licença-MIT-green.svg)

Um gerador de banco de dados com interface gráfica que permite criar bancos de dados SQLite com dados aleatórios para testes. Desenvolvido com Python e Tkinter, demonstrando boas práticas de desenvolvimento e CI/CD.

## 🚀 Tecnologias Utilizadas

- Python 3.8+
- Tkinter (GUI)
- SQLAlchemy (ORM)
- Faker (Geração de dados)
- PyInstaller (Criação de executável)
- Inno Setup (Criação de instalador)
- GitHub Actions (CI/CD)

## 📋 Funcionalidades

- Interface gráfica intuitiva em português
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
- Sistema de CI/CD automatizado

## 🛠️ Instalação

### Para Usuários
1. Baixe o arquivo `Gerador_Banco_Dados_Setup.exe` da seção [Releases](https://github.com/JeffersonOtharan/Gerador_data/releases)
2. Execute o instalador
3. Siga as instruções na tela
4. O programa será instalado em "Arquivos de Programas" e criará atalhos no menu Iniciar

### Para Desenvolvedores
1. Clone o repositório:
```bash
git clone https://github.com/JeffersonOtharan/Gerador_data.git
cd Gerador_data
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o programa:
```bash
python database_generator.py
```

## 🔄 Pipeline CI/CD

O projeto utiliza GitHub Actions para automatizar:
- Testes automatizados
- Criação de executável
- Geração de instalador
- Criação automática de releases

## 📝 Documentação

- [Guia de Uso](docs/USO.md)
- [Documentação Técnica](docs/TECNICA.md)
- [Changelog](CHANGELOG.md)

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

Jefferson Otharan
- GitHub: [@JeffersonOtharan](https://github.com/JeffersonOtharan)
- LinkedIn: [Seu LinkedIn]
- Email: [Seu Email]

## Download

Você pode baixar o instalador do programa na seção [Releases](https://github.com/seu-usuario/gerador-banco-dados/releases) deste repositório.

### Requisitos do Sistema
- Windows 10 ou superior
- Não requer Python instalado

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

## Saída

O aplicativo irá:
1. Criar um banco de dados SQLite na pasta `