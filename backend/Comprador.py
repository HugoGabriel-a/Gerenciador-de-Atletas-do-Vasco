class Comprador:
    def __init__(self,nome,cod_comprador,cod=None):
        self.nome=nome
        self.cod_comprador=cod_comprador
        self.cod=cod
    def __str__(self):
        return f"Nome: {self.nome}\nCodigo Coprador: {self.cod_comprador}\nCodigo Atletas: {self.cod}"
