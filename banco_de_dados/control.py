from model import Model 

class ControllerFuncionario:
    """
    Controlador responsável por intermediar as requisições da interface (View)
    e a lógica de acesso a dados (Model).
    """
    def __init__(self):
        # CORREÇÃO CRUCIAL: Uso da importação relativa para garantir que o 'model.py' seja encontrado
        self.model = Model()

    def criar_tabelas(self):
        """
        Garante que as tabelas necessárias (funcionarios) estão criadas. 
        """
        self.model.create_db()

    def inserir_funcionario(self, codigo_fc, nome, setor, email, telefone, tem_pc=0, codigo_pc=None, patrimonio=None):
        """
        Insere um novo funcionário. 
        """
        sql = (
            "INSERT INTO funcionarios (codigo_fc, nome, setor, email, telefone, tem_pc, codigo_pc, patrimonio) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
        )
        params = (codigo_fc, nome, setor, email, telefone, tem_pc, codigo_pc, patrimonio)
        
        return self.model.insert(sql, params)

    def listar_funcionarios(self, termo_busca=''):
        """
        Lista funcionários, opcionalmente filtrando por nome ou código do funcionário.
        """
        if termo_busca:
            sql = f"SELECT id, codigo_fc, nome, setor, tem_pc, codigo_pc, patrimonio, email, telefone FROM funcionarios WHERE nome LIKE ? OR codigo_fc LIKE ? ORDER BY nome"
            return self.model.get(sql, (f'%{termo_busca}%', f'%{termo_busca}%'))
        else:
            sql = "SELECT id, codigo_fc, nome, setor, tem_pc, codigo_pc, patrimonio, email, telefone FROM funcionarios ORDER BY nome"
            return self.model.get(sql)


    def excluir_funcionario(self, id):
        """Exclui um funcionário pelo ID."""
        sql = "DELETE FROM funcionarios WHERE id=?;"
        return self.model.delete(sql, (id,))

    def editar_funcionario(self, id, codigo_fc, nome, setor, email, telefone, tem_pc=0, codigo_pc=None, patrimonio=None):
        """
        Atualiza os dados de um funcionário.
        """
        sql = (
            "UPDATE funcionarios SET codigo_fc=?, nome=?, setor=?, email=?, telefone=?, "
            "tem_pc=?, codigo_pc=?, patrimonio=? WHERE id=?"
        )
        params = (codigo_fc, nome, setor, email, telefone, tem_pc, codigo_pc, patrimonio, id)
        
        return self.model.update(sql, params)
