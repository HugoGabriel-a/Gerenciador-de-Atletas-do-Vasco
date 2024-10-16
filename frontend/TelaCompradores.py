import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.CompradorBanco import CompradorBanco

def adcionar_comprador():
    global entry_nome
    janela=tk.Tk()
    label_nome=tk.Label(janela,text="Digite seu nome de comprador")
    janela.title("Tela Comprador")
    label_nome.pack(pady=5)
    janela.geometry("500x300") 

    entry_nome=tk.Entry(janela)
    entry_nome.pack(pady=5)

    botao_cadastrar=tk.Button(janela,text='Cadastrar',font=("Arial",13),command=cadastrar)
    botao_cadastrar.pack(pady=5)
    janela.mainloop()

def cadastrar():
    global entry_nome
    nome=entry_nome.get()
    CB=CompradorBanco()
    try:
        cadastrar=CB.Create_comprador(nome)
        messagebox.showinfo("","Comprador Cadastrado")
    except:
        messagebox.showerror("","Impossivel Cadastrar Comprador")

def tabela_todos():

    janela = tk.Tk()
    janela.geometry("500x300") 
    janela.title("Tabela Tkinter")

    colunas = ("Nome", "Codigo_Comprador", "Codigo_Atleta")

    tree = ttk.Treeview(janela, columns=colunas, show='headings')

    label = tk.Label(janela, text="Lista de Compradores", font=('Arial', 16))
    label.pack(pady=5)

    tree.heading("Nome", text="Nome")
    tree.heading("Codigo_Comprador", text="Código Comprador")
    tree.heading("Codigo_Atleta", text="Código Atleta")

    tree.column("Nome", width=100)
    tree.column("Codigo_Comprador", width=100)
    tree.column("Codigo_Atleta", width=100)

    CP=CompradorBanco()
    dados=CP.get_all_comprador()

    for comprador in dados:
        tree.insert("", tk.END, values=(comprador.nome, comprador.cod_comprador, comprador.cod))
    tree.pack(pady=20)  
    janela.mainloop()

def tela_compradores():
    janela=tk.Tk()
    janela.geometry("500x300") 
    janela.title("Tela Comprador")

    button_add_compradores=tk.Button(janela,text="Adcionar Comprador",font=("Arial",16),command=adcionar_comprador)
    button_add_compradores.pack(pady=5)


    button_ver_all=tk.Button(janela,text="ver todos os compradores",font=("Arial",16),command=tabela_todos)
    button_ver_all.pack(pady=5)

    janela.mainloop()
