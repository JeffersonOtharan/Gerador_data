# Guia de Uso

## Iniciando o Programa

1. Execute o programa através do atalho no menu Iniciar ou área de trabalho
2. A interface principal será exibida

## Configurando o Banco de Dados

### Adicionando Colunas

1. Clique no botão "Adicionar Coluna"
2. Para cada coluna:
   - Digite o nome da coluna
   - Selecione o tipo de dados
   - (Opcional) Clique em "Configurações" para ajustar parâmetros específicos

### Tipos de Dados Disponíveis

#### Texto
- Dados de texto simples
- Configurações:
  - Tamanho máximo do texto

#### Números
- Inteiros ou decimais
- Configurações:
  - Valor mínimo
  - Valor máximo
  - Casas decimais (para decimais)

#### Data e Hora
- Datas e horários
- Configurações:
  - Formato da data
  - Período (início e fim)

#### Verdadeiro/Falso
- Valores booleanos
- Sem configurações adicionais

#### Email
- Endereços de email
- Sem configurações adicionais

#### Nome
- Nomes de pessoas
- Sem configurações adicionais

#### Telefone
- Números de telefone
- Sem configurações adicionais

#### Endereço
- Endereços completos
- Sem configurações adicionais

#### CPF
- Números de CPF
- Sem configurações adicionais

#### CNPJ
- Números de CNPJ
- Sem configurações adicionais

#### RG
- Números de RG
- Sem configurações adicionais

## Configurações Gerais

### Número de Linhas
- Digite o número de linhas desejado
- O valor deve ser maior que 0

### Credenciais
- Usuário: nome de usuário para acesso ao banco
- Senha: senha para acesso ao banco
- Clique em "Mostrar Senha" para visualizar

## Salvando e Carregando Configurações

### Salvar Configuração
1. Configure as colunas e opções desejadas
2. Clique em "Salvar Configuração"
3. Escolha um nome para a configuração
4. Clique em "Salvar"

### Carregar Configuração
1. Clique em "Carregar Configuração"
2. Selecione a configuração desejada
3. Clique em "Abrir"

## Gerando o Banco de Dados

1. Configure todas as colunas e opções
2. Defina o número de linhas
3. Configure as credenciais
4. Clique em "Baixar Banco de Dados"
5. Escolha o local para salvar
6. Aguarde a conclusão

## Arquivos Gerados

### Banco de Dados
- Arquivo SQLite (.db)
- Contém as tabelas e dados gerados

### Credenciais
- Arquivo JSON
- Contém as credenciais de acesso
- Guarde em local seguro

## Dicas

1. **Organização**
   - Use nomes descritivos para as colunas
   - Agrupe colunas relacionadas
   - Salve configurações comuns

2. **Performance**
   - Evite gerar muitas linhas de uma vez
   - Use tipos de dados apropriados
   - Configure limites razoáveis

3. **Segurança**
   - Use senhas fortes
   - Mantenha as credenciais seguras
   - Não compartilhe arquivos de credenciais

## Solução de Problemas

### Erro ao Gerar Banco
- Verifique se todas as colunas estão configuradas
- Confirme se o número de linhas é válido
- Verifique se há espaço suficiente no disco

### Erro ao Carregar Configuração
- Verifique se o arquivo existe
- Confirme se o arquivo não está corrompido
- Verifique se a versão é compatível

### Outros Problemas
- Verifique os logs de erro
- Reinicie o programa
- Entre em contato com o suporte 