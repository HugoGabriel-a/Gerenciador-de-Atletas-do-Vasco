class Usuario:
    def __init__(self,nome,senha,cod):
        self.nome=nome
        self.senha=senha
        self.cod=cod
    
    def __str__(self):
        return f"Nome: {self.nome}\nSenha: {self.senha}\nCodigo: {self.cod}"