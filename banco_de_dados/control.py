import model

class ControllerFuncionario:
    def __init__(self):
        self.model = model.Model()

    def criar_tabelas(self):
        self.model.create_db()

    def inserir_funcionario(self, nome, cpf, email, telefone):
        sql = (f"INSERT INTO funcionario (nome, codigo, email, telefone) VALUES('{nome}', "
               f"'{cpf}','{email}', {telefone});")
        return self.model.insert(sql)

    def listar_funcionario(self, nome=''):
        sql = f"SELECT * FROM funcionario WHERE nome LIKE '%{nome}%';"
        return self.model.get(sql)

    def excluir_funcionario(self, id):
        sql = f"DELETE FROM funcionario WHERE id={id};"
        return self.model.delete(sql)

    def editar_funcionario(self, id, nome, codigo, email, telefone):
        sql = f"UPDATE funcionario SET nome='{nome}', codigo='{codigo}', email='{email}', telefone='{telefone}' WHERE id={id};"
        return self.model.update(sql)