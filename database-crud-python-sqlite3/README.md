#CRUD Básico com Sqlite3

Esse exemplo de CRUD em um sqlite3 é bem interessante. Existem várias formas de fazer isso, mas achei essa a melhor. Basicamente:
- Temos uma classe de objeto representando uma tabela no banco de dados, PESSOAS, no exemplo.
- A classe tem os métodos insert, delete, update, display, listall e truncate, o CRUD e algumas coisas a mais.
- Instanciamos o objeto que queremos usando a classe pessoa, e chamamos o metodo CRUD passando a conexão criada com o banco.

Outro ponto importante:
- Temos um modulo dbAPI, que conhece o banco de dados e faz o CRUD.
- O modulo main import dbAPI para acessar o banco. Veja que o módulo main não sabe sobre o banco, nem que é um sqlite3. Isolamos essa camada de lógica da camada de banco de dados e, dbAPI, o que é muito bom.

**Steps:**
1) Primeiro vamos importar o arquivo database.py, que está em "database-basics". Esse módulo tem umas funções de banco de dados.
2) Depois iremos criar 2 arquivos:
    dbAPI.py - Com o código necessário para o CRUD (é a camada de acesso à dados)
    main.py - Com o código que irá testar o dbAPI.py (basicamente é a camada de logica do sistema)
3) Começando pelo dbAPI.py, iremos:
    a. Criar o banco de dados
    b. Criar uma classe sobre a tabela do banco de dados
    c. Implementar o crud nesta classe
4) Depois, no main.py:
    a. Importaremos o dbAPI
    b. Testaremos as operações de crud


    