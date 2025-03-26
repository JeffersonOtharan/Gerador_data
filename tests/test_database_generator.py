import unittest
import os
import json
from database_generator import DatabaseGenerator

class TestDatabaseGenerator(unittest.TestCase):
    def setUp(self):
        self.app = DatabaseGenerator()
        
    def test_adicionar_coluna(self):
        # Testa adicionar uma coluna
        self.app.adicionar_coluna()
        self.assertEqual(len(self.app.colunas), 1)
        
        # Verifica se os widgets foram criados
        col_frame = self.app.colunas_frame.winfo_children()[0]
        self.assertIsNotNone(col_frame.nome_entry)
        self.assertIsNotNone(col_frame.tipo_combo)
        
    def test_salvar_configuracao(self):
        # Adiciona uma coluna
        self.app.adicionar_coluna()
        
        # Define valores
        col_frame = self.app.colunas_frame.winfo_children()[0]
        col_frame.nome_entry.insert(0, "teste")
        col_frame.tipo_combo.set("Texto")
        
        # Salva configuração
        self.app.salvar_configuracao()
        
        # Verifica se o arquivo foi criado
        self.assertTrue(os.path.exists("configuracao.json"))
        
        # Verifica conteúdo
        with open("configuracao.json", "r", encoding="utf-8") as f:
            config = json.load(f)
            self.assertEqual(config["colunas"][0]["nome"], "teste")
            self.assertEqual(config["colunas"][0]["tipo"], "Texto")
            
    def tearDown(self):
        # Limpa arquivos de teste
        if os.path.exists("configuracao.json"):
            os.remove("configuracao.json")
        self.app.root.destroy()

if __name__ == "__main__":
    unittest.main() 