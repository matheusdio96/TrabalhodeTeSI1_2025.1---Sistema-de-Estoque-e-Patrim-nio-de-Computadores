import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ConfiguracaoLogin:
    usuario_nome = "admin"
    usuario_senha = "admin"
    usuario_resposta = "admin"
    
    def redefinir_credenciais(novo_usuario, nova_senha):
        ConfiguracaoLogin.usuario_nome = novo_usuario
        ConfiguracaoLogin.usuario_senha = nova_senha

class TelaRedefinirSenha:
    def __init__(self, master, janela_login):
        self.janela = master
        self.janela_login = janela_login  # Guarda referência da janela de login
        self.janela.title("Redefinir Senha")
        self.janela.geometry("300x480")
        self.janela.resizable(False, False)

        self.config = ConfiguracaoLogin

        self.lbl_titulo = ttk.Label(self.janela, text="Redefinição de Senha", bootstyle="primary", font=("Helvetica", 16, "bold"))
        self.lbl_titulo.pack(pady=(50, 20))

        #Pergunta
        self.lbl_pergunta = ttk.Label(self.janela, bootstyle="yeti", text="Qual o nome do seu primeiro animal de estimação?", wraplength=250)
        self.lbl_pergunta.pack(pady=10)
        self.ent_resposta = ttk.Entry(self.janela, width=35, bootstyle="secondary")
        self.ent_resposta.pack(pady=(0, 20))

        #Novo Usuário
        self.lbl_user = ttk.Label(self.janela, bootstyle="yeti", text="Novo Usuário:", font=("Helvetica", 10, "bold"))
        self.lbl_user.pack(anchor="w", padx=35)
        self.ent_user = ttk.Entry(self.janela, width=35, bootstyle="secondary")
        self.ent_user.pack(pady=(0, 10))

        #Nova senha
        self.lbl_nova = ttk.Label(self.janela, bootstyle="yeti", text="Nova senha:", font=("Helvetica", 10, "bold"))
        self.lbl_nova.pack(anchor="w", padx=35)
        self.ent_nova = ttk.Entry(self.janela, width=35, show="*", bootstyle="secondary")
        self.ent_nova.pack(pady=(0, 10))

        #Confirmar senha
        self.lbl_conf = ttk.Label(self.janela, bootstyle="yeti", text="Confirmar senha:", font=("Helvetica", 10, "bold"))
        self.lbl_conf.pack(anchor="w", padx=35)
        self.ent_conf = ttk.Entry(self.janela, width=35, show="*", bootstyle="secondary")
        self.ent_conf.pack(pady=(0, 20))

        #Botões
        self.btn_salvar = ttk.Button(self.janela, text="Salvar", bootstyle="success", width=20, command=self.salvar_nova_senha)
        self.btn_salvar.pack(pady=5)

        self.btn_cancelar = ttk.Button(self.janela, text="Cancelar", bootstyle="secondary", width=20, command=self.voltar_login)
        self.btn_cancelar.pack(pady=5)

        self.lbl_msg = ttk.Label(self.janela, bootstyle="yeti", text="", font=("Helvetica", 10, "bold"))
        self.lbl_msg.pack(pady=10)
        
        #Configurar o fechamento da janela
        self.janela.protocol("WM_DELETE_WINDOW", self.voltar_login)

    def salvar_nova_senha(self):
        resposta = self.ent_resposta.get().strip().lower()
        novo_usuario = self.ent_user.get().strip()
        nova_senha = self.ent_nova.get().strip()
        conf_senha = self.ent_conf.get().strip()

        #Validações
        if resposta == "" or novo_usuario == "" or nova_senha == "" or conf_senha == "":
            self.lbl_msg.config(text="Campo vazio, preencha corretamente.", foreground="red")
        elif resposta != self.config.usuario_resposta:
            self.lbl_msg.config(text="Resposta incorreta.", foreground="red")
        elif nova_senha != conf_senha:
            self.lbl_msg.config(text="As senhas não coincidem.", foreground="red")
        elif len(nova_senha) < 4:
            self.lbl_msg.config(text="A senha deve ter pelo menos 4 caracteres.", foreground="red")
        else:
            self.config.redefinir_credenciais(novo_usuario, nova_senha)
            self.lbl_msg.config(text="Usuário e senha redefinidos com sucesso!", foreground="green")
            #Volta para a tela de login após 2,5 segundos
            self.janela.after(2500, self.voltar_login)

    def voltar_login(self): 
        #Fecha a janela atual e reabre a de login
        self.janela.destroy()
        if self.janela_login:
            self.janela_login.deiconify()

def iniciar_tela_redefinir_senha():
    app = ttk.Window(themename="yeti")
    TelaRedefinirSenha(app, None)
    app.mainloop()

if __name__ == "__main__":
    iniciar_tela_redefinir_senha()