import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.AtletaBanco import AtletaBanco
from backend.CompradorBanco import CompradorBanco
from frontend.TelaCompradores import tela_compradores

def tela_tabelas():
    janela=tk.Tk()
    janela.geometry("500x300") 
    janela.title("Tabelas")
    janela.title("Tabela Tkinter")

    colunas = ("Nome", "Idade", "Posição","Valor","Status","Codigo")

    tree = ttk.Treeview(janela, columns=colunas, show='headings')

    label=tk.Label(janela,text="lista de atletas",font=('Arial',16))
    label.pack(pady=5)
    tree.heading("Nome", text="Nome")
    tree.heading("Idade", text="Idade")
    tree.heading("Posição", text="Posição")
    tree.heading("Valor", text="Valor")
    tree.heading("Status",text="Status")
    tree.heading("Codigo", text="Codigo")

    tree.column("Nome", width=100)
    tree.column("Idade", width=50)
    tree.column("Posição", width=100)
    tree.column("Valor", width=100)
    tree.column("Status",width=100)
    tree.column("Codigo", width=50)

    lista=AtletaBanco()
    dados = lista.get_all_atletas()
    for atleta in dados:
        if atleta.ativo==True:
            tree.insert("", tk.END, values=(atleta.nome, atleta.idade, atleta.posicao, atleta.valor,atleta.ativo, atleta.cod))
    tree.pack()
    janela.mainloop()

def tela_vendas():
    global entry_cod
    global entry_cod_comprador
    janela=tk.Tk()
    janela.geometry("500x300") 
    janela.title("Coprar Atletas")

    label_cod_comprador = tk.Label(janela, text="Por favor digite o codigo do comprador para quem deseja vender",font=('Arial',13))
    label_cod_comprador.pack(pady=5)

    entry_cod_comprador=tk.Entry(janela)
    entry_cod_comprador.pack(pady=5)

    label_cod = tk.Label(janela, text="Por favor digite o codigo do Atleta que você quer vender",font=('Arial',13))
    label_cod.pack(pady=5)

    entry_cod=tk.Entry(janela)
    entry_cod.pack(pady=5)


    Button_vender_atleta = tk.Button(janela, text="Clique para vender Atletas", font=('Arial',16),command=vender_atleta)
    Button_vender_atleta.pack(pady=10)
    
    janela.mainloop()

def vender_atleta():
    global entry_cod 
    global entry_cod_comprador
    cod=entry_cod.get()
    cod_comprador=entry_cod_comprador.get()

    CB=CompradorBanco()
    comprador=CB.get_comprador_by_cod(cod_comprador)
    print(comprador)
    AB=AtletaBanco()
    jogador_comprado=AB.get_atletas_by_cod(cod)

    if jogador_comprado!=None and comprador != None:
        AB.update_status_atleta_to_False(jogador_comprado.cod)
        compra=CB.Compra_Aleta(cod_comprador,cod)
        messagebox.showinfo ("compra", "Atleta vendido com sucesso!")
    else:
        messagebox.showerror("compra", "impossivel vender atleta")

def tela_reaver():
    global entry_cod_recompra
    janela=tk.Tk()
    janela.geometry("500x300") 
    janela.title("Coprar Atletas")

    label_cod = tk.Label(janela, text="Por favor digite o codigo do Atleta que você quer recomprar",font=('Arial',13))
    label_cod.pack(pady=5)

    entry_cod_recompra=tk.Entry(janela,text="cod")
    entry_cod_recompra.pack(pady=5)


    button_recomprar_atleta= tk.Button(janela, text="Clique para comprar Atletas", font=('Arial',16),command=recomprar_atleta)
    button_recomprar_atleta.pack(pady=10)
    
    janela.mainloop()

def recomprar_atleta():
    global entry_cod_recompra
    cod=entry_cod_recompra.get()

    Ab=AtletaBanco()
    jogador_recomprado=Ab.get_atletas_by_cod(cod)

    if jogador_recomprado != None:
        Ab.reaver_atleta_by_cod(jogador_recomprado.cod)
        messagebox.showinfo ("compra", "Atleta recomprado com sucesso!")
    else:
         messagebox.showerror("compra", "Atleta não encontrado")

def adicionar_atleta():
    global entry_nome
    global entry_idade
    global entry_posicao
    global entry_valor


    
    janela=tk.Tk()
    janela.title("adicionar atletas")
    janela.geometry("500x300")
   

    label_nome=tk.Label(janela,text="Nome",font=("Arial",16))
    label_nome.pack(pady=5)

    entry_nome=tk.Entry(janela)
    entry_nome.pack(pady=5)

    label_idade=tk.Label(janela,text="Idade",font=("Arial",16))
    label_idade.pack(pady=5)
    entry_idade=tk.Entry(janela)
    entry_idade.pack(pady=5)
    
    label_posicao=tk.Label(janela,text="Posicao",font=("Arial",16))
    label_posicao.pack(pady=5)
    entry_posicao=tk.Entry(janela)
    entry_posicao.pack(pady=5)

    label_valor=tk.Label(janela,text="Valor",font=("Arial",13))
    label_valor.pack(pady=5)
    entry_valor=tk.Entry(janela)
    entry_valor.pack(pady=5)

    botao=tk.Button(janela,text="Adcionar Atleta",command=criar)
    botao.pack(pady=5)

    janela.mainloop()

