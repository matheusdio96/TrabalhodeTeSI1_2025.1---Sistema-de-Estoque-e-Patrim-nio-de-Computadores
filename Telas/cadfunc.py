import ttkbootstrap as tb
from ttkbootstrap.constants import *

class TelaCadastroFuncionario:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Cadastro Funcionário")
        self.janela.geometry("600x500")
        self.janela.resizable(False, False)

        self.lbl_titulo = tb.Label(self.janela, text="Cadastro Funcionário", font=("Helvetica", 16, "bold"))
        self.lbl_titulo.pack(pady=(20, 20))

        self.lbl_nome = tb.Label(self.janela, text="Nome", font=("Helvetica", 10, "bold"))
        self.lbl_nome.pack(anchor="w", padx=140)
        self.ent_nome = tb.Entry(self.janela, width=50, bootstyle="secondary")
        self.ent_nome.pack(pady=(0, 10))

        self.lbl_codigo = tb.Label(self.janela, text="Código", font=("Helvetica", 10, "bold"))
        self.lbl_codigo.pack(anchor="w", padx=140)
        self.ent_codigo = tb.Entry(self.janela, width=50, bootstyle="secondary")
        self.ent_codigo.pack(pady=(0, 10))

        self.lbl_email = tb.Label(self.janela, text="E-mail", font=("Helvetica", 10, "bold"))
        self.lbl_email.pack(anchor="w", padx=140)
        self.ent_email = tb.Entry(self.janela, width=50, bootstyle="secondary")
        self.ent_email.pack(pady=(0, 10))

        self.lbl_telefone = tb.Label(self.janela, text="Telefone", font=("Helvetica", 10, "bold"))
        self.lbl_telefone.pack(anchor="w", padx=140)
        self.ent_telefone = tb.Entry(self.janela, width=50, bootstyle="secondary")
        self.ent_telefone.pack(pady=(0, 20))

        self.lbl_setor = tb.Label(self.janela, text="Setor", font=("Helvetica", 10, "bold"))
        self.lbl_setor.pack(anchor="w", padx=35)

        frame_setor = tb.Frame(self.janela)
        frame_setor.pack(pady=(0, 10), padx=35, fill='x')

        self.ent_setor = tb.Entry(frame_setor, width=30, bootstyle="secondary")
        self.ent_setor.pack(side="left", fill="x", expand=True)

        self.cmb_setor = tb.Combobox(frame_setor, width=20, state="readonly")
        self.cmb_setor['values'] = ["RH", "TI", "Financeiro"]
        self.cmb_setor.pack(side="left", padx=5)

        self.btn_add_setor = tb.Button(frame_setor, text="+", width=3, bootstyle="info")
        self.btn_add_setor.pack(side="left")

        frame_botoes = tb.Frame(self.janela)
        frame_botoes.pack(pady=30)

        self.btn_cancelar = tb.Button(frame_botoes, text="Cancelar", bootstyle="danger", width=15)
        self.btn_cancelar.pack(side="left", padx=10)

        self.btn_cadastrar = tb.Button(frame_botoes, text="Cadastrar", bootstyle="success", width=15)
        self.btn_cadastrar.pack(side="left", padx=10)

        self.chk_gerente = tb.Checkbutton(self.janela, text="Gerente?")
        self.chk_gerente.pack(padx=35)

app = tb.Window(themename="flatly")
TelaCadastroFuncionario(app)
app.mainloop()