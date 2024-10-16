import psycopg2
from backend.Usuario import Usuario

class UsuarioBanco:
    def __init__(self):
        pass

    def get_usuario_pelo_nome(self,nome):
        bd_conexao=psycopg2.connect(dbname="Banco_base_vasco",
                                    user="postgres",
                                    password="270280",
                                    host="localhost",
                                    port=5432

        )
        cursor=bd_conexao.cursor()
        cod_sql="SELECT * FROM usuario WHERE nome = '"+nome+"';"
        cursor.execute(cod_sql)

        result=cursor.fetchone()
        bd_conexao.commit()
        bd_conexao.close()

        if result != None:
            nome_usuario= result[0]
            senha_usuario=result[1]
            cod_usuario=result[2]
            usuario=Usuario(nome_usuario,senha_usuario,cod_usuario)
        else:
            usuario=None
        return usuario

