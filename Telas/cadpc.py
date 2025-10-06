from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import DateEntry


class CadastroPc():
  
    def __init__(self, master):
        
        self.janela = master
        self.janela.title("Cadastro de Computador")
        self.janela.geometry("600x500")
        self.janela.resizable(False, False)

        #componentes


        #container principal dos componentes
        self.container_principal = ttk.Frame(self.janela, padding=20)
        self.container_principal.pack(fill=BOTH, expand=True)


        #titulo da tela
        self.lbl_titulo = ttk.Label(self.container_principal, text="Cadastro de Computador", font=("Helvetica", 16, "bold"))
        self.lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="ew")


        #container dos campos de entrada 1
        self.campos_frame1 = ttk.Frame(self.container_principal)
        self.campos_frame1.grid(row=1, column=0, columnspan=2, sticky="ew")
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
        self.ent_ano = ttk.DateEntry(self.campos_frame1, width=25, bootstyle="secondary")
        self.ent_ano.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        #container dos campos de entrada 2
        self.campos_frame2 = ttk.Frame(self.container_principal)
        self.campos_frame2.grid(row=1, column=1, columnspan=1, sticky="ew")
        self.janela.columnconfigure(1, weight=1)


        self.lbl_patrimonio = ttk.Label(self.campos_frame2, text="Patrimônio: ", font=("Helvetica", 10, "bold"))
        self.lbl_patrimonio.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.ent_patrimonio = ttk.Entry(self.campos_frame2, width=25, bootstyle="secondary")
        self.ent_patrimonio.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.lbl_status = ttk.Label(self.campos_frame2, text="Status: ", font=("Helvetica", 10, "bold"))
        self.lbl_status.grid(row=2, column=2, padx=6, pady=5, sticky="w")
        self.comb_status = ttk.Combobox(self.campos_frame2, values=['Disponível', 'Indisponível' ])
        self.comb_status.grid(row=3, column=2, padx=6, pady=5, sticky="w")

        self.lbl_setor = ttk.Label(self.campos_frame2, text="Setor: ", font=("Helvetica", 10, "bold"))
        self.lbl_setor.grid(row=4, column=2, padx=5, pady=5, sticky="w")
        self.comb_setor = ttk.Combobox(self.campos_frame2, values=['TI', 'RH', 'Financeiro', 'Juridico', 'Estratégico'])
        self.comb_setor.grid(row=5, column=2, padx=5, pady=5, sticky="w")

        
        #caixa de texto

        self.lbl_descricoes = ttk.Label(self.container_principal, text='Descrições/Informações Adicionais: ', font=("Helvetica", 10, "bold"))
        self.lbl_descricoes.grid(row=2, column=0, padx=5, pady=(20, 5), sticky="w")
        self.scrText = ttk.ScrolledText(self.container_principal)
        self.scrText.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.container_principal.rowconfigure(3, weight=1)

        #frame de botões
        frame_botoes = ttk.Frame(self.container_principal)
        frame_botoes.grid(row=4, column=0, columnspan=2, pady=(20, 0))

        self.btn_cancelar = ttk.Button(frame_botoes, text="Cancelar", bootstyle="danger", width=15)
        self.btn_cancelar.pack(side="left", padx=10)

        self.btn_cadastrar = ttk.Button(frame_botoes, text="Cadastrar", bootstyle="sucess", width=15)
        self.btn_cadastrar.pack(side="right", padx=35)

    def cadastrar_pc(self):
        # Lógica para coletar os dados dos campos
        codigo = self.ent_cod.get()
        patrimonio = self.ent_patrimonio.get()
        marca = self.comb_marca.get()
        status = self.comb_status.get()
        ano = self.ent_ano.entry.get() # Pega a data selecionada como string
        setor = self.ent_setor.get()
        descricao = self.scrText.get("1.0", "end-1c")

        # Exibe os dados coletados em uma caixa de mensagem
        dados = f"Código: {codigo}\nPatrimônio: {patrimonio}\nMarca: {marca}\nStatus: {status}\nAno: {ano}\nSetor: {setor}\nDescrição: {descricao}"
        messagebox.showinfo("Dados do PC Cadastrado", dados)
        self.limpar_campos()

    def cancelar_cadastro(self):
        # Fecha a janela ou limpa os campos
        if messagebox.askyesno("Cancelar", "Deseja cancelar o cadastro e fechar a janela?"):
            self.janela.destroy()

    def limpar_campos(self):
        # Limpa todos os campos da interface
        self.ent_cod.delete(0, END)
        self.ent_patrimonio.delete(0, END)
        self.comb_marca.set('')
        self.comb_status.set('')
        self.ent_ano.entry.delete(0, END) # Limpa o campo de entrada do calendário
        self.ent_ano.selected_date = date.today() # Volta o calendário para a data atual
        self.ent_setor.delete(0, END)
        self.scrText.delete("1.0", END)
        self.ent_cod.focus_set()

app = ttk.Window(themename="flatly")
principal = CadastroPc(app)
app.mainloop()