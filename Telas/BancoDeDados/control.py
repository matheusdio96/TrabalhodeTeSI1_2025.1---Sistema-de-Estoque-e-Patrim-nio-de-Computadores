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

class ControllerComputadores:
    """
    Controlador responsável por intermediar as requisições da interface (View)
    e a lógica de acesso a dados (Model) para a entidade COMPUTADOR.
    """
    def __init__(self):
        self.model = Model()

    def inserir_computador(self, id, marca, patrimonio, status, ano, setor, descricoes):
        """
        Cadastra um novo computador no sistema, utilizando o método do Model.
        """
        # Chama diretamente o método insert_computador que foi adicionado no Model.py
        return self.model.insert_computador(
            id, 
            marca,  
            patrimonio, 
            status, 
            ano, 
            setor, 
            descricoes, 
        )

    # EXEMPLO: Método para listar computadores (opcional)
    def listar_computadores(self, termo_busca=''):
        """
        Lista todos os computadores, ou filtra por código ou marca.
        """
        if termo_busca:
            sql = f"SELECT * FROM computadores WHERE id LIKE ? OR marca LIKE ? ORDER BY patrimonio"
            return self.model.get(sql, (f'%{termo_busca}%', f'%{termo_busca}%'))
        else:
            sql = "SELECT * FROM computadores ORDER BY patrimonio"
            return self.model.get(sql)
        
    def editar_computador(self, id, marca, patrimonio, status, ano, setor, descricoes):
        """
        Atualiza todos os dados de um computador existente com base no ID.
        """
        sql = """
            UPDATE computadores SET marca=?, patrimonio=?, 
            status=?, setor=?, ano=?, setor=?, 
            localizacao=? WHERE id=?
        """
        params = (
            marca, patrimonio, status, 
            ano, setor, descricoes, id
        )
        
        return self.model.update(sql, params) # Reutiliza o método update() do Model

    def excluir_computador(self, id):
        """
        Exclui um computador do banco de dados pelo seu ID.
        """
        sql = "DELETE FROM computadores WHERE id=?"
        return self.model.delete(sql, (id,)) # Reutiliza o método delete() do Model
