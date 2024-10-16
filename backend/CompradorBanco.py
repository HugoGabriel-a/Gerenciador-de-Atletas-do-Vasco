import psycopg2
from backend.Comprador import Comprador

class CompradorBanco:
    def __init__(self):
        self.connect=psycopg2.connect(dbname='Banco_base_vasco',user="postgres",password="270280",host="localhost",port=5432)
        self.cursor=self.connect.cursor()
        self.connect.autocommit=True

    def Create_comprador(self,nome):
        cod_sql=f"INSERT INTO comprador(nome) VALUES ('{nome}')"
        self.cursor.execute(cod_sql)
        
    def get_all_comprador(self):
        cod_sql="SELECT * FROM comprador"
        self.cursor.execute(cod_sql)
        result=self.cursor.fetchall()
        lista_compradores=[]
        if result != None:
            for comprador in result:
                nome=comprador[0]
                cod_comprador=comprador[1]
                cod=comprador[2]
                comprador=Comprador(nome,cod_comprador,cod)
                lista_compradores.append(comprador)
        else:
            lista_compradores=None
        return lista_compradores

    def get_comprador_by_cod(self,cod):
        cod_sql=f"SELECT * FROM comprador WHERE cod_comprador={cod}"
        self.cursor.execute(cod_sql)
        result= self.cursor.fetchone()
        if result != None:
            nome=result[0]
            cod_comprador=result[1]
            cod=result[2]
            comprador=Comprador(nome,cod_comprador,cod)
        else:
            comprador=None
        return comprador
        
    def Compra_Aleta(self,cod_comprador,cod):
        cod_sql=f"UPDATE comprador SET cod={cod} WHERE cod_comprador={cod_comprador}"
        self.cursor.execute(cod_sql)
        
