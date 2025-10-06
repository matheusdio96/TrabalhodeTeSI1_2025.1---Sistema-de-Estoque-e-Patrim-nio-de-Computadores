from sqlite3 import Error
# CORREÇÃO: Importa a classe Conexao do módulo conexao dentro do mesmo pacote (ponto .)
import conexao

class Model:
    """
    Camada de acesso a dados (Model) que interage diretamente com o SQLite.
    Todas as consultas SQL são executadas aqui.
    """
    def __init__(self):
        self.con = conexao.Conexao() # Usa a classe Conexao diretamente

    def create_db(self):
        """
        Cria a tabela 'funcionarios' se ela não existir.
        """
        sql = """CREATE TABLE IF NOT EXISTS "funcionarios" (
                "id" INTEGER,
                "codigo_fc" VARCHAR NOT NULL UNIQUE,
                "nome"  VARCHAR NOT NULL,
                "setor" VARCHAR,
                "tem_pc" INTEGER DEFAULT 0,
                "codigo_pc" VARCHAR,
                "patrimonio" VARCHAR,
                "email" VARCHAR,
                "telefone" VARCHAR,
                PRIMARY KEY("id" AUTOINCREMENT)
                );"""
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            con.close()
        except Error as er:
            print(f"Erro ao criar o banco de dados: {er}")

    def get(self, sql, params=()):
        """
        Executa uma consulta SELECT e retorna todos os resultados.
        """
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            # Usa execute com parâmetros para segurança contra SQL injection
            result = cursor.execute(sql, params).fetchall() 
            con.close()
            return result
        except Error as er:
            print(f"Erro GET: {er}")
            return []

    def insert(self, sql, params):
        """
        Executa uma operação INSERT.
        """
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql, params)
            
            if cursor.rowcount >= 1: # Verifica se a inserção foi bem-sucedida
                con.commit()
            con.close()
            return cursor.rowcount
        except Error as er:
            print(f"Erro INSERT: {er}")
            return 0

    def delete(self, sql, params):
        """
        Executa uma operação DELETE.
        """
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql, params)
            if cursor.rowcount >= 1:
                con.commit()
            con.close()
            return cursor.rowcount
        except Error as er:
            print(f"Erro DELETE: {er}")
            return 0

    def update(self, sql, params):
        """
        Executa uma operação UPDATE.
        """
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql, params)
            if cursor.rowcount >= 1:
                con.commit()
            con.close()
            return cursor.rowcount
        except Error as er:
            print(f"Erro UPDATE: {er}")
            return 0
