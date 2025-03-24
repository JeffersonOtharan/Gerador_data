import tkinter as tk
from tkinter import ttk, messagebox
import json
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import random
from datetime import datetime
import shutil
from pathlib import Path

# Inicializa o Faker
fake = Faker('pt_BR')  # Configura para gerar dados em português do Brasil

# Cria a classe base para SQLAlchemy
Base = declarative_base()

class GeradorBancoDados:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerador de Banco de Dados")
        self.root.geometry("800x600")
        
        # Lista para armazenar definições de colunas
        self.colunas = []
        
        # Armazena o último banco de dados gerado
        self.ultimo_banco = None
        
        self.configurar_interface()
        
    def configurar_interface(self):
        # Frame principal
        frame_principal = ttk.Frame(self.root, padding="10")
        frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Seção de definição de colunas
        ttk.Label(frame_principal, text="Definição de Colunas", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=3, pady=10)
        
        # Nome da coluna
        ttk.Label(frame_principal, text="Nome da Coluna:").grid(row=1, column=0, padx=5)
        self.nome_coluna = ttk.Entry(frame_principal, width=30)
        self.nome_coluna.grid(row=1, column=1, padx=5)
        
        # Seleção do tipo de dado
        ttk.Label(frame_principal, text="Tipo de Dado:").grid(row=1, column=2, padx=5)
        self.tipos_dados = ['Texto', 'Número Inteiro', 'Número Decimal', 'Data e Hora', 'Verdadeiro/Falso', 
                          'Email', 'Nome', 'Telefone', 'Endereço']
        self.tipo_dado = ttk.Combobox(frame_principal, values=self.tipos_dados, state='readonly', width=20)
        self.tipo_dado.grid(row=1, column=3, padx=5)
        self.tipo_dado.set(self.tipos_dados[0])
        
        # Botão para adicionar coluna
        ttk.Button(frame_principal, text="Adicionar Coluna", command=self.adicionar_coluna).grid(row=1, column=4, padx=5)
        
        # Lista de colunas
        self.frame_colunas = ttk.Frame(frame_principal)
        self.frame_colunas.grid(row=2, column=0, columnspan=5, pady=10)
        
        # Número de linhas
        ttk.Label(frame_principal, text="Quantidade de Linhas:").grid(row=3, column=0, padx=5, pady=10)
        self.num_linhas = ttk.Entry(frame_principal, width=20)
        self.num_linhas.grid(row=3, column=1, padx=5, pady=10)
        self.num_linhas.insert(0, "100")
        
        # Frame para botões
        frame_botoes = ttk.Frame(frame_principal)
        frame_botoes.grid(row=4, column=0, columnspan=5, pady=20)
        
        # Botão para gerar
        ttk.Button(frame_botoes, text="Gerar Banco de Dados", command=self.gerar_banco_dados).grid(row=0, column=0, padx=5)
        
        # Botão para download
        self.botao_download = ttk.Button(frame_botoes, text="Baixar Banco de Dados", command=self.baixar_banco_dados, state='disabled')
        self.botao_download.grid(row=0, column=1, padx=5)
        
    def adicionar_coluna(self):
        nome = self.nome_coluna.get().strip()
        tipo = self.tipo_dado.get()
        
        if not nome:
            messagebox.showerror("Erro", "Por favor, insira um nome para a coluna")
            return
            
        # Adiciona à lista de colunas
        self.colunas.append({"nome": nome, "tipo": tipo})
        
        # Atualiza a exibição das colunas
        self.atualizar_exibicao_colunas()
        
        # Limpa o campo de entrada
        self.nome_coluna.delete(0, tk.END)
        
    def atualizar_exibicao_colunas(self):
        # Limpa a exibição atual
        for widget in self.frame_colunas.winfo_children():
            widget.destroy()
            
        # Mostra as colunas
        for i, col in enumerate(self.colunas):
            ttk.Label(self.frame_colunas, text=f"{col['nome']} ({col['tipo']})").grid(row=i, column=0, padx=5)
            ttk.Button(self.frame_colunas, text="Remover", 
                      command=lambda idx=i: self.remover_coluna(idx)).grid(row=i, column=1, padx=5)
            
    def remover_coluna(self, indice):
        self.colunas.pop(indice)
        self.atualizar_exibicao_colunas()
        
    def gerar_banco_dados(self):
        if not self.colunas:
            messagebox.showerror("Erro", "Adicione pelo menos uma coluna")
            return
            
        try:
            num_linhas = int(self.num_linhas.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido de linhas")
            return
            
        # Gera nome aleatório para o banco de dados
        nome_banco = f"banco_{random.randint(1000, 9999)}"
        
        # Cria diretório de bancos de dados se não existir
        if not os.path.exists("bancos_dados"):
            os.makedirs("bancos_dados")
            
        # Cria banco de dados SQLite
        engine = create_engine(f'sqlite:///bancos_dados/{nome_banco}.db')
        
        # Cria classe de tabela dinâmica
        atributos_tabela = {}
        for col in self.colunas:
            if col['tipo'] in ['Texto', 'Email', 'Nome', 'Telefone', 'Endereço']:
                atributos_tabela[col['nome']] = Column(String)
            elif col['tipo'] == 'Número Inteiro':
                atributos_tabela[col['nome']] = Column(Integer)
            elif col['tipo'] == 'Número Decimal':
                atributos_tabela[col['nome']] = Column(Float)
            elif col['tipo'] == 'Data e Hora':
                atributos_tabela[col['nome']] = Column(DateTime)
            elif col['tipo'] == 'Verdadeiro/Falso':
                atributos_tabela[col['nome']] = Column(Boolean)
                
        TabelaDinamica = type('TabelaDinamica', (Base,), {
            '__tablename__': 'dados',
            **atributos_tabela
        })
        
        # Cria a tabela
        Base.metadata.create_all(engine)
        
        # Cria sessão
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Gera dados
        for _ in range(num_linhas):
            dados_linha = {}
            for col in self.colunas:
                if col['tipo'] == 'Texto':
                    dados_linha[col['nome']] = fake.text(max_nb_chars=50)
                elif col['tipo'] == 'Número Inteiro':
                    dados_linha[col['nome']] = fake.random_int(min=-1000, max=1000)
                elif col['tipo'] == 'Número Decimal':
                    dados_linha[col['nome']] = fake.random_number(digits=5, fix_len=True)
                elif col['tipo'] == 'Data e Hora':
                    dados_linha[col['nome']] = fake.date_time()
                elif col['tipo'] == 'Verdadeiro/Falso':
                    dados_linha[col['nome']] = fake.boolean()
                elif col['tipo'] == 'Email':
                    dados_linha[col['nome']] = fake.email()
                elif col['tipo'] == 'Nome':
                    dados_linha[col['nome']] = fake.name()
                elif col['tipo'] == 'Telefone':
                    dados_linha[col['nome']] = fake.phone_number()
                elif col['tipo'] == 'Endereço':
                    dados_linha[col['nome']] = fake.address()
                    
            session.add(TabelaDinamica(**dados_linha))
            
        session.commit()
        session.close()
        
        # Salva credenciais
        credenciais = {
            "nome_banco": nome_banco,
            "caminho_banco": f"bancos_dados/{nome_banco}.db",
            "criado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        with open(f"bancos_dados/{nome_banco}_credenciais.json", "w", encoding='utf-8') as f:
            json.dump(credenciais, f, indent=4, ensure_ascii=False)
            
        # Armazena informações do último banco gerado
        self.ultimo_banco = {
            "nome": nome_banco,
            "caminho": f"bancos_dados/{nome_banco}.db",
            "credenciais": f"bancos_dados/{nome_banco}_credenciais.json"
        }
        
        # Habilita o botão de download
        self.botao_download.config(state='normal')
            
        messagebox.showinfo("Sucesso", f"Banco de dados gerado com sucesso!\nNome: {nome_banco}\nLocalização: bancos_dados/{nome_banco}.db")
        
    def baixar_banco_dados(self):
        if not self.ultimo_banco:
            messagebox.showerror("Erro", "Nenhum banco de dados foi gerado ainda")
            return
            
        try:
            # Obtém o caminho da pasta de downloads
            downloads_path = str(Path.home() / "Downloads")
            
            # Cria uma pasta para o banco de dados
            pasta_banco = os.path.join(downloads_path, f"banco_dados_{self.ultimo_banco['nome']}")
            os.makedirs(pasta_banco, exist_ok=True)
            
            # Copia o arquivo do banco de dados
            shutil.copy2(self.ultimo_banco['caminho'], os.path.join(pasta_banco, f"{self.ultimo_banco['nome']}.db"))
            
            # Copia o arquivo de credenciais
            shutil.copy2(self.ultimo_banco['credenciais'], os.path.join(pasta_banco, f"{self.ultimo_banco['nome']}_credenciais.json"))
            
            messagebox.showinfo("Sucesso", f"Banco de dados baixado com sucesso!\nLocalização: {pasta_banco}")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao baixar o banco de dados: {str(e)}")
        
    def executar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GeradorBancoDados()
    app.executar() 