def criar():
    global entry_nome
    global entry_idade
    global entry_posicao
    global entry_valor

    nome=entry_nome.get()
    idade=entry_idade.get()
    posicao=entry_posicao.get()
    valor=entry_valor.get()
    ativo='true'

    AB=AtletaBanco()
    try:
        atleta_criado=AB.create_atleta(nome,idade,posicao,valor,ativo)
        messagebox.showinfo ("compra", "Atleta adcionado com sucesso!")
    except:
        messagebox.showerror('adicionar',"Impossivel Adcionar Jogador")

def atualizar_atleta():

    global entry_cod_at
    janela=tk.Tk()
    janela.title("adicionar atletas")
    janela.geometry("500x300")
   
    label_cod_at=tk.Label(janela,text="Digite o codigo do Atleta que você deseja atualizar")
    label_cod_at.pack(pady=5)
    entry_cod_at=tk.Entry(janela)
    entry_cod_at.pack(pady=5)

    botao=tk.Button(janela,text="buscar",command=verif)
    botao.pack(pady=5)
    janela.mainloop()

def verif():
    global entry_cod_at
    cod=entry_cod_at.get()
    ab=AtletaBanco()
    verif=ab=ab.get_atletas_by_cod(cod)
    if verif != None:
        update()
    else:
        messagebox.showerror("erro","atleta não encontrado")

def update():
    global entry_nome_at
    global entry_idade_at
    global entry_posicao_at
    global entry_valor_at

    janela=tk.Tk()
    janela.title("adicionar atletas")
    janela.geometry("500x300")

    label_nome=tk.Label(janela,text="Nome",font=("Arial",16))
    label_nome.pack(pady=5)

    entry_nome_at=tk.Entry(janela)
    entry_nome_at.pack(pady=5)

    label_idade=tk.Label(janela,text="Idade",font=("Arial",16))
    label_idade.pack(pady=5)
    entry_idade_at=tk.Entry(janela)
    entry_idade_at.pack(pady=5)
    
    label_posicao=tk.Label(janela,text="Posicao",font=("Arial",16))
    label_posicao.pack(pady=5)
    entry_posicao_at=tk.Entry(janela)
    entry_posicao_at.pack(pady=5)

    label_valor=tk.Label(janela,text="Valor",font=("Arial",16))
    label_valor.pack(pady=5)
    entry_valor_at=tk.Entry(janela)
    entry_valor_at.pack(pady=5)

    botao_update=tk.Button(janela,text="Atualizar",command=Atualizar)
    botao_update.pack(pady=5)
    janela.mainloop()

def Atualizar():
    global entry_nome_at
    global entry_idade_at
    global entry_posicao_at
    global entry_valor_at
    global entry_cod_at

    nome=entry_nome_at.get()
    idade=entry_idade_at.get()
    posicao=entry_posicao_at.get()
    valor=entry_valor_at.get()
    cod=entry_cod_at.get()

    ab=AtletaBanco()

    try:
        atualizar=ab.atualizar_atleta(cod,nome,idade,posicao,valor)
        messagebox.showinfo("certo","Atleta Atualizado com sucesso")
    except:
        messagebox.showerror("errado","Impossivel Atualizar Atleta")

def run():
    janela = tk.Tk()
    janela.title("Gerenciador de Atletas da Base Vasco da Gama")  
    janela.geometry("600x500") 
    label=tk.Label(janela,text='Bem vindo ao nosso Gerenciador de atletas', font=('Arial',16))
    label.pack(pady=10)

    Button_ver_atletas = tk.Button(janela, text="Clique para ver os Atletas", font=('Arial',16),command=tela_tabelas)
    Button_ver_atletas.pack(pady=10)

    Button_vender_atleta = tk.Button(janela, text="Clique para vender Atletas", font=('Arial',16),command=tela_vendas)
    Button_vender_atleta.pack(pady=10)

    button_recomprar_atletas = tk.Button(janela, text="Clique para recomprar Atletas", font=('Arial',16),command=tela_reaver)
    button_recomprar_atletas.pack(pady=10)

    button_adicionar_atletas= tk.Button(janela, text="Clique para adicionar Atletas", font=('Arial',16),command=adicionar_atleta)
    button_adicionar_atletas.pack(pady=10)

    button_atualizar_atletas= tk.Button(janela, text="Clique para atualizat Atletas", font=('Arial',16),command=atualizar_atleta)
    button_atualizar_atletas.pack(pady=10)

    button_comprador=tk.Button(janela,text="Compradores",command=tela_compradores,font=("Arial",16))
    button_comprador.pack(pady=5)

    janela.mainloop()
