"""
Module: dbAPI
Description: Modelo de uma API/Crud para um banco de dados sqlite3
Autor: Henrique Araujo
Data: 27/11/2021
"""

import sqlite3
import os, string, random
import database as db

# Criando uma variável global para o banco de dados
DATABASE = ""

def createDb(p_conn):
    #script de criação de uma tabela
    sqlcmd = """CREATE TABLE IF NOT EXISTS PESSOA (
	            "id"	TEXT NOT NULL,
	            "nome"	TEXT,
	            "data_criacao"	TEXT,
	            PRIMARY KEY("id")
                )
                """
    #cria a tabela
    cur = p_conn.cursor()
    cur.execute(sqlcmd)                

# Esse método é para gerar uma chave para criarmos os registros na tabela, a primary key
def generate_key(stringLength=10):
    """Objective: Generate a random string of fixed length """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


def getConnection():
    # Essa linha é para pegar o diretório e criar o banco no lugar certo
    global DATABASE
    DB_FOLDER = os.getcwd()
    DATABASE = DB_FOLDER + "\\database-crud-python-sqlite3\\myCrudDb.db"    
    print('Banco será: ',DATABASE)

    # Cria uma conexão com myCrudDb.db. Se o banco não existir, irá criá-lo
    conn = db.sqlite3Connection(DATABASE)
    return conn

class pessoa:
    def __init__(self):
        self.id = ""
        self.nome = ""
        self.data_criacao = ""

    def display(self):
        print(self.id, " - ", self.nome, " - ", self.data_criacao)

    def loadObj(self, p_conn):
        # se o ID não for informado, mostra mensage. O id deve ser informado em uma instance de pessoa.id
        if self.id == None:
            print("ID não informado")
        else:
            sqlcmd = "select nome, data_criacao from PESSOA where id = ?"
            cur = p_conn.execute(sqlcmd, (self.id))
            for row in cur:
                self.nome = row[0]
                self.data_criacao = row[1]

    def insert(self, p_conn):
        sqlcmd="insert into PESSOA(id, nome, data_criacao) values(?,?,?)"

        self.id = db.generate_key()
        
        try:
            cursor = p_conn.execute(sqlcmd, (self.id, self.nome, self.data_criacao ))
            p_conn.commit()
            print("operation executed")
            
        except sqlite3.OperationalError:
            p_conn.rollback()
            print("error in operation")

    def update(self, p_conn):
        sqlcmd="update PESSOA set nome = ?, data_criacao = ? where id = ?"
        try:
            cursor = p_conn.execute(sqlcmd, (self.nome, self.data_criacao, self.id ))
            p_conn.commit()
            print("operation executed")
        
        except sqlite3.OperationalError:
            p_conn.rollback()
            print("error in operation")

    def delete(self, p_conn):
        sqlcmd = "delete from PESSOA where id = ?"

        try:
            cursor = p_conn.execute(sqlcmd, ([self.id])) 
            p_conn.commit()
            print("operation executed")
        except sqlite3.OperationalError:
            p_conn.rollback()
            print("Error in operation. Database locked")

    @staticmethod
    def truncate(p_conn):
        sqlcmd = "delete from PESSOA"

        try:
            cursor = p_conn.execute(sqlcmd) 
            p_conn.commit()
            print("operation executed")
        except sqlite3.OperationalError:
            p_conn.rollback()
            print("Error in operation. Database locked")

    @staticmethod    
    def listall(p_conn):
        sqlcmd= "SELECT id, nome, data_criacao from PESSOA"
        cursor = p_conn.execute(sqlcmd)
        for row in cursor:
            print(row)



def main():

    # Esse MAIN testa a API.
    # Quando dbAPI for importado em main.py, esse trecho não será executado

    conn = getConnection()
    cur = conn.cursor()    
    createDb(conn)

    print("Apagando conteudo da tabela PESSOA")
    pessoa.truncate(conn)

    joao = pessoa()
    joao.nome = "João da Silva"
    joao.data_criacao = "01/01/2021"
    joao.insert(conn)
    print("João criado")


    maria = pessoa()
    maria.nome = "Maria da Silva"
    maria.data_criacao = "01/01/2021"
    maria.insert(conn)
    print("Maria criada")    

    print("Imprimindo resultado do insert")
    pessoa.listall(conn)

    print("Atualizando João")
    joao.data_criacao = '30/02/2010'
    joao.update(conn)

    print("Imprimindo resultado do update do João")
    pessoa.listall(conn)    

    print("Apagando Maria")    
    maria.delete(conn)

    print("Imprimindo resultado do delete da Maria")
    pessoa.listall(conn)        

    conn.close()

if __name__ == "__main__":
    main()