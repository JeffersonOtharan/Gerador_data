# Gerador de Banco de Dados

Este é um aplicativo com interface gráfica para gerar bancos de dados SQLite com dados aleatórios em português.

## Requisitos

- Python 3.7 ou superior
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone este repositório ou baixe os arquivos
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Usar

1. Execute o aplicativo:
```bash
python database_generator.py
```

2. Na interface gráfica:
   - Digite o nome da coluna
   - Selecione o tipo de dado desejado
   - Clique em "Adicionar Coluna"
   - Repita o processo para adicionar mais colunas
   - Especifique a quantidade de linhas desejada
   - Clique em "Gerar Banco de Dados"
   - Após gerar, use o botão "Baixar Banco de Dados" para copiar para a pasta de Downloads

## Tipos de Dados Disponíveis

- Texto: Texto aleatório
- Número Inteiro: Números inteiros aleatórios
- Número Decimal: Números decimais aleatórios
- Data e Hora: Datas e horários aleatórios
- Verdadeiro/Falso: Valores booleanos aleatórios
- Email: Endereços de email aleatórios
- Nome: Nomes aleatórios
- Telefone: Números de telefone aleatórios
- Endereço: Endereços aleatórios

## Saída

O aplicativo irá:
1. Criar um banco de dados SQLite na pasta `bancos_dados`
2. Gerar um arquivo de credenciais JSON com informações sobre o banco de dados
3. Mostrar uma mensagem de sucesso com o nome e localização do banco de dados gerado
4. Permitir o download do banco de dados para a pasta de Downloads do usuário

## Observações

- Todos os dados gerados são em português do Brasil
- Os bancos de dados são salvos no formato SQLite
- Cada banco de dados gerado recebe um nome único
- As credenciais são salvas em um arquivo JSON separado
- Ao baixar o banco de dados, ele será copiado para uma pasta específica na pasta de Downloads
- O botão de download só fica disponível após gerar um banco de dados

## Criando o Executável

Para criar um executável do aplicativo:

1. Certifique-se de que todas as dependências estão instaladas:
```bash
pip install -r requirements.txt
```

2. Execute o script de criação do executável:
```bash
python criar_executavel.py
```

3. O executável será criado na pasta `dist` com o nome `GeradorBancoDados.exe`

4. Para usar o executável:
   - Copie o arquivo `GeradorBancoDados.exe` da pasta `dist`
   - Execute-o com duplo clique
   - O aplicativo funcionará sem necessidade de ter o Python instalado

### Requisitos para o Executável

- Windows 7 ou superior
- Não é necessário ter Python instalado
- O executável é um arquivo único e independente
- Os bancos de dados gerados serão salvos na mesma pasta do executável 