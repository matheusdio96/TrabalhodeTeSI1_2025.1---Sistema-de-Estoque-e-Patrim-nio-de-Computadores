import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ConfiguracaoLogin

class TelaLogin:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Login")
        self.janela.geometry("300x450")
        self.janela.resizable(False, False)

        self.config = ConfiguracaoLogin

        self.lbl_titulo = ttk.Label(self.janela, text="Login", font=("Helvetica", 16, "bold"))
        self.lbl_titulo.pack(pady=(70, 20))

        self.lbl_usuario = ttk.Label(self.janela, text="Usuário", font=("Helvetica", 10, "bold"))
        self.lbl_usuario.pack(anchor="w", padx=35)
        self.ent_nome = ttk.Entry(self.janela, width=35, bootstyle="secondary")
        self.ent_nome.pack(pady=(0, 10))
 
        #self.ent_nome.insert(0, self.config.usuario_nome) 

        self.lbl_senha = ttk.Label(self.janela, text="Senha", font=("Helvetica", 10, "bold"))
        self.lbl_senha.pack(anchor="w", padx=35)
        self.ent_senha = ttk.Entry(self.janela, width=35, show="*", bootstyle="secondary")
        self.ent_senha.pack(pady=(0, 20))

        #self.ent_senha.insert(0, self.config.usuario_senha) 

        self.btn_entrar = ttk.Button(self.janela, text="Entrar", bootstyle="success", width=20, command=self.fazer_login)
        self.btn_entrar.pack(pady=10)

        self.btn_esqueci = ttk.Button(self.janela, text="Esqueci minha senha", bootstyle="secondary", width=20, command=self.redefinir_senha)
        self.btn_esqueci.pack()

        self.lbl_msg = ttk.Label(self.janela, text="", font=("Helvetica", 9))
        self.lbl_msg.pack(pady=10)

    def fazer_login(self):
        usuario = self.ent_nome.get().strip()
        senha = self.ent_senha.get().strip()

        if usuario == "" or senha == "":
            self.lbl_msg.config(text="Campo vazio, preencha corretamente.", foreground="red")
        elif usuario == self.config.usuario_nome and senha == self.config.usuario_senha:
            self.lbl_msg.config(text="Login realizado com sucesso!", foreground="green")
            #self.janela.destroy()
            #abrir tela principal AQUI
        else:
            self.lbl_msg.config(text="Usuário ou senha incorretos.", foreground="red")

    def redefinir_senha(self):
        #Cria nova janela antes de destruir a atual
        nova_janela = ttk.Window(themename="yeti")
        nova_janela.title("Redefinir Senha")
        nova_janela.geometry("300x460")
        nova_janela.resizable(False, False)
        
        #Inicia a tela de redefinir senha
        TelaRedefinirSenha(nova_janela, self.janela)
        
        #Esconde a janela
        self.janela.withdraw()

def iniciar_tela_login():
    app = ttk.Window(themename="yeti")
    TelaLogin(app)
    app.mainloop()

if __name__ == "__main__":
    iniciar_tela_login()

#python -m ttkbootstrap