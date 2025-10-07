from tkinter import messagebox, END
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import DateEntry
from datetime import date
import control

class CadastroPc():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Cadastro de Computador")
        self.janela.geometry("700x600")

        # self.controller = ControllerPc()  # Descomente quando criar o controller

        self.container_principal = ttk.Frame(self.janela, padding=20)
        self.container_principal.pack(fill=BOTH, expand=True)

        self.lbl_titulo = ttk.Label(self.container_principal, text="Cadastro de Computador", font=("Helvetica", 16, "bold"))
        self.lbl_titulo.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="ew")

        self.campos_frame1 = ttk.Frame(self.container_principal)
        self.campos_frame1.grid(row=1, column=0, sticky="nsew")
        self.janela.columnconfigure(0, weight=1)

        self.lbl_cod = ttk.Label(self.campos_frame1, text="Código: ", font=("Helvetica", 10, "bold"))
        self.lbl_cod.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_cod = ttk.Entry(self.campos_frame1, width=25, bootstyle="secondary")
        self.ent_cod.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.lbl_marca = ttk.Label(self.campos_frame1, text="Marca: ", font=("Helvetica", 10, "bold"))
        self.lbl_marca.grid(row=2, column=0, padx=6, pady=5, sticky="w")
        self.comb_marca = ttk.Combobox(self.campos_frame1, values=['Dell', 'Samsung', 'Acer', 'Lenovo', 'Hp', 'Avell', 'Vaio', 'Asus'])
        self.comb_marca.grid(row=3, column=0, padx=6, pady=5, sticky="w")

        self.lbl_ano = ttk.Label(self.campos_frame1, text="Ano: ", font=("Helvetica", 10, "bold"))
        self.lbl_ano.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.ent_ano = DateEntry(self.campos_frame1, width=25, bootstyle="secondary")
        self.ent_ano.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.campos_frame2 = ttk.Frame(self.container_principal)
        self.campos_frame2.grid(row=1, column=1, sticky="nsew")
        self.janela.columnconfigure(1, weight=1)

        self.lbl_patrimonio = ttk.Label(self.campos_frame2, text="Patrimônio: ", font=("Helvetica", 10, "bold"))
        self.lbl_patrimonio.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.ent_patrimonio = ttk.Entry(self.campos_frame2, width=25, bootstyle="secondary")
        self.ent_patrimonio.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.lbl_status = ttk.Label(self.campos_frame2, text="Status: ", font=("Helvetica", 10, "bold"))
        self.lbl_status.grid(row=2, column=2, padx=6, pady=5, sticky="w")
        self.comb_status = ttk.Combobox(self.campos_frame2, values=['Disponível', 'Indisponível'])
        self.comb_status.grid(row=3, column=2, padx=6, pady=5, sticky="w")

        self.lbl_setor = ttk.Label(self.campos_frame2, text="Setor: ", font=("Helvetica", 10, "bold"))
        self.lbl_setor.grid(row=4, column=2, padx=5, pady=5, sticky="w")
        self.comb_setor = ttk.Combobox(self.campos_frame2, values=['TI', 'RH', 'Financeiro', 'Juridico', 'Estratégico'])
        self.comb_setor.grid(row=5, column=2, padx=5, pady=5, sticky="w")

        self.lbl_descricoes = ttk.Label(self.container_principal, text='Descrições/Informações Adicionais: ', font=("Helvetica", 10, "bold"))
        self.lbl_descricoes.grid(row=2, column=0, padx=5, pady=(20, 5), sticky="w")
        self.scrText = ttk.ScrolledText(self.container_principal)
        self.scrText.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
        self.container_principal.rowconfigure(3, weight=1)

        frame_botoes = ttk.Frame(self.container_principal)
        frame_botoes.grid(row=4, column=0, columnspan=3, pady=(20, 0))

        self.btn_cancelar = ttk.Button(frame_botoes, text="Cancelar", bootstyle="danger", width=15, command=self.cancelar_cadastro)
        self.btn_cancelar.pack(side="left", padx=10)

        self.btn_limpar = ttk.Button(frame_botoes, text="Limpar", bootstyle="warning", width=15, command=self.confirmar_limpar)
        self.btn_limpar.pack(side="left", padx=10)

        self.btn_cadastrar = ttk.Button(frame_botoes, text="Cadastrar", bootstyle="success", width=15, command=self.confirmar_cadastro)
        self.btn_cadastrar.pack(side="right", padx=35)

    def campos_obrigatorios_preenchidos(self):
        return (
            self.ent_cod.get().strip() and
            self.ent_patrimonio.get().strip() and
            self.comb_marca.get().strip() and
            self.comb_status.get().strip() and
            self.ent_ano.entry.get().strip() and
            self.comb_setor.get().strip()
        )

    def confirmar_cadastro(self):
        if not self.campos_obrigatorios_preenchidos():
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")
            return
        if messagebox.askyesno("Confirmação", "Deseja realmente cadastrar este computador?"):
            self.cadastrar_pc()

    def inserir_pc(self):
        codigo = self.ent_cod.get().strip()
        patrimonio = self.ent_patrimonio.get().strip()
        marca = self.comb_marca.get().strip()
        status = self.comb_status.get().strip()
        ano = self.ent_ano.entry.get().strip()
        setor = self.comb_setor.get().strip()
        descricao = self.scrText.get("1.0", "end-1c").strip()

        # Salvar no banco de dados (descomente e ajuste quando tiver o controller/model)
        resultado = self.inserir_pc(codigo, patrimonio, marca, status, ano, setor, descricao)
        if resultado == 1:
            messagebox.showinfo("Sucesso", "Computador cadastrado com sucesso!")
            self.janela.destroy()  # Volta para tela principal
        else:
            messagebox.showerror("Erro", "Erro ao cadastrar computador.")

        # Exemplo temporário:
        messagebox.showinfo("Sucesso", "Computador cadastrado com sucesso!")
        self.janela.destroy()  # Volta para tela principal

    def cancelar_cadastro(self):
        if messagebox.askyesno("Cancelar", "Deseja cancelar o cadastro e voltar para a tela principal?"):
            self.janela.destroy()

    def confirmar_limpar(self):
        if messagebox.askyesno("Limpar", "Deseja realmente limpar todos os campos?"):
            self.limpar_campos()

    def limpar_campos(self):
        self.ent_cod.delete(0, END)
        self.ent_patrimonio.delete(0, END)
        self.comb_marca.set('')
        self.comb_status.set('')
        self.ent_ano.entry.delete(0, END)
        self.ent_ano.selected_date = date.today()
        self.comb_setor.set('')
        self.scrText.delete("1.0", END)
        self.ent_cod.focus_set()

app = ttk.Window(themename="flatly")
principal = CadastroPc(app)
app.mainloop()