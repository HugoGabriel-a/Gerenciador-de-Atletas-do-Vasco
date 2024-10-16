class Atleta:
    def __init__(self,nome,idade,posicao,valor,cod,ativo=None):
        self.nome=nome
        self.idade=idade
        self.posicao=posicao
        self.valor=valor
        self.ativo=ativo
        self.cod=cod

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nPosicao: {self.posicao}\nValor: {self.valor}\nStatus: {self.ativo}\nCodigo: {self.cod}'
    
