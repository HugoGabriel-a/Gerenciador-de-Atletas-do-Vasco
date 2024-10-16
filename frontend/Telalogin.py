import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.UsuarioBanco import UsuarioBanco
from frontend.Telahome import run




def login():
    nome = entry_nome.get()
    senha = entry_senha.get()

    usuariobanco = UsuarioBanco()
    usuario = usuariobanco.get_usuario_pelo_nome(nome)

    if usuario !=None and usuario.senha == senha:
        run()
    else:
        messagebox.showerror("Login", "Nome de usuário ou senha incorretos.")


telalogin = tk.Tk()
telalogin.title("Tela de Login")


telalogin.geometry("500x300")
label_nome = tk.Label(telalogin, text="Bem vindo ao Gerenciador de Atletas da base do Vasco da gama",font=('Arial',13))
label_nome.pack(pady=5)


label_nome = tk.Label(telalogin, text="Nome do Usuario:",font=('Arial',16))
label_nome.pack(pady=5)

entry_nome = tk.Entry(telalogin)
entry_nome.pack(pady=5)

label_senha = tk.Label(telalogin, text="Senha:",font=('Arial',16))
label_senha.pack(pady=5)
#aqui esta transformando o texto da senha em *
entry_senha = tk.Entry(telalogin, show="*")
entry_senha.pack(pady=5)


button_login = tk.Button(telalogin, text="Login", command= login , font=('Arial',16))
button_login.pack(pady=20)

telalogin.mainloop()
