import dbAPI

def main():

    # Esse MAIN testa a API e É DIFERENTE DO MAIN() DO MODULO dbAPI!!!

    conn = dbAPI.getConnection()
    cur = conn.cursor()    

    print("Apagando conteudo da tabela PESSOA")
    dbAPI.pessoa.truncate(conn)

    p1 = dbAPI.pessoa()
    p1.nome = "João da Silva"
    p1.data_criacao = "01/01/2021"
    p1.insert(conn)
    print("João criado")


    p2 = dbAPI.pessoa()
    p2.nome = "Maria da Silva"
    p2.data_criacao = "01/01/2021"
    p2.insert(conn)
    print("Maria criada")    

    print("Imprimindo resultado do insert")
    dbAPI.pessoa.listall(conn)

    print("Atualizando João")
    p1.data_criacao = '30/02/2010'
    p1.update(conn)

    print("Imprimindo resultado do update do João")
    dbAPI.pessoa.listall(conn)    

    print("Apagando Maria")    
    p2.delete(conn)

    print("Imprimindo resultado do delete da Maria")
    dbAPI.pessoa.listall(conn)        

    conn.close()

if __name__ == "__main__":
    main()