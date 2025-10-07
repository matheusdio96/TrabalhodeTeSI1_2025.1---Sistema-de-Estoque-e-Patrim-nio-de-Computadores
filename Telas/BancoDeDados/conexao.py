import sqlite3
from sqlite3 import Error

class Conexao:
    """
    Classe responsável por estabelecer e retornar a conexão com o banco de dados SQLite.
    """
    def get_conexao(self):
        # ATENÇÃO: Este é o caminho absoluto que você especificou. 
        # Garanta que o arquivo banco_tesi1.db exista neste local antes de executar.
        caminho = r'C:\Users\mathe\Tesi 1 2025.1\Projeto-n2\banco_de_dados\banco_tesi1.db'
        
        try:
            con = sqlite3.connect(caminho)
            print("Conexão com o banco de dados estabelecida com sucesso!")
            return con
        except Error as er:
            # Mensagem mais clara e informativa
            print(f"Erro ao conectar ao banco de dados em '{caminho}': {er}")
            # Retorna None para indicar que a conexão falhou
            return None
