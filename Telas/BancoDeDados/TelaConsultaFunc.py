import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Importa o Controller
import control

class TelaConsultaFunc:
    def __init__(self, master):
        self.master = master
        self.master.title("Consulta e Gestão de Funcionários")
        self.master.geometry("1100x600")

        # Inicializa o Controller
        self.controller = control.ControllerFuncionario() 

        # Configuração do Container Principal
        container = tb.Frame(master, padding=20)
        container.pack(fill=BOTH, expand=YES)
        
        # --- Frame de Título ---
        frame_titulo = tb.Frame(container)
        frame_titulo.pack(fill=X, pady=(0, 20))
        tb.Label(frame_titulo, text="Gestão de Funcionários", font=("Helvetica", 24, "bold"), bootstyle="primary").pack(side=LEFT)
        
        # --- Frame de Busca e Filtro ---
        frame_busca = tb.Frame(container)
        frame_busca.pack(fill=X, pady=(0, 15))

        tb.Label(frame_busca, text="Buscar:", bootstyle="secondary").pack(side=LEFT, padx=(0, 10))
        self.entry_busca = tb.Entry(frame_busca, width=50, bootstyle="info")
        self.entry_busca.pack(side=LEFT, fill=X, expand=YES, padx=(0, 20))
        self.entry_busca.bind("<KeyRelease>", self.buscar_funcionario) # Busca em tempo real
       
        # Botão de pesquisar
        self.btn_pesquisar = tb.Button(frame_busca, text="Pesquisar", bootstyle="success", width=12, command=self.buscar_funcionario)
        self.btn_pesquisar.pack(side=LEFT, padx=(0, 10))

        self.btn_limpar = tb.Button(frame_busca, text="Limpar", bootstyle="primary", width=12, command=self.limpar_busca)
        self.btn_limpar.pack(side=LEFT, padx=(10, 0))
        self.btn_limpar = tb.Button(frame_busca, text="Limpar", bootstyle="outline-secondary", width=12, command=self.limpar_busca)
        self.btn_limpar.pack(side=LEFT, padx=(10, 0))

        # --- Treeview (Tabela) ---
        
        # Frame para conter a Treeview e a Scrollbar
        frame_tabela = tb.Frame(container)
        frame_tabela.pack(fill=BOTH, expand=YES)

        # Scrollbar vertical
        scrollbar = tb.Scrollbar(frame_tabela, bootstyle="round-info")
        scrollbar.pack(side=RIGHT, fill=Y)

        # Definindo as colunas
        colunas = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9")
        self.tree = ttk.Treeview(frame_tabela, columns=colunas, show='headings', yscrollcommand=scrollbar.set, bootstyle="primary")
        self.tree.pack(fill=BOTH, expand=YES)

        scrollbar.config(command=self.tree.yview)

        # Configurando os cabeçalhos e largura das colunas
        self.tree.heading("#1", text="ID", anchor=CENTER)
        self.tree.column("#1", width=50, anchor=CENTER, stretch=NO)

        self.tree.heading("#2", text="Cód. Func.", anchor=CENTER)
        self.tree.column("#2", width=100, anchor=CENTER, stretch=NO)

        self.tree.heading("#3", text="Nome", anchor=W)
        self.tree.column("#3", width=250, anchor=W)

        self.tree.heading("#4", text="Setor", anchor=CENTER)
        self.tree.column("#4", width=100, anchor=CENTER)

        self.tree.heading("#5", text="Tem PC?", anchor=CENTER)
        self.tree.column("#5", width=80, anchor=CENTER, stretch=NO)
        
        self.tree.heading("#6", text="Cód. PC", anchor=CENTER)
        self.tree.column("#6", width=100, anchor=CENTER)

        self.tree.heading("#7", text="Patrimônio", anchor=CENTER)
        self.tree.column("#7", width=120, anchor=CENTER)

        self.tree.heading("#8", text="Email", anchor=W)
        self.tree.column("#8", width=200, anchor=W)

        self.tree.heading("#9", text="Telefone", anchor=CENTER)
        self.tree.column("#9", width=120, anchor=CENTER)

        # Adiciona um evento de clique duplo para abrir detalhes/edição
        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.bind("<Button-3>", self.mostrar_menu_contexto) # Botão direito

        # --- Frame de Botões ---
        frame_botoes = tb.Frame(container)
        frame_botoes.pack(fill=X, pady=(20, 0))
        
        # Botão para adicionar novo funcionário
        self.btn_novo = tb.Button(frame_botoes, text="Novo Funcionário", bootstyle="success", width=20, command=self.abrir_cadastro)
        self.btn_novo.pack(side=LEFT, padx=(0, 10))

        self.btn_voltar = tb.Button(frame_botoes, text="Voltar", bootstyle="outline-secondary", width=15, command=self.voltar)
        self.btn_voltar.pack(side=RIGHT)
        
        # Carrega os dados na inicialização
        self.carregar_funcionarios()

    def voltar(self):
        """Ação para o botão Voltar (pode ser substituída por uma lógica de navegação real)."""
        messagebox.showinfo("Voltar", "Função 'Voltar' será implementada para a tela anterior.")
        
    def abrir_cadastro(self):
        """Ação para o botão Novo Funcionário."""
        messagebox.showinfo("Cadastro", "Esta função abrirá a tela de cadastro de novos funcionários.")
        
    # --- Métodos de Leitura e Busca (usando Controller) ---
        
    def carregar_funcionarios(self):
        """Carrega todos os funcionários do banco de dados e exibe na Treeview."""
        # Limpa a Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            # CHAMA O CONTROLLER
            dados = self.controller.listar_funcionarios()
            
            for linha in dados:
                # O Controller retorna a lista na ordem correta: id, codigo_fc, nome, setor, tem_pc, codigo_pc, patrimonio, email, telefone
                id_func, cod_fc, nome, setor, tem_pc, cod_pc, patrimonio, email, telefone = linha
                
                # 'Tem PC?' (0 ou 1)
                tem_pc_display = "Sim" if tem_pc == 1 else "Não"
                
                # O item é inserido na Treeview
                self.tree.insert('', END, values=(id_func, cod_fc, nome, setor, tem_pc_display, cod_pc or '', patrimonio or '', email or '', telefone or ''))
                
        except Exception as e:
            messagebox.showerror("Erro de Leitura", f"Falha ao carregar dados: {e}")


    def buscar_funcionario(self, event=None):
        """Filtra a Treeview com base no texto digitado na barra de busca."""
        termo_busca = self.entry_busca.get().strip()
        
        # Limpa a Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not termo_busca:
            self.carregar_funcionarios()
            return

        try:
            # CHAMA O CONTROLLER com o termo de busca
            dados = self.controller.listar_funcionarios(termo_busca)

            for linha in dados:
                id_func, cod_fc, nome, setor, tem_pc, cod_pc, patrimonio, email, telefone = linha
                tem_pc_display = "Sim" if tem_pc == 1 else "Não"
                self.tree.insert('', END, values=(id_func, cod_fc, nome, setor, tem_pc_display, cod_pc or '', patrimonio or '', email or '', telefone or ''))

        except Exception as e:
            messagebox.showerror("Erro de Busca", f"Falha ao buscar dados: {e}")


    def limpar_busca(self):
        """Limpa o campo de busca e recarrega todos os funcionários."""
        self.entry_busca.delete(0, END)
        self.carregar_funcionarios()

    def mostrar_menu_contexto(self, event):
        """Exibe o menu de contexto (botão direito) na Treeview."""
        item_id = self.tree.identify_row(event.y)
        if not item_id:
            return

        self.tree.selection_set(item_id)
        
        # Obtém os valores do item selecionado
        self.funcionario_selecionado = self.tree.item(item_id, 'values')
        
        menu = tk.Menu(self.master, tearoff=0)
        menu.add_command(label="Detalhes", command=lambda: self.abrir_detalhes(self.funcionario_selecionado))
        menu.add_command(label="Editar", command=lambda: self.abrir_edicao(self.funcionario_selecionado))
        menu.add_command(label="Excluir", command=self.confirmar_exclusao, foreground="red")
        
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()

    def on_double_click(self, event):
        """Trata o clique duplo na Treeview."""
        item = self.tree.selection()[0]
        coluna_id = self.tree.identify_column(event.x)
        
        if coluna_id == "#1": # Coluna ID
            self.funcionario_selecionado = self.tree.item(item, 'values')
            self.abrir_detalhes(self.funcionario_selecionado)
        else:
            # Opção padrão: abrir edição ou detalhes
            self.funcionario_selecionado = self.tree.item(item, 'values')
            self.abrir_edicao(self.funcionario_selecionado)


    # --- Exclusão (usando Controller) ---
    def confirmar_exclusao(self):
        """Confirma a exclusão de um funcionário."""
        if not hasattr(self, 'funcionario_selecionado') or not self.funcionario_selecionado:
            return

        id_funcionario = self.funcionario_selecionado[0]
        nome = self.funcionario_selecionado[2]

        if messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja EXCLUIR o funcionário {nome} (ID: {id_funcionario})?"):
            self.excluir_funcionario(id_funcionario)

    def excluir_funcionario(self, id_funcionario):
        """Executa a exclusão no banco de dados através do Controller."""
        try:
            # CHAMA O CONTROLLER
            linhas_afetadas = self.controller.excluir_funcionario(id_funcionario)

            if linhas_afetadas > 0:
                messagebox.showinfo("Sucesso", f"Funcionário (ID: {id_funcionario}) excluído com sucesso.")
                self.carregar_funcionarios() # Recarrega a lista
            else:
                messagebox.showerror("Erro", "Nenhum funcionário foi excluído. ID não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro de Exclusão", f"Falha ao excluir funcionário: {e}")

    # --- Detalhes/Edição (usando Controller) ---
    
    def abrir_detalhes(self, dados_funcionario):
        """Abre uma janela para visualizar os detalhes do funcionário."""
        detalhes = f"ID: {dados_funcionario[0]}\nCódigo FC: {dados_funcionario[1]}\nNome: {dados_funcionario[2]}\nSetor: {dados_funcionario[3]}\nTem PC: {dados_funcionario[4]}\nCódigo PC: {dados_funcionario[5]}\nPatrimônio: {dados_funcionario[6]}\nEmail: {dados_funcionario[7]}\nTelefone: {dados_funcionario[8]}"
        messagebox.showinfo("Detalhes do Funcionário", detalhes)

    def abrir_edicao(self, dados_funcionario):
        """Abre uma janela para editar os dados do funcionário selecionado."""
        self.top_edicao = tb.Toplevel(self.master)
        self.top_edicao.title(f"Editar Funcionário: {dados_funcionario[2]}")
        self.top_edicao.geometry("450x450")
        
        campos = ["ID", "Código FC", "Nome", "Setor", "Tem PC", "Código PC", "Patrimônio", "Email", "Telefone"]
        self.dados_originais = dict(zip(campos, dados_funcionario))

        frame_form = tb.Frame(self.top_edicao, padding=15)
        frame_form.pack(fill=BOTH, expand=YES)
        
        self.entries = {}
        setores = ["TI", "RH", "Financeiro", "Administrativo", "Vendas", "Operações"]

        for i, (campo, valor) in enumerate(self.dados_originais.items()):
            if campo == "ID": continue 
            
            tb.Label(frame_form, text=f"{campo}:", bootstyle="secondary").grid(row=i, column=0, sticky=W, pady=5, padx=5)
            
            if campo == "Setor":
                entrada = tb.Combobox(frame_form, values=setores, bootstyle="info", state="readonly", width=30)
                entrada.set(valor)
            elif campo == "Tem PC":
                entrada = tb.Combobox(frame_form, values=["Sim", "Não"], bootstyle="info", state="readonly", width=30)
                entrada.set(valor)
            else:
                entrada = tb.Entry(frame_form, bootstyle="info", width=35)
                entrada.insert(0, valor)

            entrada.grid(row=i, column=1, sticky=EW, pady=5, padx=5)
            self.entries[campo] = entrada

        # Botões de ação
        frame_botoes_1 = tb.Frame(frame_form)
        frame_botoes_1.grid(row=len(campos), column=0, columnspan=2, pady=20)
        
        btn_salvar = tb.Button(frame_botoes_1, text="Salvar Edição", bootstyle="success", width=15, command=self.salvar_edicao)
        btn_salvar.pack(side=LEFT, padx=10)
        
        btn_cancelar = tb.Button(frame_botoes_1, text="Cancelar", bootstyle="outline-secondary", width=12, command=self.top_edicao.destroy)
        btn_cancelar.pack(side=LEFT)

    def salvar_edicao(self):
        """Salva as alterações no banco de dados através do Controller."""
        id_funcionario = self.dados_originais["ID"]
        
        # Pega os novos valores dos campos
        novo_cod_fc = self.entries["Código FC"].get().strip()
        novo_nome = self.entries["Nome"].get().strip()
        novo_setor = self.entries["Setor"].get()
        novo_tem_pc_display = self.entries["Tem PC"].get()
        novo_cod_pc = self.entries["Código PC"].get().strip()
        novo_patrimonio = self.entries["Patrimônio"].get().strip()
        novo_email = self.entries["Email"].get().strip()
        novo_telefone = self.entries["Telefone"].get().strip()
        
        # Conversão para o formato do banco de dados
        novo_tem_pc = 1 if novo_tem_pc_display == "Sim" else 0
        
        if not novo_cod_fc or not novo_nome or not novo_setor:
            messagebox.showerror("Erro de Validação", "Código FC, Nome e Setor são campos obrigatórios.")
            return

        try:
            # CHAMA O CONTROLLER
            linhas_afetadas = self.controller.editar_funcionario(
                id_funcionario, novo_cod_fc, novo_nome, novo_setor, 
                novo_email or None, novo_telefone or None, novo_tem_pc, 
                novo_cod_pc or None, novo_patrimonio or None
            )

            if linhas_afetadas > 0:
                messagebox.showinfo("Sucesso", "Dados do funcionário atualizados com sucesso.")
                self.top_edicao.destroy()
                self.carregar_funcionarios() # Recarrega a tabela para refletir a mudança
            else:
                messagebox.showinfo("Aviso", "Nenhuma alteração detectada ou ID não encontrado.")

        except Exception as e:
            messagebox.showerror("Erro de Atualização", f"Falha ao salvar as alterações: {e}")

# Execução (com verificação para evitar execução em ambientes de teste/importação)
if __name__ == "__main__":
    app = tb.Window(themename="flatly")
    TelaConsultaFunc(app)
    app.mainloop()
