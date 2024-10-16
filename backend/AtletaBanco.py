import psycopg2
from backend.Atleta import Atleta

class AtletaBanco:
    def __init__(self):
        self.connection = psycopg2.connect(dbname='Banco_base_vasco',user='postgres',password='270280',host='localhost',port=5432)
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True

    def get_all_atletas(self):
        cod_sql= "SELECT * FROM atleta"
        self.cursor.execute(cod_sql)
        lista_atletas=self.cursor.fetchall()
        lista_atletas_respostas=[]

        for atleta in lista_atletas:

            nome=atleta[0]
            idade=atleta[1]
            posicao=atleta[2]
            valor=atleta[3]
            ativo=atleta[5]
            cod=atleta[4]

            atleta_item = Atleta(nome,idade,posicao,valor,ativo,cod)
            lista_atletas_respostas.append(atleta_item)
        return lista_atletas_respostas
    
    def get_atletas_by_cod(self,cod):
        
        cod_sql=f"SELECT * FROM atleta WHERE cod = {cod};"
        self.cursor.execute(cod_sql)

        result=self.cursor.fetchone()

        if result!=None:
            nome= result[0]
            idade=result[1]
            posicao=result[2]
            valor=result[3]
            ativo=result[5]
            cod=result[4]
            atleta=Atleta(nome,idade,posicao,valor,ativo,cod)
        else:
            atleta=None
        return atleta

    def update_status_atleta_to_False(self,cod):
        
        cod_sql = f"UPDATE atleta SET ativo= false WHERE cod={cod};"
        self.cursor.execute(cod_sql)
        
    def create_atleta(self,nome,idade,posicao,valor,ativo):
        cod_sql= f"INSERT INTO atleta(nome,idade,posicao,valor,ativo) VALUES ('{nome}',{idade},'{posicao}',{valor},{ativo})"
        self.cursor.execute(cod_sql)

    def reaver_atleta_by_cod(self,cod):
        cod_sql=f"UPDATE atleta SET ativo= true WHERE cod={cod};"
        self.cursor.execute(cod_sql)

    def atualizar_atleta(self,cod,nome,idade,posicao,valor):
        cod_sql=f"UPDATE atleta SET nome='{nome}',idade={idade},posicao='{posicao}',valor={valor} WHERE cod={cod}"
        self.cursor.execute(cod_sql)






                
