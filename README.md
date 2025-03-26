# Gerador de Banco de Dados

Uma aplicação gráfica para gerar bancos de dados SQLite com dados aleatórios em português.

## Funcionalidades

- Interface gráfica intuitiva
- Geração de dados aleatórios em português
- Suporte a diversos tipos de dados:
  - Texto (com tamanho configurável)
  - Números inteiros e decimais (com faixa de valores configurável)
  - Data e hora (com formato configurável)
  - Verdadeiro/Falso
  - Email
  - Nome
  - Telefone
  - Endereço
  - CPF
  - CNPJ
  - RG
- Configurações personalizáveis por coluna
- Barra de progresso durante a geração
- Salvamento e carregamento de configurações
- Validação de entrada de dados
- Geração de banco SQLite

## Requisitos

- Python 3.8 ou superior
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/gerador-banco-dados.git
cd gerador-banco-dados
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

1. Execute o programa:
```bash
python database_generator.py
```

2. Na interface:
   - Adicione colunas clicando em "Adicionar Coluna"
   - Configure cada coluna com nome e tipo
   - Ajuste as configurações específicas de cada coluna (opcional)
   - Defina o número de linhas desejado
   - Clique em "Baixar Banco de Dados" para gerar

3. O banco de dados será gerado na pasta `bancos_dados`

## Configurações de Colunas

### Texto
- Tamanho máximo do texto

### Números
- Valor mínimo
- Valor máximo

### Data e Hora
- Formato da data (ex: %d/%m/%Y, %Y-%m-%d)

## Contribuição

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## Saída

O aplicativo irá:
1. Criar um banco de dados SQLite na pasta `