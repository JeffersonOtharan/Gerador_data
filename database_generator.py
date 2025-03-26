import tkinter as tk
from tkinter import ttk, messagebox
import json
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
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

class DatabaseGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Banco de Dados")
        self.root.geometry("800x600")
        
        # Configuração do estilo
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5)
        self.style.configure("TLabel", padding=5)
        self.style.configure("TEntry", padding=5)
        
        # Frame principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configuração do grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        
        # Número de linhas
        ttk.Label(self.main_frame, text="Número de Linhas:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.num_linhas = ttk.Entry(self.main_frame, width=20)
        self.num_linhas.grid(row=0, column=1, sticky=tk.W, pady=5)
        self.num_linhas.insert(0, "10")  # Valor padrão
        
        # Frame para credenciais
        cred_frame = ttk.LabelFrame(self.main_frame, text="Credenciais do Banco", padding="5")
        cred_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Usuário
        ttk.Label(cred_frame, text="Usuário:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.usuario = ttk.Entry(cred_frame, width=20)
        self.usuario.grid(row=0, column=1, sticky=tk.W, padx=5)
        self.usuario.insert(0, "admin")  # Valor padrão
        
        # Senha
        ttk.Label(cred_frame, text="Senha:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.senha = ttk.Entry(cred_frame, width=20, show="*")
        self.senha.grid(row=1, column=1, sticky=tk.W, padx=5)
        self.senha.insert(0, "admin123")  # Valor padrão
        
        # Botão para mostrar/ocultar senha
        self.mostrar_senha = tk.BooleanVar(value=False)
        self.btn_mostrar_senha = ttk.Checkbutton(cred_frame, text="Mostrar Senha", 
                                                variable=self.mostrar_senha,
                                                command=self.toggle_mostrar_senha)
        self.btn_mostrar_senha.grid(row=1, column=2, sticky=tk.W, padx=5)
        
        # Frame para colunas
        self.colunas_frame = ttk.LabelFrame(self.main_frame, text="Colunas", padding="5")
        self.colunas_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Lista de colunas
        self.colunas = []
        
        # Botões
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(self.button_frame, text="Adicionar Coluna", command=self.adicionar_coluna).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Limpar Colunas", command=self.limpar_colunas).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Salvar Configuração", command=self.salvar_configuracao).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Carregar Configuração", command=self.carregar_configuracao).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Baixar Banco de Dados", command=self.gerar_banco_dados).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Abrir Pasta de Bancos", command=self.abrir_pasta_bancos).pack(side=tk.LEFT, padx=5)
        
        # Barra de progresso
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.main_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Status
        self.status_var = tk.StringVar()
        self.status_var.set("Pronto")
        self.status_label = ttk.Label(self.main_frame, textvariable=self.status_var)
        self.status_label.grid(row=5, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Configuração do grid para expansão
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.columnconfigure(1, weight=1)

    def validar_numero_linhas(self):
        try:
            num = int(self.num_linhas.get())
            if num <= 0:
                raise ValueError("O número de linhas deve ser positivo")
            if num > 1000000:
                raise ValueError("O número de linhas não pode ser maior que 1.000.000")
            return num
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return None

    def limpar_colunas(self):
        for widget in self.colunas_frame.winfo_children():
            widget.destroy()
        self.colunas = []
        self.status_var.set("Colunas limpas")

    def salvar_configuracao(self):
        if not self.colunas:
            messagebox.showwarning("Aviso", "Não há colunas para salvar")
            return
            
        config = {
            'colunas': self.colunas,
            'num_linhas': self.num_linhas.get()
        }
        
        try:
            with open('configuracao.json', 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Sucesso", "Configuração salva com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar configuração: {str(e)}")

    def carregar_configuracao(self):
        try:
            with open('configuracao.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
                
            self.limpar_colunas()
            self.num_linhas.delete(0, tk.END)
            self.num_linhas.insert(0, config.get('num_linhas', '10'))
            
            # Carrega as colunas
            for col in config.get('colunas', []):
                # Cria o frame da coluna
                col_frame = ttk.Frame(self.colunas_frame)
                col_frame.pack(fill=tk.X, pady=2)
                
                # Nome da coluna
                ttk.Label(col_frame, text="Nome:").pack(side=tk.LEFT, padx=2)
                nome_entry = ttk.Entry(col_frame, width=20)
                nome_entry.pack(side=tk.LEFT, padx=2)
                nome_entry.insert(0, col.get('nome', ''))
                
                # Tipo da coluna
                ttk.Label(col_frame, text="Tipo:").pack(side=tk.LEFT, padx=2)
                tipo_combo = ttk.Combobox(col_frame, values=[
                    'Texto', 'Número Inteiro', 'Número Decimal', 'Data e Hora',
                    'Verdadeiro/Falso', 'Email', 'Nome', 'Telefone', 'Endereço',
                    'CPF', 'CNPJ', 'RG'
                ], state='readonly')
                tipo_combo.pack(side=tk.LEFT, padx=2)
                tipo_combo.set(col.get('tipo', ''))
                
                # Configurações adicionais
                config_frame = ttk.Frame(col_frame)
                config_frame.pack(side=tk.LEFT, padx=2)
                
                # Botão de configurações
                config_btn = ttk.Button(config_frame, text="Configurações", 
                                      command=lambda: self.abrir_configuracoes_coluna(col_frame))
                config_btn.pack(side=tk.LEFT)
                
                # Botão de remover
                remove_btn = ttk.Button(col_frame, text="Remover", 
                                      command=lambda: self.remover_coluna(col_frame))
                remove_btn.pack(side=tk.RIGHT)
                
                # Armazena os widgets para referência
                col_frame.nome_entry = nome_entry
                col_frame.tipo_combo = tipo_combo
                col_frame.config_frame = config_frame
                col_frame.config = col.get('config', {})
                
                # Atualiza a lista de colunas quando o nome ou tipo mudar
                def atualizar_coluna(*args):
                    for col in self.colunas:
                        if col['nome'] == nome_entry.get():
                            col['nome'] = nome_entry.get()
                            col['tipo'] = tipo_combo.get()
                            break
                
                nome_entry.bind('<KeyRelease>', atualizar_coluna)
                tipo_combo.bind('<<ComboboxSelected>>', atualizar_coluna)
                
                # Adiciona a coluna à lista
                self.colunas.append({
                    'nome': col.get('nome', ''),
                    'tipo': col.get('tipo', ''),
                    'config': col.get('config', {})
                })
                
                self.colunas_frame.update_idletasks()
                self.colunas_frame.configure(height=len(self.colunas_frame.winfo_children()) * 40)
                
            messagebox.showinfo("Sucesso", "Configuração carregada com sucesso!")
        except FileNotFoundError:
            messagebox.showwarning("Aviso", "Nenhuma configuração encontrada")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar configuração: {str(e)}")

    def adicionar_coluna(self, coluna_existente=None):
        # Frame para a coluna
        col_frame = ttk.Frame(self.colunas_frame)
        col_frame.pack(fill=tk.X, pady=2)
        
        # Nome da coluna
        ttk.Label(col_frame, text="Nome:").pack(side=tk.LEFT, padx=2)
        nome_entry = ttk.Entry(col_frame, width=20)
        nome_entry.pack(side=tk.LEFT, padx=2)
        
        # Tipo da coluna
        ttk.Label(col_frame, text="Tipo:").pack(side=tk.LEFT, padx=2)
        tipo_combo = ttk.Combobox(col_frame, values=[
            'Texto', 'Número Inteiro', 'Número Decimal', 'Data e Hora',
            'Verdadeiro/Falso', 'Email', 'Nome', 'Telefone', 'Endereço',
            'CPF', 'CNPJ', 'RG'
        ], state='readonly')
        tipo_combo.pack(side=tk.LEFT, padx=2)
        
        # Configurações adicionais
        config_frame = ttk.Frame(col_frame)
        config_frame.pack(side=tk.LEFT, padx=2)
        
        # Botão de configurações
        config_btn = ttk.Button(config_frame, text="Configurações", 
                              command=lambda: self.abrir_configuracoes_coluna(col_frame))
        config_btn.pack(side=tk.LEFT)
        
        # Botão de remover
        remove_btn = ttk.Button(col_frame, text="Remover", 
                              command=lambda: self.remover_coluna(col_frame))
        remove_btn.pack(side=tk.RIGHT)
        
        # Se houver uma coluna existente, preenche os valores
        if coluna_existente:
            nome_entry.insert(0, coluna_existente['nome'])
            tipo_combo.set(coluna_existente['tipo'])
        else:
            # Adiciona a coluna à lista de colunas
            self.colunas.append({
                'nome': nome_entry.get(),
                'tipo': tipo_combo.get(),
                'config': {}
            })
        
        # Armazena os widgets para referência
        col_frame.nome_entry = nome_entry
        col_frame.tipo_combo = tipo_combo
        col_frame.config_frame = config_frame
        
        # Atualiza a lista de colunas quando o nome ou tipo mudar
        def atualizar_coluna(*args):
            for col in self.colunas:
                if col['nome'] == nome_entry.get():
                    col['nome'] = nome_entry.get()
                    col['tipo'] = tipo_combo.get()
                    break
        
        nome_entry.bind('<KeyRelease>', atualizar_coluna)
        tipo_combo.bind('<<ComboboxSelected>>', atualizar_coluna)
        
        self.colunas_frame.update_idletasks()
        self.colunas_frame.configure(height=len(self.colunas_frame.winfo_children()) * 40)

    def abrir_configuracoes_coluna(self, col_frame):
        tipo = col_frame.tipo_combo.get()
        if not tipo:
            messagebox.showwarning("Aviso", "Selecione um tipo de coluna primeiro")
            return
            
        config_window = tk.Toplevel(self.root)
        config_window.title("Configurações da Coluna")
        config_window.geometry("300x200")
        
        # Frame para configurações
        config_frame = ttk.Frame(config_window, padding="10")
        config_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configurações específicas por tipo
        if tipo in ['Texto', 'Email', 'Nome', 'Telefone', 'Endereço']:
            ttk.Label(config_frame, text="Tamanho máximo:").pack(anchor=tk.W)
            tamanho_entry = ttk.Entry(config_frame)
            tamanho_entry.pack(fill=tk.X, pady=5)
            tamanho_entry.insert(0, "50")
            
        elif tipo in ['Número Inteiro', 'Número Decimal']:
            ttk.Label(config_frame, text="Valor mínimo:").pack(anchor=tk.W)
            min_entry = ttk.Entry(config_frame)
            min_entry.pack(fill=tk.X, pady=5)
            min_entry.insert(0, "0")
            
            ttk.Label(config_frame, text="Valor máximo:").pack(anchor=tk.W)
            max_entry = ttk.Entry(config_frame)
            max_entry.pack(fill=tk.X, pady=5)
            max_entry.insert(0, "1000")
            
        elif tipo == 'Data e Hora':
            ttk.Label(config_frame, text="Formato:").pack(anchor=tk.W)
            formato_combo = ttk.Combobox(config_frame, 
                                       values=['%d/%m/%Y', '%Y-%m-%d', '%d/%m/%Y %H:%M:%S'],
                                       state='readonly')
            formato_combo.pack(fill=tk.X, pady=5)
            formato_combo.set('%d/%m/%Y')
            
        # Botão de salvar
        def salvar_config():
            config = {}
            if tipo in ['Texto', 'Email', 'Nome', 'Telefone', 'Endereço']:
                config['tamanho_maximo'] = int(tamanho_entry.get())
            elif tipo in ['Número Inteiro', 'Número Decimal']:
                config['minimo'] = float(min_entry.get())
                config['maximo'] = float(max_entry.get())
            elif tipo == 'Data e Hora':
                config['formato'] = formato_combo.get()
                
            col_frame.config = config
            config_window.destroy()
            
        ttk.Button(config_frame, text="Salvar", command=salvar_config).pack(pady=10)

    def remover_coluna(self, col_frame):
        # Remove a coluna da lista
        nome = col_frame.nome_entry.get()
        for col in self.colunas[:]:
            if col['nome'] == nome:
                self.colunas.remove(col)
                break
        
        col_frame.destroy()
        self.colunas_frame.update_idletasks()
        self.colunas_frame.configure(height=len(self.colunas_frame.winfo_children()) * 40)

    def gerar_banco_dados(self):
        if not self.colunas:
            messagebox.showerror("Erro", "Adicione pelo menos uma coluna")
            return
            
        num_linhas = self.validar_numero_linhas()
        if num_linhas is None:
            return
            
        try:
            # Gera nome aleatório para o banco de dados
            nome_banco = f"banco_{random.randint(1000, 9999)}"
            
            # Cria diretório de bancos de dados se não existir
            if not os.path.exists("bancos_dados"):
                os.makedirs("bancos_dados")
                
            # Cria banco de dados SQLite
            engine = create_engine(f'sqlite:///bancos_dados/{nome_banco}.db')
            
            # Cria classe de tabela dinâmica
            atributos_tabela = {
                '__tablename__': 'dados',
                'id': Column(Integer, primary_key=True, autoincrement=True)
            }
            
            # Adiciona as colunas dinamicamente
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
                    
            TabelaDinamica = type('TabelaDinamica', (Base,), atributos_tabela)
            
            # Cria a tabela
            Base.metadata.create_all(engine)
            
            # Cria sessão
            Session = sessionmaker(bind=engine)
            session = Session()
            
            # Atualiza a barra de progresso
            self.progress_var.set(0)
            self.status_var.set("Gerando dados...")
            self.root.update()
            
            # Gera dados
            for i in range(num_linhas):
                dados_linha = {}
                for col in self.colunas:
                    if col['tipo'] == 'Texto':
                        tamanho = col.get('config', {}).get('tamanho_maximo', 50)
                        dados_linha[col['nome']] = fake.text(max_nb_chars=tamanho)
                    elif col['tipo'] == 'Número Inteiro':
                        min_val = col.get('config', {}).get('minimo', 0)
                        max_val = col.get('config', {}).get('maximo', 1000)
                        dados_linha[col['nome']] = fake.random_int(min=int(min_val), max=int(max_val))
                    elif col['tipo'] == 'Número Decimal':
                        min_val = col.get('config', {}).get('minimo', 0)
                        max_val = col.get('config', {}).get('maximo', 1000)
                        dados_linha[col['nome']] = fake.random_number(digits=5, fix_len=True)
                    elif col['tipo'] == 'Data e Hora':
                        formato = col.get('config', {}).get('formato', '%d/%m/%Y')
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
                    elif col['tipo'] == 'CPF':
                        dados_linha[col['nome']] = fake.cpf()
                    elif col['tipo'] == 'CNPJ':
                        dados_linha[col['nome']] = fake.cnpj()
                    elif col['tipo'] == 'RG':
                        dados_linha[col['nome']] = fake.rg()
                        
                session.add(TabelaDinamica(**dados_linha))
                
                # Atualiza a barra de progresso
                progress = (i + 1) / num_linhas * 100
                self.progress_var.set(progress)
                self.status_var.set(f"Gerando dados... {int(progress)}%")
                self.root.update()
                
            session.commit()
            session.close()
            
            # Salva as credenciais
            credenciais = {
                "nome_banco": nome_banco,
                "usuario": self.usuario.get(),
                "senha": self.senha.get(),
                "caminho_banco": f"bancos_dados/{nome_banco}.db",
                "criado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            with open(f"bancos_dados/{nome_banco}_credenciais.json", "w", encoding='utf-8') as f:
                json.dump(credenciais, f, indent=4, ensure_ascii=False)
            
            # Atualiza status final
            self.status_var.set(f"Banco de dados gerado com sucesso: {nome_banco}.db")
            messagebox.showinfo("Sucesso", f"Banco de dados gerado com sucesso!\nArquivo: {nome_banco}.db\nCredenciais: {nome_banco}_credenciais.json")
            
        except Exception as e:
            self.status_var.set("Erro ao gerar banco de dados")
            messagebox.showerror("Erro", f"Erro ao gerar banco de dados: {str(e)}")

    def abrir_pasta_bancos(self):
        """Abre a pasta onde os bancos de dados são salvos"""
        import os
        import subprocess
        
        pasta_bancos = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bancos_dados")
        if not os.path.exists(pasta_bancos):
            os.makedirs(pasta_bancos)
            
        if os.name == 'nt':  # Windows
            os.startfile(pasta_bancos)
        elif os.name == 'posix':  # Linux/Mac
            subprocess.run(['xdg-open', pasta_bancos])

    def toggle_mostrar_senha(self):
        """Alterna entre mostrar e ocultar a senha"""
        if self.mostrar_senha.get():
            self.senha.config(show="")
        else:
            self.senha.config(show="*")

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseGenerator(root)
    root.mainloop() 